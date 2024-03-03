import csv
import requests

# 假定的API Key和文件名
API_KEY = 'ed101415655a4513cfc7616b4e0af202'
INPUT_CSV_FILE = '河北地址.csv'
OUTPUT_CSV_FILE = 'output_with_locations.csv'

def get_location(address, city):
    """根据地址和城市获取位置信息"""
    url = f"https://restapi.amap.com/v3/geocode/geo?key={API_KEY}&address={address}&city={city}&output=JSON"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["geocodes"]:
            return data["geocodes"][0]["location"]
    return None

# 读取CSV文件，并为每个地址获取位置信息
with open(INPUT_CSV_FILE, mode='r', encoding='utf-8') as infile, \
     open(OUTPUT_CSV_FILE, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['location']  # 添加新列名
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        address = row['address']
        city = row.get('city', '')  # 假设city列可能不存在
        location = get_location(address, city)
        if location:
            row['location'] = location
        else:
            row['location'] = "未找到位置"
        writer.writerow(row)

print("完成！带有位置信息的数据已保存到", OUTPUT_CSV_FILE)
