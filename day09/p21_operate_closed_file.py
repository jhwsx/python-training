import os

filestream = open('my.txt', mode='w')
filestream.close()
# filestream.write('hello')  # ValueError: I/O operation on closed file.
# filestream.read()  # ValueError: I/O operation on closed file.

os.remove('my.txt')
