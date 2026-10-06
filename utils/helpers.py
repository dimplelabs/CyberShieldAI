import html
import re

def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())

def risk_class(level: str) -> str:
    return {"Low Risk":"low","Suspicious":"medium","High Risk":"high"}.get(level, "info")

def escape(value: str) -> str:
    return html.escape(str(value or ""))
