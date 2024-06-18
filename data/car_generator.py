import sqlite3
import random
import datetime

# 数据库连接
conn = sqlite3.connect('instance/cars_database.db')
cursor = conn.cursor()

# 创建cars表
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cars (
    VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
    OwnerID INTEGER,
    Model TEXT,
    LicensePlate TEXT UNIQUE,
    VIN TEXT,
    PurchaseDate TEXT,
    FOREIGN KEY (OwnerID) REFERENCES Users(ID)
)
''')

# 读取users表中角色为customer的数据行
cursor.execute("SELECT ID FROM Users WHERE Role = 'customer'")
customers = cursor.fetchall()

# 生成车数据
models = ['Model A', 'Model B', 'Model C', 'Model D']

def generate_license_plate():
    return f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(1000, 9999)}"

def generate_vin():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=17))

def generate_purchase_date():
    start_date = datetime.date(2015, 1, 1)
    end_date = datetime.date.today()
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.isoformat()

# 插入车数据
for customer in customers:
    owner_id = customer[0]
    model = random.choice(models)
    license_plate = generate_license_plate()
    vin = generate_vin()
    purchase_date = generate_purchase_date()
    
    cursor.execute('''
    INSERT INTO Cars (OwnerID, Model, LicensePlate, VIN, PurchaseDate)
    VALUES (?, ?, ?, ?, ?)
    ''', (owner_id, model, license_plate, vin, purchase_date))

# 提交事务
conn.commit()

# 关闭数据库连接
conn.close()

print("车数据已成功生成并写入数据库")
