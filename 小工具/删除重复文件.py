import os
import hashlib
from datetime import datetime
import shutil
import xxhash

def get_file_hash(filename):
    """获取文件的MD5哈希值"""
    with open(filename, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

def calculate_xxhash(file_path, block_size=65536):
    """计算文件的 xxHash 值"""
    hash_xx = xxhash.xxh64()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(block_size), b""):
            hash_xx.update(chunk)
    return hash_xx.hexdigest()

def remove_duplicates(directory):
    """删除目录中的重复文件"""
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # file_hash = calculate_xxhash(file_path)
            file_hash = get_file_hash(file_path)
            if file_hash not in hashes:
                hashes[file_hash] = (file_path, datetime.fromtimestamp(os.path.getctime(file_path)))
            else:
                existing_path, existing_ctime = hashes[file_hash]
                current_ctime = datetime.fromtimestamp(os.path.getctime(file_path))
                if current_ctime > existing_ctime:
                    # os.remove(file_path)
                    print(f"Removed duplicate: {file_path}")
                else:
                    # os.remove(existing_path)
                    hashes[file_hash] = (file_path, current_ctime)
                    print(f"Removed duplicate: {existing_path}")


def sort_and_rename_files(directory):
    """按创建时间排序并重新命名文件"""
    for root, dirs, files in os.walk(directory):
        # 获取所有文件的创建时间和路径
        files_with_ctime = [(os.path.join(root, f), datetime.fromtimestamp(os.path.getctime(os.path.join(root, f)))) for
                            f in files]
        # 按创建时间排序
        files_with_ctime.sort(key=lambda x: x[1])

        # 重新命名文件
        for index, (file_path, ctime) in enumerate(files_with_ctime):
            ext = os.path.splitext(file_path)[1]
            new_filename = f"{index}{ext}"
            new_filepath = os.path.join(root, new_filename)
            shutil.move(file_path, new_filepath)
            print(f"Renamed '{file_path}' to '{new_filepath}'")


target_directory = r'E:\telegrame_download'
remove_duplicates(target_directory)

# 按创建时间排序并重新命名文件
# sort_and_rename_files(target_directory)