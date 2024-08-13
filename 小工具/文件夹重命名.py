import os

def rename_subfolders(parent_folder):
    subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]
    subfolders.sort()  # 确保文件夹按名称排序

    for index, folder in enumerate(subfolders):
        new_name = os.path.join(parent_folder, str(index + 100000))
        os.rename(folder, new_name)
        print(f"Renamed '{folder}' to '{new_name}'")

# 指定要处理的目录
parent_directory = r'F:\FL-pic2'
rename_subfolders(parent_directory)