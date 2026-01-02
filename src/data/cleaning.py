import pandas as pd

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # example cleaning steps
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df
