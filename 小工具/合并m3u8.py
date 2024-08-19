# 需要手动下载ffmpeg  https://www.gyan.dev/ffmpeg/builds/

import os
import subprocess

def find_m3u8_files(directory):
    m3u8_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.m3u8'):
                m3u8_files.append(os.path.join(root, file))
    return m3u8_files

def find_deepest_m3u8(m3u8_files):
    deepest_m3u8 = None
    deepest_level = -1
    for m3u8_file in m3u8_files:
        level = len(m3u8_file.split(os.sep))
        if level > deepest_level:
            deepest_m3u8 = m3u8_file
            deepest_level = level
    return deepest_m3u8

def merge_m3u8_to_mp4(m3u8_file_path, output_file_name):
    # 读取 M3U8 文件
    with open(m3u8_file_path, 'r') as f:
        lines = f.readlines()

    # 创建一个临时文件来存放片段列表
    temp_list_file = 'temp_list.txt'
    with open(temp_list_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if not line.startswith('#'):
                # 假设视频片段与 M3U8 文件在同一目录下
                file_path = os.path.join(os.path.dirname(m3u8_file_path), line.strip())
                normalized_path = os.path.normpath(file_path)
                f.write(f"file '{normalized_path}'\n")

    # 此处需要手动修改
    ffmpeg_exe = r'C:\Users\js\ffmpeg\bin\ffmpeg.exe'
    # 使用 ffmpeg 合并片段
    command = [
        ffmpeg_exe,
        '-f', 'concat',
        '-safe', '0',
        '-i', temp_list_file,
        '-c', 'copy',
        output_file_name
    ]
    subprocess.run(command)

    # 清理临时文件
    os.remove(temp_list_file)





def run_single_merge(path):
    directory = path
    m3u8_files = find_m3u8_files(directory)
    deepest_m3u8_file = find_deepest_m3u8(m3u8_files)
    # 输出文件名为该文件夹的名字
    save_path = r"E:\test"
    output_file_name = os.path.join(save_path,os.path.basename(directory)) + '.mp4'
    # 执行合并操作
    merge_m3u8_to_mp4(deepest_m3u8_file, output_file_name)

if __name__ == '__main__':
    root_folder = r"E:\迅雷下载"
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        run_single_merge(folder_path)