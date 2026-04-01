from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = ROOT_DIR / "models"
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_PATH = MODELS_DIR / "model_pipeline.joblib"
THRESHOLD_PATH = MODELS_DIR / "threshold.json"
KMEANS_PATH = MODELS_DIR / "kmeans.joblib"
CLUSTER_METADATA_PATH = MODELS_DIR / "cluster_metadata.csv"
SPOTIFY_CATALOG_PATH = MODELS_DIR / "spotify_catalog.csv"
