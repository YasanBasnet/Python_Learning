# ==========================================================
# K-MEANS CLUSTERING COMPLETE PIPELINE
# Dataset : Customers_Data.csv
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================================================
# STEP 1 : Read CSV File
# ==========================================================

df = pd.read_csv("Customers_Data.csv")

print("=" * 60)
print("DATASET PREVIEW")
print("=" * 60)
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

# ==========================================================
# STEP 2 : Feature Selection
# ==========================================================

numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

print("\nAll Numeric Columns:")
print(numeric_columns)

# Remove ID column automatically
cluster_features = []

for col in numeric_columns:

    if "id" not in col.lower():
        cluster_features.append(col)

print("\nFeatures Used for Clustering")
print(cluster_features)

X = df[cluster_features]

# Fill missing values
X = X.fillna(X.mean())

# ==========================================================
# STEP 3 : Correlation Matrix
# ==========================================================

print("\nCorrelation Matrix")
print(X.corr())

plt.figure(figsize=(8,6))

plt.imshow(
    X.corr(),
    cmap="coolwarm",
    interpolation="nearest"
)

plt.colorbar()

plt.xticks(
    range(len(cluster_features)),
    cluster_features,
    rotation=45
)

plt.yticks(
    range(len(cluster_features)),
    cluster_features
)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.show()

# ==========================================================
# STEP 4 : Standardization
# ==========================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nData Standardized Successfully")

# ==========================================================
# STEP 5 : Find Optimal K
# ==========================================================

max_k = min(10, len(X_scaled)-1)

wcss = []
silhouette_scores = []

print("\nFinding Optimal K...\n")

for k in range(2, max_k+1):

    model = KMeans(
        n_clusters=k,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    wcss.append(model.inertia_)

    score = silhouette_score(X_scaled, labels)

    silhouette_scores.append(score)

    print(
        f"K={k} | WCSS={model.inertia_:.2f} | Silhouette={score:.4f}"
    )

# ==========================================================
# STEP 6 : Elbow Plot
# ==========================================================

plt.figure(figsize=(8,5))

plt.plot(
    range(2,max_k+1),
    wcss,
    marker='o',
    linewidth=2
)

plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.grid(True)

plt.show()

# ==========================================================
# STEP 7 : Automatic Elbow Detection
# ==========================================================

x = np.arange(2,max_k+1)

y = np.array(wcss)

p1 = np.array([x[0],y[0]])
p2 = np.array([x[-1],y[-1]])

distance = []

for i in range(len(x)):

    p = np.array([x[i],y[i]])

    d = np.abs(
        np.cross(p2-p1,p1-p)
    ) / np.linalg.norm(p2-p1)

    distance.append(d)

elbow_k = x[np.argmax(distance)]

print("\nOptimal K by Elbow Method =", elbow_k)

# ==========================================================
# STEP 8 : Silhouette Plot
# ==========================================================

plt.figure(figsize=(8,5))

plt.plot(
    range(2,max_k+1),
    silhouette_scores,
    marker='o',
    color='green',
    linewidth=2
)

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score")
plt.grid(True)

plt.show()

silhouette_k = np.argmax(silhouette_scores)+2

print("\nOptimal K by Silhouette Score =", silhouette_k)

# ==========================================================
# STEP 9 : Final K Selection
# ==========================================================

if elbow_k == silhouette_k:

    optimal_k = elbow_k

    print("\nBoth methods agree.")

else:

    optimal_k = silhouette_k

    print("\nMethods disagree.")
    print("Using Silhouette Score for better cluster quality.")

print("\nFinal Selected K =", optimal_k)

# ==========================================================
# STEP 10 : Apply KMeans
# ==========================================================

kmeans = KMeans(
    n_clusters=optimal_k,
    init='k-means++',
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

df["Cluster"] = clusters

print("\nCluster Counts")
print(df["Cluster"].value_counts())

# ==========================================================
# STEP 11 : Cluster Centers
# ==========================================================

centers = scaler.inverse_transform(kmeans.cluster_centers_)

print("\nCluster Centers")

center_df = pd.DataFrame(
    centers,
    columns=cluster_features
)

print(center_df)

# ==========================================================
# STEP 12 : Plot Every Pair of Features
# ==========================================================

print("\nGenerating Cluster Plots...")

n = len(cluster_features)

for i in range(n):

    for j in range(i+1,n):

        plt.figure(figsize=(7,6))

        plt.scatter(
            X.iloc[:,i],
            X.iloc[:,j],
            c=clusters,
            cmap='viridis',
            s=60
        )

        plt.scatter(
            centers[:,i],
            centers[:,j],
            color='red',
            marker='X',
            s=250,
            label='Centroids'
        )

        plt.xlabel(cluster_features[i])
        plt.ylabel(cluster_features[j])

        plt.title(
            f"{cluster_features[i]} vs {cluster_features[j]}"
        )

        plt.legend()

        plt.grid(True)

        plt.show()

# ==========================================================
# STEP 13 : Save Clustered Dataset
# ==========================================================

df.to_csv(
    "Customers_Clustered.csv",
    index=False
)

print("\nCustomers_Clustered.csv Saved Successfully")

print("\nProgram Finished Successfully.")