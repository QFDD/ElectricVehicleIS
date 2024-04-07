import csv
import sqlite3
from werkzeug.security import generate_password_hash
def print_table(db_path, table_name):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 执行查询，选择表中的所有数据
    cursor.execute(f"SELECT * FROM {table_name}")
 
    # 获取并打印列名
    column_names = [description[0] for description in cursor.description]
    print(column_names)  # 打印列名作为表头
    
    print(cursor.fetchone())

db_path = 'database.db'  # 请将此路径替换为你的数据库文件路径
table_name = 'Users'  # 请将此替换为你想要打印的表名
print_table(db_path, table_name)