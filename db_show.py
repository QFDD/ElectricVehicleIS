import sqlite3

def get_messages_by_conversation_id(database_file, conversation_id):
    # 连接到SQLite数据库
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # SQL查询，获取指定conversation_id的所有消息
    query = '''
    SELECT sender_id, conversation_id, message_text
    FROM messages
    WHERE conversation_id = ?
    '''
    
    # 执行查询并获取结果
    cursor.execute(query, (conversation_id,))
    rows = cursor.fetchall()

    # 打印结果
    for row in rows:
        print(f"Message ID: {row[0]}, Conversation ID: {row[1]},{row[2]}")

    # 关闭数据库连接
    conn.close()

def fetch_first_10_rows(database_file, table_name):
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # 执行查询获取前10行数据
        query = f"SELECT * FROM {table_name} LIMIT 10;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # 获取列名
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = [info[1] for info in cursor.fetchall()]

        # 打印表的前10行数据
        print(f"First 10 rows of the table '{table_name}':")
        print(columns)
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # 关闭数据库连接
        if conn:
            conn.close()

def list_tables(database_file):
    try:
        # 连接到SQLite数据库
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # 执行查询以获取所有表名init_db
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # 关闭数据库连接
        if conn:
            conn.close()
def get_table_columns(database_file, table_name):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(f'PRAGMA table_info({table_name})')
    columns = [column[1] for column in cursor.fetchall()]
    conn.close()
    return columns
# 数据库文件路径
database_file = 'instance/cars_database.db'
fetch_first_10_rows(database_file, 'Users')