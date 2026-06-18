import dataset as ds
import numpy as np
import matplotlib.pyplot as plt

#DATA
x_linear = np.hstack(ds.linear_dataset_x)
y_linear = np.round(x_linear**2- 5*x_linear + 6 + np.random.randn(699),4)

x1 = x_linear
x2 = x_linear**2

w1 = 0.0
w2 = 0.0
b = 0.0

learning_rate = 0.00000001
epsilon = 1e-4
prev_loss = float ('inf') #vo cung cua float
loss_history = []

while True:
    y_pred = w1*x1 + w2*x2 + b

    #Tinh Loss (MSE)
    loss = (1/(2*len(x_linear))) * np.sum((y_pred - y_linear)**2)
    loss_history.append(loss)

    #Kiem tra dieu kien dung vong lap
    if abs(prev_loss - loss) <= epsilon:
        break
    prev_loss = loss

    #Gradient descent
    error = y_pred - y_linear
    w1 -= learning_rate * (1/len(x_linear)) * np.sum(error * x1)
    w2 -= learning_rate * (1/len(x_linear)) * np.sum(error * x2)
    b -= learning_rate * (1/len(x_linear)) * np.sum(error)

print(f"Kết quả: y = {w1:.4f}x^2 + {w2:.4f}x + {b:.4f}")

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(x_linear, y_linear, s=5, label='Dữ liệu thực tế')
# Vẽ đường cong dự đoán
x_plot = np.sort(x_linear)
y_plot = w1*(x_plot/100)**2 + w2*(x_plot/100) + b
plt.plot(x_plot, y_plot, color='red', label='Dự đoán')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(loss_history)
plt.title("Biểu đồ Loss Function")
plt.xlabel("Số vòng lặp")
plt.show()