import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from pathlib import Path

root_path = Path(__file__).parent.parent
data_path = root_path/"data"/"raw"
data_path.mkdir(parents=True, exist_ok=True)

#url to download datset
url = 'https://raw.githubusercontent.com/campusx-official/toy-datasets/main/student_performance.csv'

#read the dataset
df = pd.read_csv(url)

#split the dataset
train, test = train_test_split(df, test_size=0.2, random_state=42)

train.to_csv(data_path/"train.csv", index=False)
test.to_csv(data_path/"test.csv", index=False)