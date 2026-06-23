"""
计算函数
"""


def f(x, w, s):
    print(2 * x + 3 * w - s + 1)


print(id(f))
f(2, 3, 1)
print(f)  # 输出函数数据
# f('hello', 'world', 'hi')  # TypeError: unsupported operand type(s) for -: 'str' and 'str'
