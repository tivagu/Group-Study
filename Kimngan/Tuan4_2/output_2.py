import numpy as np

matrix_data = []

with open("dataset_2.txt", "r") as file:
    for line in file:
        line = line.strip() # Xoa khoang cach hay xuong dong du thua
        
        if line.startswith("$IMU"):
            parts = line.split(";")
            data_parts = parts[1:5] # Chi lay cac du lieu ID, X, Y, Z
            
            row_values = []
            for items in data_parts:
                value = items.split(":")[1] # Chi lay gia tri
                row_values.append(float(value)) 
                
            matrix_data.append(row_values)
            
X_matrix = np.array(matrix_data)

print("MA TRAN DAU RA:")
print(X_matrix)
print("\nKich thuoc cua ma tran:", X_matrix.shape)