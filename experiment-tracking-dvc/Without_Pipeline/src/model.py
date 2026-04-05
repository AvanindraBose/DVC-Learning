import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from dvclive import Live

root_path = Path(__file__).parent.parent
data_path = root_path/"data"/"student_data.csv"

df = pd.read_csv(data_path)

n_estimators = 100
max_depth = 6
rf = RandomForestClassifier(n_estimators=100,max_depth=6)

X = df.drop(columns=['Placed'])
y = df['Placed']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)

with Live(save_dvc_exp=True) as live:
    live.log_metric("accuracy", accuracy_score(y_test, y_pred))
    live.log_metric("precision", precision_score(y_test, y_pred))
    live.log_metric("recall", recall_score(y_test, y_pred))
    live.log_metric("f1", f1_score(y_test, y_pred))
    live.log_param("n_estimators",n_estimators)
    live.log_param("max_depth",max_depth)