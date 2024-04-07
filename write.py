import sqlite3

# 连接数据库
conn = sqlite3.connect('database.db')
c = conn.cursor()

# 执行创建表的 SQL 语句
rows = c.execute('''
    Select * from sqlite_master where type='table';
''').fetchall()
for row in rows:
    print(row[1])

# 提交事务
conn.commit()

# 关闭连接
conn.close()