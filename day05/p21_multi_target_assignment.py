"""
多目标赋值
- 将一个对象同时赋值给多个变量
"""
a = b = c = 199
assert id(a) == id(b)
assert id(b) == id(c)
a += 1
assert b == 199
assert c == 199

a = b = c = [1, 2, 3]
assert id(a) == id(b)
assert id(b) == id(c)
a.append(4)
# 副作用
assert b == [1, 2, 3, 4]
assert c == [1, 2, 3, 4]
