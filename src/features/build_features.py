import pandas as pd

def build_user_features(tx: pd.DataFrame) -> pd.DataFrame:
    # group by persona and compute simple aggregates
    agg = tx.groupby('persona_id').agg(
        total_spent=('amount', 'sum'),
        tx_count=('transaction_id', 'count'),
        avg_tx=('amount', 'mean')
    ).reset_index()
    return agg
