import pandas as pd
import os


file_path = '河北地址.csv'  # 请替换为你的文件路径
df = pd.read_csv(file_path)

# 从文件名中提取城市名，并删除"地址"字样
file_name = os.path.basename(file_path)  # 获取文件名（带扩展名）
city_name = file_name.replace('地址', '').split('.')[0]  # 删除"地址"，并去掉文件扩展名

# 添加"city"列，填充提取的城市名
df['city'] = city_name

# 直接覆盖保存原CSV文件
df.to_csv(file_path, index=False)

print(f'原文件已更新，路径为: {file_path}')
