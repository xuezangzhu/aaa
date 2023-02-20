
import os

# 列出当前目录下的所有文件，将结果拼成一个字符串返回
def run(**agrs):
    print("[*] in dirlister module.")
    files = os.listdir(".")
    return str(files)