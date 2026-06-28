import numpy as np

with open("dataset_2.txt", "r") as file:
    node_ids = []
    x = []
    y = []
    z = []
    
    for line in file:
        line_clean = line.strip() 
        if not line_clean or line_clean == "[]" or not line_clean.startswith("$IMU"):
            continue 
            
        line_data = line_clean.replace("$IMU;", "")
        if line_data.endswith(";"):
            line_data = line_data[:-1] 
            
        parts = line_data.split(";")
        
        if len(parts) >= 4:
            id_part = parts[0].split(":")[1]
            node_ids.append(float(id_part))
            
            x_part = parts[1].split(":")[1]
            x.append(float(x_part))
            
            y_part = parts[2].split(":")[1]
            y.append(float(y_part))
            
            z_part = parts[3].split(":")[1]
            z.append(float(z_part))

X_matrix = np.array([node_ids, x, y, z]).T

print("MA TRAN DAU RA:")
print(X_matrix)
print("\nKich thuoc cua ma tran:", X_matrix.shape)