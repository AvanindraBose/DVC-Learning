import pandas as pd
import numpy as np
from pathlib import Path

df = pd.read_csv("https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv")

df = df.iloc[:,3:]

df = df[df['Length of Membership'] > 3]

root_path = Path(__file__).parent.parent
print(root_path)
df.to_csv(root_path/"data"/"customers.csv",index=False)
