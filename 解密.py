import wave
import os
def decrypt_file():
    try:
        # 获取密钥并进行简单验证（这里只是简单判断是否为数字，可根据需求加强验证）
        while True:
            s = input("请输入密码（只能是数字）:")
            if s.isdigit():
                s = int(s)
                break
            else:
                print("密钥必须为数字，请重新输入")

        # 获取文件路径并进行简单验证（这里只是简单判断文件是否存在）
        while True:
            size = input("请输入要解密的文件路径(用\ 分割，在路径最后加上 \\):")
            if os.path.exists(size):
                break
            else:
                print("文件路径不存在，请重新输入")

        # 获取文件名并进行简单验证（这里只是简单判断是否为合法文件名，可根据需求加强验证）
        while True:
            name = input("请输入文件名称:")
            if len(name) > 0:
                break
            else:
                print("文件名不能为空，请重新输入")

        with wave.open(os.path.join(size, "newandf.wav"), 'rb') as data3:
            new_txt = data3.readframes(-1)
            # 假设文件内容表示一个32位有符号整数，使用4字节转换
            num_bytes = 4
            b = int.from_bytes(new_txt[:num_bytes], byteorder='little', signed=True)
            b -= s
            new_txt = b.to_bytes(num_bytes, byteorder='little', signed=True)

        with open(os.path.join(size, name), 'wb') as f:
            f.write(new_txt)
    except FileNotFoundError:
        print("文件不存在，请检查输入的文件路径和名称")
    except PermissionError:
        print("没有权限操作文件，请检查权限设置")
    except ValueError:
        print("文件内容转换为整数时出错，请检查文件内容格式")
if __name__ == '__main__':
    decrypt_file()