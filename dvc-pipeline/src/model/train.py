from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def main():
    root_path = Path(__file__).parent.parent.parent
    path = root_path/"data"/"final"

    X_train = pd.read_csv(path / "X_train.csv")
    y_train = pd.read_csv(path / "y_train.csv")

    model = LinearRegression()
    model.fit(X_train, y_train)

    model_path = root_path / "models" / "model.pkl"
    model_path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, model_path)

    print("Model trained")

if __name__ == "__main__":
    main()