from app.ai.state import IndicatorContext
from app.schemas.analysis import AnalysisIndicator, AnalysisIndicatorIntent


def build_analysis_indicators(
    indicator_context: IndicatorContext | None,
) -> list[AnalysisIndicator]:
    if indicator_context is None:
        return []

    comparison = indicator_context.comparison
    indicators: list[AnalysisIndicator] = []

    if comparison.average_change_percent is not None:
        indicators.append(
            AnalysisIndicator(
                label="평균 등락률",
                value=_format_percent(comparison.average_change_percent),
                intent=_intent_from_change(comparison.average_change_percent),
            )
        )

    if comparison.total_volume is not None:
        indicators.append(
            AnalysisIndicator(
                label="거래량",
                value=f"{comparison.total_volume:,}주",
                intent=_intent_from_change(comparison.average_change_percent),
            )
        )

    if comparison.rising_count or comparison.falling_count:
        indicators.append(
            AnalysisIndicator(
                label="상승/하락 종목 수",
                value=f"{comparison.rising_count}상승 / {comparison.falling_count}하락",
                intent=_intent_from_counts(
                    rising_count=comparison.rising_count,
                    falling_count=comparison.falling_count,
                ),
            )
        )

    return indicators


def _intent_from_change(value: float | None) -> AnalysisIndicatorIntent:
    if value is None:
        return "neutral"
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "neutral"


def _intent_from_counts(
    *,
    rising_count: int,
    falling_count: int,
) -> AnalysisIndicatorIntent:
    if rising_count > falling_count:
        return "positive"
    if falling_count > rising_count:
        return "negative"
    return "neutral"


def _format_percent(value: float) -> str:
    sign = "+" if value >= 0 else ""
    return f"{sign}{value:.2f}%"
