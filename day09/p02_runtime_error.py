print(1 + 1)
print(1 - 1)
print(2 * 3)
# print(2 / 0)  # ZeroDivisionError: division by zero
print(6 / 2)

"""
见过的异常
语法异常：
NameError - 名字不存在
IndentationError: unexpected indent
SyntaxError
运行时异常：
ZeroDivisionError
IndexError
TypeError
ValueError
KeyError
AttributeError
StopIteration
"""
# print(num)  # NameError: name 'num' is not defined
#     print(1)  # IndentationError: unexpected indent

lst = []
# x = lst[100]  # IndexError: list index out of range

# y = 'hello' - 'hi'  # TypeError: unsupported operand type(s) for -: 'str' and 'str'


def f(a, b):
    pass

# f(1)  # TypeError: f() missing 1 required positional argument: 'b'


# print(int("7.89"))  # ValueError: invalid literal for int() with base 10: '7.89'

d = {}
# d.pop('a')  # KeyError: 'a'

z = zip([1, 2], [5, 6])
print(next(z))
print(next(z))
# print(next(z))  # StopIteration
