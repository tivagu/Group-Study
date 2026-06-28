import numpy as np

data_tong = []

with open('dataset_2.txt', 'r') as file:
    for line in file:
        if "[]" in line:
            continue 
        clean_1 = line.replace("$IMU", "").replace(";", " ").strip()
        clean_2 = clean_1.split()
        tempt = []
        for index in clean_2:
            chi_tiet = index.split(":")
            if len(chi_tiet) == 2:
                gia_tri = float(chi_tiet[1])
                tempt.append(gia_tri)
        if len(tempt) == 4:
            data_tong.append(tempt)
finaldata = np.array(data_tong)
print("Ma tran:\n")
print(finaldata)
