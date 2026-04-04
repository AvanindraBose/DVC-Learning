from pathlib import Path
import pandas as pd
import joblib
from sklearn.metrics import r2_score
import json

def adjusted_r2(r2, n, p):
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)

def main():
    root_path = Path(__file__).parent.parent.parent
    data_path = root_path /"data"/"final"

    X_test = pd.read_csv(data_path / "X_test.csv")
    y_test = pd.read_csv(data_path / "y_test.csv")

    model = joblib.load(root_path / "models" / "model.pkl")

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    n = len(y_test)
    p = X_test.shape[1]

    adj_r2 = adjusted_r2(r2, n, p)

    metrics = {
        "r2": r2,
        "adjusted_r2": adj_r2
    }

    metrics_path = root_path/"reports"/"metrics.json"
    metrics_path.parent.mkdir(parents=True, exist_ok=True)

    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)

    print("Metrics saved:", metrics)

if __name__ == "__main__":
    main()