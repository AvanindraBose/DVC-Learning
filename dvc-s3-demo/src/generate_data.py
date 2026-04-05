import pandas as pd
import numpy as np
from pathlib import Path

root_path = Path(__file__).parent.parent
data_path = root_path/"data"/"raw"/"student_data.csv"
data_path.parent.mkdir(parents=True, exist_ok=True)
np.random.seed(42)

n = 100

data = {
    'IQ' : np.random.uniform(80,160,n).round(2),
    'CGPA' : np.random.uniform(5,10,n).round(2),
    '10th_Marks':np.random.uniform(60,100,n).round(2),
    '12th_Marks':np.random.uniform(60,100,n).round(2),
    'Placed': np.random.randint(0,2,n)
}

df = pd.DataFrame(data)

df.to_csv(data_path,index=False)