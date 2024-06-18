import sqlite3

def create_database():
    # 连接到 SQLite 数据库（如果数据库不存在，则会自动创建）
    conn = sqlite3.connect('instance/cars_database.db')
    cursor = conn.cursor()

    # 创建 marketing_events 表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS marketing_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        budget INTEGER NOT NULL
    )
    ''')

    # 提交更改并关闭连接
    conn.commit()
    conn.close()
    print("Database and table created successfully.")

if __name__ == '__main__':
    create_database()
