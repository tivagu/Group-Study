import dataset as ds
import numpy as np
import matplotlib.pyplot as plt
# MODEL của linear regression giả định rằng sẽ là: y = x^2 - 5x + 6 hay lý thuyết là y = w1x1 + w2x2 + b với ký hiệu lần lượt tương ứng
x_linear = np.hstack(ds.linear_dataset_x)
y_linear = np.round(x_linear**2- 5*x_linear + 6 + np.random.randn(699),4)
# MODEL của logistic regression giả định sẽ là: z = w1x1 + w2x2 + b với con số cụ thể sẽ thông qua quá trình "học có giám sát"
x_logistic = np.hstack(ds.logistic_dataset_age)
y_logistic = np.hstack(ds.logistic_dataset_salary)
z_logistic = np.where(y_logistic > np.mean(y_logistic), 1,0)
'''Xin lưu ý rằng: vì logistic có "nhiều hơn 2 ẩn", vì vậy để có cái nhìn tổng quan về phân loại. Yêu cầu mọi người hãy sử dụng phương trình đường thẳng
Nghĩa là: y = w1x1 + b và z sẽ đóng vai là gán nhãn phân loại 2 bên (bên trái tượng trương z = 0 và ngược lại) để dễ hình dung'''
# Code bắt đầu từ đây. Chỉ sử dụng các thư viện có sẵn, pull file "Tuần 2.py" và "dataset.py" để chạy dataset


