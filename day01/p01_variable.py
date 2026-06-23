# 变量定义, 先定义后使用
num = 789
print(num)
print(num / 2)
print(num + 2)
print(num - 2)
print(num * 2)

a = num
print(a)

print(id(num))
print(id(a))

a = 123
print(num)
print(a)
print(id(num))
print(id(a))

num = a
print(id(num))
print(id(a))

a = 345
num = 345
print(id(num))
print(id(a))

a = 100000000000000
num = 100000000000000
print(id(num))
print(id(a))

import sys

a = ['hello']
num = ['hello']
print(sys.getrefcount(a))