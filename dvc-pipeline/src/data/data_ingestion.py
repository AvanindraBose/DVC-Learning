from pathlib import Path
import pandas as pd
from sklearn.datasets import load_iris

def main():
    data = load_iris(as_frame=True)
    df = data.frame
    root = Path(__file__).parent.parent.parent
    path = root / "data" / "raw" / "iris.csv"
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)
    print("Data saved")

if __name__ == "__main__":
    main()