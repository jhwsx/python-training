"""
文件读写
"""

"""
open(file, mode='r', encoding=None) 

- file：文件路径
- mode：文件打开的模式，默认为 'r' 模式
- encoding：指定文本文件的编码方式，默认依赖系统，处理非ASCII文本时，"UTF-8" 通常是首选编码
- 打开指定的文件，返回一个文件对象（迭代器对象）
- 每次迭代会返回该文件中的一行数据
"""

# FileNotFoundError: [Errno 2] No such file or directory: './unexistedfile.wtf'
# filestream = open('./unexistedfile.wtf')
filestream = open('./p01_syntax_error.py')
print(filestream)  # <_io.TextIOWrapper name='./p01_syntax_error.py' mode='r' encoding='cp936'>
print(type(filestream))  # <class '_io.TextIOWrapper'>
# import _io
# _io.TextIOWrapper
# 读取内容方式1：
print(next(filestream), end='')
print(next(filestream), end='')
print(next(filestream), end='')
print(next(filestream), end='')
print(next(filestream), end='')
# print(next(filestream), end='')  # StopIteration

# 读取内容方式2：
filestream.seek(0)
for line in filestream:
    print(line, end='')

# 读取内容方式3：
filestream.seek(0)
"""
file.read(size=-1)

- 从 file 中读取至多 size 个字符并返回
- 如果 size 为负值或 None，则读取至 EOF（End Of File）
"""
print(filestream.read(), end='')
