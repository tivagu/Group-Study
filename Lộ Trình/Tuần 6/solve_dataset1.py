import ast
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Trích xuất dữ liệu thành numpy
with open('dataset_1.txt', 'r') as f:
    content = f.read()
list_str = content.replace("dataset =", "").strip()
data_list = ast.literal_eval(list_str)
X = np.array(data_list)


K_values = [2, 5, 10]

plt.figure(figsize=(15, 5))
plt.suptitle('Kết quả gom cụm (K-Means) trên dataset 1', fontsize=16)

for i, k in enumerate(K_values):

    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    labels = kmeans.fit_predict(X)
    

    plt.subplot(1, len(K_values), i + 1)
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k')

    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Tâm cụm')
    
    plt.title(f'K = {k}')
    plt.xlabel('Trục X')
    plt.ylabel('Trục Y')
    plt.legend()

# hiển thị
plt.tight_layout()
plt.show()
