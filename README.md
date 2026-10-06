# CyberShield AI

CyberShield AI is a college-level prototype for women safety and cyber-security awareness. It combines local RAG guidance, explainable heuristic analyzers, complaint preparation, mock location data, a prototype voice architecture, and a local threat-pattern scanner.

## Features
- Women Safety Assistant
- AI Safety Chatbot with local RAG
- Complaint-preparation checklist
- Suspicious URL analyzer
- Suspicious message analyzer
- Nearby Help with clearly labelled DEMO/MOCK data
- Emergency/Voice Prototype architecture
- Safety Resources
- SQL injection, XSS, command-injection and path-traversal pattern scanner

## Architecture
Streamlit UI -> backend services -> local CSV knowledge base / analyzers. The RAG layer uses `all-MiniLM-L6-v2` when SentenceTransformers can load it. If model loading or network access fails, the chatbot gracefully falls back to local keyword retrieval.

## Technologies
Python 3.12, Streamlit, pandas, NumPy, Requests, python-dotenv, SentenceTransformers, Transformers, PyTorch.

## Folder structure
```text
CyberShieldAI/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── backend/
├── frontend/
├── data/
├── utils/
└── tests/
```

## Installation
Python 3.12 is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
streamlit run app.py
```

The first semantic-RAG run may download the `all-MiniLM-L6-v2` model if it is not already cached. Core analyzers and fallback retrieval do not require an API key.

## RAG explanation
`data/knowledge_base.csv` stores trusted, general educational guidance. SentenceTransformers embeds each entry and the user's query; cosine similarity retrieves the most relevant entries. The UI combines those retrieved entries into bounded general guidance. No external LLM API is required.

## Analyzer explanation
The URL and message analyzers are transparent local heuristics. They look for common indicators such as HTTP, raw IP URLs, URL shorteners, urgency, OTP requests, credential requests, financial requests, impersonation and suspicious links. A risk label is a heuristic signal, not proof that content is malicious.

## Testing
```bash
python -m unittest discover -s tests -p "test_*.py"
```
You can also run:
```bash
python -m compileall -q .
```

## Future telephony integration
A production voice service could use a verified telephony/IVR provider, speech-to-text, a safety-policy layer, trusted retrieval, consent controls, human escalation, and audited routing. This project deliberately contains no real phone number and does not place calls.

## Limitations
- No emergency dispatch or real-world reporting.
- Demo locations are fictional.
- No official contacts are invented.
- URL/message results are heuristic.
- RAG content is educational and should be reviewed by qualified staff before real deployment.
- Real deployments need privacy, security, legal, accessibility, monitoring and jurisdiction-specific review.

## College demo instructions
1. Start the app with `streamlit run app.py`.
2. Demonstrate an OTP/phishing question in AI Chatbot.
3. Analyze an HTTP/IP URL.
4. Analyze a message containing an OTP request and link.
5. Generate a complaint checklist.
6. Show the clearly labelled DEMO/MOCK Nearby Help records.
7. Show the PROTOTYPE-only voice architecture.
8. Run the Threat Scanner using a harmless test string containing `<script>`.
