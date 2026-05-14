from typing import Literal, TypeAlias

from pydantic import BaseModel, Field

from app.models.enums import SectorCode
from app.schemas.common import SourceInfo, WarningMessage


AnalysisIndicatorIntent: TypeAlias = Literal["positive", "neutral", "negative"]


class AnalysisIndicator(BaseModel):
    label: str
    value: str
    intent: AnalysisIndicatorIntent


class KeyEvidence(BaseModel):
    title: str
    description: str
    source: SourceInfo | None = None


class SectorAnalysisResponse(BaseModel):
    sector: SectorCode
    beginner_summary: str
    key_evidence: list[KeyEvidence]
    indicators: list[AnalysisIndicator] = Field(default_factory=list)
    sources: list[SourceInfo] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)
    caution: str
    warnings: list[WarningMessage] = Field(default_factory=list)
