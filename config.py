from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = "dev-key-change-before-deployment"
    DATABASE = str(BASE_DIR / "cars.db")
