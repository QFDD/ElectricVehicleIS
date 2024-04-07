import csv
import sqlite3

database_path = 'database.db'
csv_file_path = 'user_data.csv'
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM sqlite_schema;")
tables = cursor.fetchall()

# 输出查询结果（即所有表名）
print("Tables in the database:")
for table in tables:
    print(table[1])

# 提交事务并关闭连接
conn.commit()
conn.close()

