import ipaddress
import re
from urllib.parse import urlparse

SHORTENERS = {"bit.ly","tinyurl.com","t.co","is.gd","ow.ly","buff.ly","cutt.ly","shorturl.at"}
SUSPICIOUS_WORDS = {"login","verify","verification","secure","update","account","password","wallet","payment","gift","prize","urgent","claim"}

def analyze_url(url: str) -> dict:
    raw = (url or "").strip()
    if not raw:
        return {"risk_level":"Suspicious","score":0,"indicators":["No URL was provided."],"explanation":"Enter a URL to analyze it."}
    candidate = raw if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", raw) else "http://" + raw
    try:
        p = urlparse(candidate)
    except Exception:
        return {"risk_level":"High Risk","score":100,"indicators":["URL could not be parsed."],"explanation":"The URL structure is malformed."}
    indicators=[]; score=0
    if p.scheme.lower() != "https":
        indicators.append("Uses HTTP instead of HTTPS."); score += 20
    host=(p.hostname or "").lower().rstrip(".")
    if not host:
        indicators.append("Missing domain/host."); score += 60
    try:
        ipaddress.ip_address(host)
        indicators.append("Uses a raw IP address instead of a domain."); score += 35
    except ValueError:
        pass
    if host in SHORTENERS:
        indicators.append("Uses a URL-shortening service, which can hide the final destination."); score += 20
    labels=host.split(".") if host else []
    if len(labels) >= 4:
        indicators.append("Has an unusually high number of subdomain levels."); score += 15
    if "@" in p.netloc:
        indicators.append("Contains @ in the network location, which can be misleading."); score += 35
    if host.startswith("xn--") or any(x.startswith("xn--") for x in labels):
        indicators.append("Contains an internationalized/punycode domain label."); score += 20
    text=(raw+" "+(p.path or "")+" "+(p.query or "")).lower()
    hits=sorted({w for w in SUSPICIOUS_WORDS if w in text})
    if hits:
        indicators.append("Contains potentially sensitive or urgency-related keywords: "+", ".join(hits)+"."); score += min(25, 5*len(hits))
    if len(raw)>180:
        indicators.append("URL is unusually long."); score += 10
    if p.port and p.port not in (80,443):
        indicators.append("Uses a non-standard web port."); score += 10
    if re.search(r"[<>{}\s]", raw):
        indicators.append("Contains unusual characters or whitespace."); score += 20
    score=min(score,100)
    level="Low Risk" if score<25 else ("Suspicious" if score<55 else "High Risk")
    explanation = "No strong indicators were found by this local heuristic scanner." if not indicators else "This heuristic result is not proof of maliciousness; verify the destination independently."
    return {"risk_level":level,"score":score,"indicators":indicators,"explanation":explanation}
