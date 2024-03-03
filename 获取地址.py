import os
import csv

def list_folders_and_save_cleaned_names_to_csv(directory_path, output_csv_file):
    folder_names = []
    
    # 遍历指定文件夹下的所有子文件夹
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        if os.path.isdir(full_path):
            # 删除文件夹名称中的 '\' 字符
            cleaned_name = item.replace("\\", "")
            folder_names.append(cleaned_name)
    
    # 将处理后的文件夹名称保存到CSV文件中
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Cleaned Folder Name"])
        for name in folder_names:
            writer.writerow([name])
    
    print(f"Folder names have been written to '{output_csv_file}'.")

# 指定你的文件夹路径和输出CSV文件的路径
directory_path = '/Users/liuyifeng/Desktop/湖北'
output_csv_file = '/Users/liuyifeng/Desktop/湖北/湖北地址.csv'

list_folders_and_save_cleaned_names_to_csv(directory_path, output_csv_file)
