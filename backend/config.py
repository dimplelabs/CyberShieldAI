from pathlib import Path
import os
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
KNOWLEDGE_BASE_PATH = DATA_DIR / "knowledge_base.csv"
DEMO_LOCATIONS_PATH = DATA_DIR / "demo_locations.csv"
APP_NAME = os.getenv("CYBERSHIELD_APP_NAME", "CyberShield AI")
MODEL_NAME = "all-MiniLM-L6-v2"
load_dotenv(ROOT_DIR / ".env")
