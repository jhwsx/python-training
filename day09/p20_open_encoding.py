import os

filestream = open('my.txt', mode='w+', encoding='UTF-8')
s = '你好世界helloworld'
assert filestream.write(s) == len(s)
filestream.seek(0)
assert filestream.read() == s
filestream.close()

os.remove('my.txt')
