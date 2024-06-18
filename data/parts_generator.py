import pandas as pd
import random

# 定义车的模型
vehicle_models = ['Model A', 'Model B', 'Model C', 'Model D']

# 定义零配件名称的列表（不包括模型）
part_names = [
    'Brake Pad', 'Oil Filter', 'Air Filter', 'Spark Plug', 'Battery', 
    'Headlight Bulb', 'Windshield Wiper', 'Fuel Pump', 'Alternator', 'Radiator'
]

# 生成零配件数据
parts_data = []
part_id = 1

for model in vehicle_models:
    for name in part_names:
        part = {
            'PartID': part_id,
            'Name': f"{name} for {model}",
            'VehicleModel': model,
            'StockQuantity': random.randint(1, 100)
        }
        parts_data.append(part)
        part_id += 1

# 将数据转换为DataFrame
df_parts = pd.DataFrame(parts_data)

# 输出为CSV文件
df_parts.to_csv('parts_data.csv', index=False)

# 打印生成的数据
print(df_parts.head())
