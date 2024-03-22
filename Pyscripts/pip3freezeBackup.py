import os
import time
import argparse

# 可换成其他文件名作为默认名，同时更换25行达到更换另类程序导出效果
defaultFileName = 'requirements.txt'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default=defaultFileName, nargs=1)
    # parser.add_argument('-f', '--file', type=str, nargs=1)
    return parser.parse_args()


def time_fileName(fileName):
    nowT = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    # 如果args中传入fileName无后缀名，则使用默认文件名的后缀名
    extention = os.path.splitext(fileName)[1]
    if extention == '':
        extention = os.path.splitext(defaultFileName)[1]
        return f'{nowT}-{fileName}{extention}'

    # print(nowT)
    return f'{nowT}-{fileName}'


def backupList(fname):
    file = time_fileName(fname)
    # 可换成其他命令
    if not os.path.exists('./pip3listBackup/'):
        os.mkdir('pip3listBackup')
    os.system(f'pip3 freeze > ./pip3listBackup/{file}')


if __name__ == '__main__':
    args = get_args()
    if args.file != defaultFileName:
        outPut_FileName = args.file[0]
        backupList(outPut_FileName)
    else:
        backupList(args.file)
