import os

def delete_hidden_files(directory):
    # 遍历目录
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 如果是文件并且以 . 开头，则删除它
        if os.path.isfile(file_path) and filename.startswith('.'):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

        # 如果是目录，则递归调用此函数
        elif os.path.isdir(file_path):
            delete_hidden_files(file_path)


# 指定要清理的目录
target_directory = r'F:\FL-pic2'
delete_hidden_files(target_directory)