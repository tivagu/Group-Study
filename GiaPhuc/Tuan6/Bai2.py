import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

image_path = "Tuan6/dataset_2.png"  
img = plt.imread(image_path)

H, W, C = img.shape
print(f"Kích thước ảnh gốc: {H}x{W} với {C} kênh màu.")

if C == 4:
  img = img[:, :, :3]
  C = 3

if img.max() > 1.0:
  img = img / 255.0

X_pixels = img.reshape(-1, 3)

k_values = [2, 5, 10, 20]

plt.figure(figsize=(16, 8))


plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title("Ảnh gốc")
plt.axis("off")

for i, k in enumerate(k_values, 2):
  print(f"Đang xử lý nén ảnh với K = {k}...")

  kmeans = KMeans(n_clusters=k, random_state=42, n_init=5)
  kmeans.fit(X_pixels)

  
  centroids = kmeans.cluster_centers_
  labels = kmeans.labels_

  compressed_pixels = centroids[labels]

  compressed_img = compressed_pixels.reshape(H, W, C)

  compressed_img = np.clip(compressed_img, 0, 1)

  plt.subplot(2, 3, i)
  plt.imshow(compressed_img)
  plt.title(f"Ảnh nén (K = {k})")
  plt.axis("off")

plt.tight_layout()
plt.show()