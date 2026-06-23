"""
基本序列赋值
格式：a, b, c, ... = iterable
将 iterable 的元素分别赋值给对应的变量，元素个数和变量个数需要一致
"""
a, b = 3, 4
assert a == 3
assert b == 4

a, b, c = 'abc'
assert a == 'a'
assert b == 'b'
assert c == 'c'

a, b, c = [1, 2, 3]
assert a == 1
assert b == 2
assert c == 3

a, b, c, d = {'name': 'Tom', 'age': 18, 'height': 180, 'weight': 75}
assert a == 'name'
assert b == 'age'
assert c == 'height'
assert d == 'weight'

# a, b, c = 1, 2  # ValueError: not enough values to unpack (expected 3, got 2)
# a, b, c = 1, 2, 3, 4  # ValueError: too many values to unpack (expected 3)
# a, b, c = 1  # TypeError: cannot unpack non-iterable int object
