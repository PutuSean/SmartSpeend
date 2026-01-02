from pathlib import Path
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_DIR: Path = Path(__file__).resolve().parents[2]
    DATA_DIR: Path = PROJECT_DIR / 'data'
    MODELS_DIR: Path = PROJECT_DIR / 'models'
    LOGS_DIR: Path = PROJECT_DIR / 'logs'

settings = Settings()
