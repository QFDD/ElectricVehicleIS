import sqlite3
from sqlite3 import Error
from names_generator import generate_name
import random
import string
import csv

def generate_random_user(email_counter):
    roles = ['customer', 'sales', 'service']
    name = generate_name(style='capital')
    role = random.choice(roles)
    phone = ''.join(random.choices(string.digits, k=10))
    email = f"{name.lower()}{email_counter}@example.com"
    # 生成随机密码，包括大小写字母、数字、特殊字符
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(password_characters, k=12))
    
    return (name, role, email, phone, password)

email_counter = 1
users = [generate_random_user(email_counter + i) for i in range(1000)]
csv_file_path = 'user_data.csv'
with open(csv_file_path, mode='w', newline='',encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
        # 写入标题行
    writer.writerow(['Name', 'Role', 'Email', 'Phone', 'Password'])
        # 批量写入用户数据
    writer.writerows(users)
