import sqlite3

# 连接数据库
conn = sqlite3.connect('./database.db')
c = conn.cursor()

# 执行查询
c.execute('SELECT * FROM Vehicles')

# 获取并打印所有行
rows = c.fetchall()
for row in rows:
    print(row)

# 关闭连接
conn.close()