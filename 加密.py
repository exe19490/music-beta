import random
import wave
import sys
import os
def encrypt_file():
    try:
        # 获取密码并进行简单验证（这里只是简单判断是否为数字，可根据需求加强验证）
        while True:
            a = input("请输入您希望设置的密码（只能用数字）:")
            if a.isdigit():
                a = int(a)
                break
            else:
                print("密码必须为数字，请重新输入")

        # 获取文件路径并进行简单验证（这里只是简单判断文件是否存在）
        while True:
            size = input("请输入文件的目录(使用\ 和 \\分割):")
            if os.path.exists(size):
                break
            else:
                print("文件路径不存在，请重新输入")

        # 获取文件名并进行简单验证（这里只是简单判断是否为合法文件名，可根据需求加强验证）
        while True:
            names = input("请输入您希望加密的文件名称(请在最后加上文件后缀名）:")
            if len(names) > 0:
                break
            else:
                print("文件名不能为空，请重新输入")

        with open(os.path.join(size, names), 'rb') as data1:
            new_wav2 = data1.read()
            # 假设文件内容表示一个32位有符号整数，使用4字节转换
            num_bytes = 4
            b = int.from_bytes(new_wav2[:num_bytes], byteorder='little', signed=True)
            b += a
            new_wav2 = b.to_bytes(num_bytes, byteorder='little', signed=True)

        with wave.open("newandf.wav", 'wb') as data2:
            data2.setnchannels(2)
            data2.setsampwidth(4)
            data2.setframerate(22050)
            data2.writeframes(new_wav2)
    except FileNotFoundError:
        print("文件不存在，请检查输入的文件路径和名称")
    except PermissionError:
        print("没有权限操作文件，请检查权限设置")
    except ValueError:
        print("文件内容转换为整数时出错，请检查文件内容格式")
if __name__ == '__main__':
    encrypt_file()