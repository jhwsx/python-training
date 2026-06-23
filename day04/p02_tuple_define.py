"""
元组

元组只有一个元素，需要写成 element,

"""

tup = (1, 2)
print(tup)

# 封包：当多个对象同时赋值给一个变量时，Python 会自动将这多个对象打包成一个元组
tup = 1, 2
print(tup)

# 只有一个元素的元组
tup = 1,
print(tup)
print(type(tup))

tup = (1,)
print(tup)
