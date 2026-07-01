import numpy as np

matrix_data = []

with open("dataset_1.txt", "r") as file:
    header = file.readline()
    
    row_values = []
    for line in file:
        line = line.strip()
        
        parts = line.split(",")
        
        # Lấy 5 cột đầu
        gases = [float(x.strip()) for x in parts[0:5]] 
        
        # Xử lí xóa khoảng trắng cột 6,7
        pres_1 = float(parts[5].strip())
        pres_2 = float(parts[6].strip())
       
        # Xử lí tách dữ liệu cột cuối
        clean_3a = parts[7]
        clean_3b = clean_3a.replace("[", "").replace("]", "")
        clean_3 = clean_3b.strip()
        
        items_list = clean_3.split("|")
        
        # Tạo dictionary để xử lý động (đề phòng xáo trộn thứ tự)
        env_dict = {}
        for item in items_list:
            key, value = item.split(":")
            env_dict[key.strip()] = int(value.strip())
            
        fan = env_dict.get("FAN", 0)
        err = env_dict.get("ERR", 0)
        zone = env_dict.get("ZONE", 0)
        
        row_values = gases + [pres_1, pres_2, fan, err, zone]
        matrix_data.append(row_values)
        
numpy_matrix = np.array(matrix_data)
print(numpy_matrix)
print("Kích thước ma trận:", numpy_matrix.shape)
        
    
        
    
         
        
        