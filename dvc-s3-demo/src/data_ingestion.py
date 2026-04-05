import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from pathlib import Path

root_path = Path(__file__).parent.parent
data_path = root_path/"data"/"raw"/"student_data.csv"
out_path = root_path/"data"/"processed"/"student_data.csv"
out_path.parent.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(data_path)

# Separating features and target variable
X = df.drop(columns=['Placed'])
y = df['Placed']

# Scaling the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Applying PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# Creating a DataFrame with PCA results
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2', 'PC3'])
df_pca['Placed'] = y.values

df_pca.to_csv(out_path, index=False)