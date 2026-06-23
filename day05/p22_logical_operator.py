"""
逻辑运算符
and 布尔与：左边 bool 判定为 False，返回左边；否则返回右边
or 布尔或：左边 bool 判定为 True，返回左边；否则返回右边
not 布尔非：判定为 False，返回 True；判定为 True，返回 False
优先级：not > and > or
短路机制, 为了提高执行效率
"""
a = 8
b = 0
c = 'hello'
d = ()
assert (a and b) == b
assert (a and c) == c
assert (b and a) == b

assert (a or b) == a
assert (a or c) == a
assert (b or a) == a
assert (b or d) == d

assert (not a) == False
assert not d

assert (d and (a / b)) == d
assert (c or (a / b)) == c
assert (c or (a / c)) == c
