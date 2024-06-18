import sqlite3
import csv
from faker import Faker
import random

# 初始化 Faker 库
fake = Faker()

# 生成100条未进行的服务记录
pending_service_records = []
service_types = ['充电', '换电', '维修']

for _ in range(100):
    record = {
        "RecordID": _ + 1,
        "VehicleID": random.randint(1, 100),
        "ServiceType": random.choice(service_types),
        "Date": fake.date(),
        "Description": fake.sentence()
    }
    pending_service_records.append(record)

# 将数据写入CSV文件
csv_file = "pending_service_records.csv"
csv_columns = ["RecordID", "VehicleID", "ServiceType", "Date", "Description"]

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for record in pending_service_records:
            writer.writerow(record)
    print(f"CSV file '{csv_file}' created successfully.")
except IOError:
    print("I/O error")

# 显示生成的CSV文件内容
import pandas as pd
df = pd.read_csv(csv_file)
print(df.head())
