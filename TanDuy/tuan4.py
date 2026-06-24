import json as j
import numpy as np
with open ("dataset_1.json","r") as file :
    data= j.load(file)
    x= data.get("sensor_readings") 
    id, temp, accel=[],[],[]
    for i in x:
        i: dict 
        id.append(i.get("node_id"))
        if i.get("status")!="ERROR":
            temp_before=i.get("temp")
            clean_1= temp_before.replace("C","")
            clean_2= clean_1.strip()
            clean_3=float(clean_2)
            temp.append(clean_3)
            accel.append(i.get("accel"))
       
x=np.array([temp,accel])
print(x)