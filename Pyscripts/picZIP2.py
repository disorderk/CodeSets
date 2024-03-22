# encoding = utf-8
# import argparse
import os
import sys


def fileMix():
    command = 'pause'
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    if os.path.exists(file1) and os.path.exists(file2):
        file1_extension = os.path.splitext(file1)[1]
        file2_extension = os.path.splitext(file2)[1]
        print('file1 path = ', file1)
        print('file1Extension=', file1_extension)
        print('file2 path = ', file2)
        print('file2Extension=', file2_extension)
        pic_extension = ['.png', '.jpg', '.gif', '.bmp', '.jpeg']
        zip_extension = ['.zip', '.rar', '.7z']
        file1E = 'str'
        file2E = 'str'
        file1name = os.path.basename(file1)
        file2name = os.path.basename(file2)
        print('file1name=', file1name)
        print('file2name=', file2name)
        indexZ = 0
        for ze in zip_extension:
            # indexZ = 0
            if file1E != 'zip' and file2E != 'zip' and file2_extension == ze:
                file2E = 'zip'
                indexZ += 1
            elif file1E != 'zip' and file2E != 'zip' and file1_extension == ze:
                file1E = 'zip'
                indexZ += 1
            elif ze == zip_extension[-1] and file1E == 'str' and file2E == 'str':
                errorZ = "This is no Zip!ALL!"
                print(errorZ)
                os.system('pause')
                exit()

            # elif ze == zip_extention[-1]:
            # elif indexZ >= len(zip_extension):
            #     error = "This is no Zip!ALL!"
            #     print(error)
                # print("This is no Zip!ALL!")
                # exit(1)
            else:
                indexZ += 1
            # else:
            #     print("This is no Zip!")
        indexP = 0
        for pe in pic_extension:
            # indexP = 0
            # if file2E != 'zip' and file2_extension == pe:
            if file1E != 'pic' and file2E != 'pic' and file2_extension == pe:
                file2E = 'pic'
                indexP += 1
            # elif file1E != 'zip' and file1_extension == pe:
            elif file1E != 'pic' and file2E != 'pic' and file1_extension == pe:
                file1E = 'pic'
                indexP += 1
            elif pe == pic_extension[-1] and file1E == 'str' or file2E == 'str':
                errorP = "This is no Pic!ALL!"
                print(errorP)
                os.system('pause')
                exit()

            # elif pe == zip_extension[-1]:
            # elif indexP >= len(pic_extension):
            #     error = "This is no Pic!ALL!"
            #     print(error)
                # print("This is no Pic!ALL!")
            else:
                indexP += 1
            # else:
            #     print("This is no Pic!")

        if file1E == 'zip' and file2E == 'pic':
            command = f"copy /b \"{file2}\"+\"{file1}\" \"./{file2name}-output{file2_extension}\""
            file2path = os.path.split(file2)[0]
            os.system(f"explorer {file2path}")
        elif file1E == 'pic' and file2E == 'zip':
            command = f"copy /b \"{file1}\"+\"{file2}\" \"./{file1name}-output{file1_extension}\""
            file1path = os.path.split(file1)[0]
            os.system(f"explorer {file1path}")
        else:
            print(f'''file1的后缀是{file1_extension},file2的后缀是{file2_extension}。file1E为{file1E}，file2E为{file2E}''')
            print("生成command的时候发生异常！")
        os.system(command)
        os.system('pause')
    else:
        print("file not exists!")


if __name__ == "__main__":
    fileMix()
