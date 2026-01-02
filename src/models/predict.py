from joblib import load
import pandas as pd

def predict_category(model_path: str, X: pd.DataFrame):
    model = load(model_path)
    return model.predict(X)
