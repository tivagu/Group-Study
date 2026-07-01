import numpy as np

matrix_data = []

with open("Tuan5_1/dataset_1.txt","r") as file:
    header = file.readline() #xóa dòng đầu tiên

    for line in file:
        line = line.strip() 
        parts = line.split(',')

        new_parts = [] 
        for i in range (7):
            new_parts.append(float(parts[i].strip()))
        
        parts[7] = parts[7].replace("[","").replace("]","")
        sub_parts = parts[7].split('|') #tách FAN, ERR, ZONE

        for item in sub_parts:
            item = item.strip()
            if item.startswith("FAN"):
                new_parts.append(float(item.replace("FAN:", "")))

            if item.startswith("ERR"):
                new_parts.append(float(item.replace("ERR:", "")))

            if item.startswith("ZONE"):
                new_parts.append(float(item.replace("ZONE:", "")))
        
        matrix_data.append(new_parts)

numpy_matrix = np.array(matrix_data)
print(numpy_matrix)
