import os

filestream = open('my.txt', mode='w')
try:
    filestream.write('hello')
    filestream.write('world')
    filestream.write('nihao')
finally:
    filestream.close()

os.remove('my.txt')

# 优雅的写法
with open('my.txt', mode='w') as filestream:
    filestream.write('hello')
    filestream.write('world')
    filestream.write('nihao')
os.remove('my.txt')
