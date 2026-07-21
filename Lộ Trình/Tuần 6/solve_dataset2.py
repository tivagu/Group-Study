import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

image_path = 'dataset_2.png'

if not os.path.exists(image_path):
    print(f"Không tìm thấy file ảnh: {image_path}")
else:
    # Tải ảnh 
    img = plt.imread(image_path)
    
    if img.shape[2] == 4:
        img = img[:, :, :3]
        
    height, width, channels = img.shape
    print(f"Kích thước ảnh ban đầu: {height}x{width} với {channels} kênh màu.")
    
    # Nén ảnh thành 1D shape 
    # Biến ảnh HxWxC thành mảng 2 chiều (H*W, C))
    X = img.reshape(-1, channels)
    K_values = [2, 5, 10, 20]
    

    plt.figure(figsize=(20, 5))
    plt.suptitle('Nén ảnh bằng K-Means', fontsize=16)
    
    plt.subplot(1, len(K_values) + 1, 1)
    plt.imshow(img)
    plt.title('Ảnh Gốc')
    plt.axis('off')
    
    # tạo, chạy hàm KMeans(), fit() và hiển thị ảnh
    for i, k in enumerate(K_values):
        print(f"Đang chạy KMeans với K = {k}...")

        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
        kmeans.fit(X)

        labels = kmeans.labels_
        centers = kmeans.cluster_centers_
        compressed_X = centers[labels]

        compressed_img = compressed_X.reshape(height, width, channels)

        compressed_img = np.clip(compressed_img, 0, 1)
        
        # Dán ảnh (hiển thị ảnh)
        plt.subplot(1, len(K_values) + 1, i + 2)
        plt.imshow(compressed_img)
        plt.title(f'K = {k}')
        plt.axis('off')
        
    plt.tight_layout()
    plt.show()
