"""
元组

元组只有一个元素，需要写成 element,

元组的元素没有类型限制

不可变，序列
"""

tup = (1, 2)
print(tup)

# 封包：当多个对象同时赋值给一个变量时，Python 会自动将这多个对象打包成一个元组
tup = 1, 2
print(tup)

tup = 1,
print(tup)
print(type(tup))

tup = 1, 2, 3, 4
print(tup)
# tup[0] = 5  # TypeError: 'tuple' object does not support item assignment

tup = 1, [True, False], 3, 4
tup[1][0] = False
assert tup == (1, [False, False], 3, 4)

"""
tuple([iterable])
"""
tup = tuple()
assert tup == ()

lst = [1, 2, 3, 4]
tup = tuple(lst)
assert tup == (1, 2, 3, 4)
tup = tuple('hello')
assert tup == ('h', 'e', 'l', 'l', 'o')

"""
tuple.count()
"""
tup = 1, 2, 3, 4, 1
assert tup.count(1) == 2

"""
tuple.size()
"""
tup = 1, 2, 3, 4, 1
assert tup.index(2) == 1
