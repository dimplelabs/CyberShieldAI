import re
from typing import List, Dict

PATTERNS = {
    "SQL injection": [
        r"(?i)(\bunion\b\s+\bselect\b|\b(?:or|and)\b\s+['\"]?[^\s'\"]+['\"]?\s*=\s*['\"]?[^\s'\"]+['\"]?|\bdrop\s+table\b|\binsert\s+into\b|\bselect\b.+\bfrom\b)",
    ],
    "XSS": [r"(?i)(<script\b|javascript:|on(?:error|load|click)\s*=)"],
    "Command injection": [r"(?i)(;\s*(?:cat|curl|wget|bash|sh|powershell|cmd)\b|\|\s*(?:cat|curl|wget|bash|sh)\b|\$\([^)]*\))"],
    "Path traversal": [r"(?:\.\./|\.\.\\|%2e%2e%2f|%2e%2e%5c)"],
}

def scan_text(text: str) -> Dict:
    text = text or ""
    findings: List[Dict] = []
    for category, patterns in PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text):
                findings.append({"category": category, "pattern": pattern})
                break
    level = "High Risk" if findings else "Low Risk"
    return {
        "risk_level": level,
        "findings": findings,
        "summary": "Potential attack patterns detected." if findings else "No configured attack patterns detected.",
    }
