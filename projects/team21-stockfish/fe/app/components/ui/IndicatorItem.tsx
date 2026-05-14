import { type ReactNode } from "react";
import { cn } from "~/utils/cn";

export interface IndicatorItemProps {
  intent: "positive" | "negative" | "neutral";
  label: string;
  value: string;
  icon?: ReactNode;
  className?: string;
}

export function IndicatorItem({ intent, label, value, icon, className }: IndicatorItemProps) {
  const colorClass =
    intent === "positive"
      ? "text-success-600"
      : intent === "negative"
        ? "text-danger-600"
        : "text-neutral-500";
  const borderClass =
    intent === "positive"
      ? "border-success-600"
      : intent === "negative"
        ? "border-danger-600"
        : "border-neutral-300";

  return (
    <div
      className={cn(
        "flex items-center justify-between px-3 py-3 rounded-xl border bg-white min-w-72 flex-1",
        borderClass,
        className,
      )}
    >
      <div className="flex items-center gap-2">
        <span className={cn("text-base font-medium", colorClass)}>{label}</span>
        {icon && (
          <div className={cn("size-3.5 flex items-center justify-center", colorClass)}>{icon}</div>
        )}
      </div>
      <span className={cn("text-base", colorClass)}>{value}</span>
    </div>
  );
}
