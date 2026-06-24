import json
import numpy as np

with open("dataset_1.json","r") as file:
    dataset = json.load(file)

    X = dataset.get("sensor_readings")
    id,temp, accel = [], [], []

    for i in X:
        i: dict # i la kieu dictionary
        id.append(i.get("node_id"))
        if i.get("status") != "ERROR":
            
            temp_before = i.get("temp")
            clean_1 = temp_before.replace("C","") #xiu test lai
            clean_2 = clean_1.strip() #xoa khoang trang 2 ben
            clean_3 = float (clean_2)
            temp.append(clean_3)

            accel.append(i.get("accel"))

X = np.array ([temp, accel])
print(X)