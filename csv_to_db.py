import sqlite3
import csv

def create_table_from_csv(database_file, csv_file, table_name):
    # 连接到SQLite数据库
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # 读取CSV文件头部以获取列名
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)

        # 准备插入数据的SQL语句
        insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(['?' for _ in headers])});"
        
        # 逐行插入CSV数据
        for row in reader:
            cursor.execute(insert_query, row)

    # 提交事务并关闭连接
    conn.commit()
    conn.close()
    print(f"Data from {csv_file} has been successfully inserted into {table_name} table in {database_file}.")

# 示例使用
database_file = 'cars_database.db'
csv_file = 'data/pending_service_records.csv'
table_name = 'PendingServiceRecords'

create_table_from_csv(database_file, csv_file, table_name)
