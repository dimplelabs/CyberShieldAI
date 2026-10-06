import re

RULES=[
("OTP request", r"(?i)\b(?:otp|one[- ]time password|verification code)\b"),
("Credential request", r"(?i)\b(?:password|passcode|pin|login|username)\b"),
("Phishing/link", r"(?i)(https?://|www\.|click\s+(?:here|this)|tap\s+(?:here|this))"),
("Urgency", r"(?i)\b(?:urgent|immediately|act now|within \d+ minutes?|account will be (?:blocked|closed|suspended))\b"),
("Financial request", r"(?i)\b(?:send|transfer|pay|payment|refund|fee|money|upi|bank)\b"),
("Impersonation", r"(?i)\b(?:bank|police|support|customer care|admin|official|manager|friend)\b"),
]
def analyze_message(message:str)->dict:
    text=message or ""
    indicators=[]
    for name,pat in RULES:
        if re.search(pat,text): indicators.append(name)
    score=min(100, len(indicators)*18 + (20 if "OTP request" in indicators else 0))
    level="Low Risk" if score<25 else ("Suspicious" if score<60 else "High Risk")
    next_steps=["Do not share OTPs, passwords, PINs, or verification codes.","Do not click suspicious links.","Verify the sender through an independently found official channel.","Preserve the original message and relevant evidence."]
    if "Financial request" in indicators: next_steps.insert(0,"Pause before sending money and independently verify the request.")
    return {"risk_level":level,"score":score,"indicators":indicators,"explanation":"Local pattern analysis flags common social-engineering signals; it cannot prove intent.","next_steps":next_steps}
