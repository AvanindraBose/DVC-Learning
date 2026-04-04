from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    root_path = Path(__file__).parent.parent.parent
    data_path = root_path / "data/raw/iris.csv"
    df = pd.read_csv(data_path)

    X = df[["sepal length (cm)"]]
    y = df["petal length (cm)"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=42
    )

    out_path = root_path/  "data"/"final"
    out_path.mkdir(parents=True, exist_ok=True)

    X_train.to_csv(out_path / "X_train.csv", index=False)
    X_test.to_csv(out_path / "X_test.csv", index=False)
    y_train.to_csv(out_path / "y_train.csv", index=False)
    y_test.to_csv(out_path / "y_test.csv", index=False)

    print("Preprocessing done")

if __name__ == "__main__":
    main()