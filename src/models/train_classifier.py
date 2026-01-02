import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

def train(X, y, out_path: str):
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    dump(clf, out_path)
