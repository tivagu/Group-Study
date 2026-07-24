import ast
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

with open("Tuan6/dataset_1.txt", "r", encoding="utf-8") as file:
  content = file.read()
  if "=" in content:
    content = content.split("=", 1)[1].strip()
  data_list = ast.literal_eval(content)
X_matrix = np.array(data_list)

print("MA TRẬN ĐẦU RA X_MATRIX:")
print(X_matrix)
print("\nKích thước ma trận (chuẩn N hàng, 2 cột):", X_matrix.shape)

k_values = [2, 5, 10]
plt.figure(figsize=(15, 4.5))

for i, k in enumerate(k_values, 1):
  kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
  labels = kmeans.fit_predict(X_matrix)
  centroids = kmeans.cluster_centers_

  print(f"\n--- Giá trị K = {k} ---")
  print("Tọa độ Centroids:\n", centroids)

  plt.subplot(1, 3, i)
  plt.scatter(
      X_matrix[:, 0],
      X_matrix[:, 1],
      c=labels,
      cmap="tab10",
      s=50,
      alpha=0.8,
      edgecolors="k",
  )
  plt.scatter(
      centroids[:, 0],
      centroids[:, 1],
      c="red",
      marker="X",
      s=200,
      label="Centroids",
  )

  plt.title(f"K-means với K = {k}")
  plt.xlabel("X1")
  plt.ylabel("X2")
  plt.legend()
  plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()