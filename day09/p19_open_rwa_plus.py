import os

# FileNotFoundError: [Errno 2] No such file or directory: './unexistedfile.wtf'
# filestream = open('./unexistedfile.wtf', mode='r+')

# 创建一个文件
filestream = open('my.txt', mode='w')
filestream.write('hello')
filestream.close()

filestream = open('my.txt', mode='r+')
filestream.write('world')
assert filestream.tell() == 5
filestream.close()

filestream = open('my.txt', mode='w+')
assert filestream.tell() == 0
filestream.write('nihao')
filestream.seek(0)
assert filestream.read() == 'nihao'
filestream.close()

filestream = open('my.txt', mode='a+')
assert filestream.read() == ''
filestream.write('ya')
filestream.seek(0)
assert filestream.read() == 'nihaoya'
filestream.close()

os.remove('my.txt')
