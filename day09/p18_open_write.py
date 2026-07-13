import os

filestream = open('my.txt', mode='w')  # 写模式
# filestream.read()  # io.UnsupportedOperation: not readable

"""
file.write(s)
- 将字符串 s 写入并返回写入的字符数
"""
assert 5 == filestream.write('hello')

filestream.close()

filestream = open('my.txt', mode='a')  # 追加写模式
# filestream.read()  # io.UnsupportedOperation: not readable
filestream.write('world')
filestream.write('mygod')
assert 15 == filestream.tell()
filestream.close()
os.remove('my.txt')
