import os
from difflib import SequenceMatcher


def rename_folders(root_folder):
    """遍历文件夹并重命名含有'xxx'的文件夹名"""
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            new_folder_name = folder_name.replace('test.m3u8', '')
            new_folder_path = os.path.join(root_folder, new_folder_name)
            if folder_name != new_folder_name:
                os.rename(folder_path, new_folder_path)
            # rename_folders(new_folder_path)  # 递归处理子文件夹

def delete_empty_folders(root_folder):
    """删除空文件夹"""
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            if not os.listdir(folder_path):  # 检查是否为空文件夹
                # os.rmdir(folder_path)
                print(folder_path)
            # else:
            #     delete_empty_folders(folder_path)  # 递归处理子文件夹


def similar(a, b):
    """计算字符串a和b的相似度"""
    return SequenceMatcher(None, a, b).ratio()


def find_similar_folders(root_folder):
    """找出相似名称的文件夹"""
    all_folders = []
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            all_folders.append(folder_name)

    similar_groups = []
    while all_folders:
        current_group = [all_folders.pop(0)]  # 取出第一个文件夹作为比较基准
        for folder in all_folders[:]:  # 需要拷贝列表以避免修改时影响迭代
            if similar(current_group[0], folder) >= 0.5:  # 如果相似度大于等于50%
                current_group.append(folder)
                all_folders.remove(folder)  # 移除已经匹配的文件夹
        if len(current_group) > 1:  # 只有当组内多于一个成员时才加入结果
            similar_groups.append(current_group)

    return similar_groups


def main():
    root_folder = r'E:\迅雷下载'

    # 删除空文件夹
    delete_empty_folders(root_folder)

    # 替换名称
    rename_folders(root_folder)

    # 找出相似名称的文件夹
    similar_folders = find_similar_folders(root_folder)

    # 输出结果
    print("相似文件夹列表:")
    print(similar_folders)


if __name__ == "__main__":
    main()