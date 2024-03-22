import argparse
import os
# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser()

# 添加位置参数，指定接收文件路径
parser.add_argument('-f1', '--file1', metavar='', type=argparse.FileType('r', encoding='UTF-8'), help='path to the file1')
parser.add_argument('-f2', '--file2', metavar='', help='path to the file2')
parser.add_argument('file3', type=argparse.FileType('r', encoding='UTF-8'), help='path to the file3')

# 解析命令行参数
args = parser.parse_args()

# 打印拖放的文件路径
print(f"Dragged File1 Path: {args.file1}")
print(f"file1 type:{type(args.file1)}")
print(f"Dragged File2 Path: {args.file2}")
print(f"file2 type:{type(args.file2)}")
os.system("pause")
