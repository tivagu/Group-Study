import numpy as np
file_path = "dataset_2.txt"
cleaned_data = []
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line.startswith("$IMU"):
            continue
        clean_line = line.strip("$IMU;")
        try:
            # Kết quả: ['ID:01', 'X:0.02', 'Y:-0.05', 'Z:0.98']
            features = clean_line.split(";")
            id_val = float(features[0].split(":")[1])
            x_val  = float(features[1].split(":")[1])
            y_val  = float(features[2].split(":")[1])
            z_val  = float(features[3].split(":")[1])
            feature_vector = [id_val, x_val, y_val, z_val]
            cleaned_data.append(feature_vector)       
        except (IndexError, ValueError) as e:
            print(f"Bỏ qua dòng lỗi cấu trúc toán học: {line}. Chi tiết: {e}")
            continue
matrix_imu = np.array(cleaned_data)
print(matrix_imu)
print(f"\nKích thước ma trận: {matrix_imu.shape}")


# Câu hỏi: Chạy vòng lặp for khác json.load(file) nếu file là dạng JSON như thế nào?
'''json.load(file): đọc file .json, phân tích dấu {} và [] để tạo cấu trúc thành dict và list
Còn for ... in file: chỉ đơn giản là các ký tự, các datasets sẽ biến thành định dạng chuỗi với type là str.'''