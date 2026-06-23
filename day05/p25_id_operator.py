"""
身份运算符
- 判定两个标识符是不是引用自同一个对象
- 返回值：True，False
is          等价于 id(object1) == id(object2)
is not      等价于 id(object1) != id(object2)
"""
a = 789
b = 789
assert a == b
assert a is b  # python 优化；命令行是没有这样的优化的; 小整数对象池[-5,256] 地址固定，命令行也有

a = [1, 2, 3]
b = [1, 2, 3]
assert a == b
assert a is not b

a = 5
b = 5
assert a == b
assert id(a) == id(b)
print(id(a))

# True False None 地址固定
print(id(True))
print(id(False))
print(id(None))

# 判定某个对象是否是 True，False，None， 用身份运算符
a = True
b = False
c = None
assert a is True
assert b is not True
assert c is None
