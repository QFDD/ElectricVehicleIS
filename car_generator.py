
import random
import string
import csv
# 生成符合中国车牌标准的车辆ID数据生成器
def generate_vehicle_data(num_vehicles):
    # 定义一些地区代码，仅用于示例
    area_codes = ['京', '沪',"津","渝",'宁' '粤','新',"藏","桂","蒙","辽","吉","黑","冀","晋","苏","浙","皖","闽","赣","鲁","豫","鄂","湘","琼","川","贵","云","陕","甘","青"]

    models = ['Model A', 'Model B', 'Model C', 'Model D']
    vehicles = []

    for _ in range(num_vehicles):
        area_code = random.choice(area_codes)
        license_plate_number = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.digits, k=5))
        license_plate = area_code + license_plate_number
        
        # 随机选择车辆模型
        model = random.choice(models)
        
        # 随机生成VIN码，为了简化，我们这里使用17位随机大写字母和数字
        vin = ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))
        
        # 随机生成购买日期
        purchase_date = f"{random.randint(2015, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        
        # 用户ID占位代码（这里使用一个随机生成的数字）
        owner_id = random.randint(1, 100)  # 假设用户ID在1到100之间

        vehicles.append((license_plate, model, vin, purchase_date, owner_id))

    return vehicles


def write_cars_to_csv(cars, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # 写入标题行
        writer.writerow(['license_plate', 'Model', 'Vin', 'Purchase_date', 'OwnerID'])
        # 批量写入用户数据
        writer.writerows(cars)
csv_file_path = "cars_data.csv"

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    # 读取并打印每一行数据，以便确认
    print(list(reader)[:5])