import pandas as pd
from pathlib import Path
from ..config.settings import settings

def load_transactions(path: Path | str = None) -> pd.DataFrame:
    path = path or settings.DATA_DIR / 'processed' / 'transactions_100k.csv'
    return pd.read_csv(path)
