import os
import time

filestream = open('my.txt', mode='w+')
filestream.write('hello')
# 这里加 read 是可以读到的，因为 read 是刷新再读
time.sleep(10)
print('time is up')
filestream.close()

time.sleep(5)
os.remove('my.txt')
