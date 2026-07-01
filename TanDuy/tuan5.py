import numpy as np
final_data=[]
with open('dataset_1.txt','r') as file:
    header = file.readline().strip() 
    for line in file:
        clean1 = line.strip()
        if not clean1:
            continue
        parts = clean1.split(',')
        values = [float(x.strip()) for x in parts[0:7]]
        env_raw = parts[7].strip().strip('[]')
        env_parts = env_raw.split('|')
        env_dict = {}
        for item in env_parts:
            if ':' in item:
                key, val = item.split(':')
                env_dict[key.strip()] = int(val.strip())
        fan = env_dict.get('FAN', 0)
        err = env_dict.get('ERR', 0)
        zone = env_dict.get('ZONE', 0)
        row = values + [fan, err, zone]
        final_data.append(row)
matrix = np.array(final_data, dtype=float)
print(matrix)



