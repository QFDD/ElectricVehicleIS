import random
from datetime import datetime, timedelta

# 设置服务类型
service_types = ['充电', '换电', '维修']

# 设置生成记录数量
num_records = 100

# 随机生成一个日期
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# 设置日期范围
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# 随机生成描述
descriptions = [
    "Regular maintenance check",
    "Battery replacement",
    "Charging session",
    "Engine checkup",
    "Electrical system repair",
    "Tire replacement",
    "Brake system check"
]

# 生成记录
records = []
for record_id in range(1, num_records + 1):
    vehicle_id = random.randint(1, 1000)
    service_type = random.choice(service_types)
    date = random_date(start_date, end_date).strftime('%Y-%m-%d')
    description = random.choice(descriptions)
    cost = round(random.uniform(50.0, 500.0), 2)
    records.append((record_id, vehicle_id, service_type, date, description, cost))
import csv
# 保存到CSV文件
csv_file = 'service_records.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(['RecordID', 'VehicleID', 'ServiceType', 'Date', 'Description', 'Cost'])
    # 写入数据
    writer.writerows(records)