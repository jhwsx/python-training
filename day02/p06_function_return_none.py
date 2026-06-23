"""
计算函数
"""

def f2(x, w, s):
    2 * x + 3 * w - s + 1
    return None  # 这一行是隐藏的


def f3():
    return None

result2 = f2(2, 3, 1)
print(result2)  # 输出 None

result3 = f3()
print(result3)  # 输出 None

a = None  # None 是一个关键字, 是一个数据，表示空
print(a)

# print(a + 1)  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
