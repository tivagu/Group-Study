import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("Lộ Trình/Tuần 3/Tuần 3.png")
H,W,C = image.shape
print(H, W, C)
pixels = image.reshape(-1, C)
print(pixels)