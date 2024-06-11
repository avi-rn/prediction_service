import joblib
from pathlib import Path

MODEL_PATH = Path("model.joblib")

def load_model():
    return joblib.load(MODEL_PATH)
