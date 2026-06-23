"""
函数的特点：
1. 函数是否有返回值，取决于关键字 return
2. return 后面可以跟一个对象，多个对象，甚至不跟
3. return 后面不跟任何对象，相当于 return None
4. 函数执行如果没有返回，等价于return None
5.
"""


def root(number, n):
    return number ** (1 / n)


assert abs(root(16, 2) - 4.0) < 0.000001
assert abs(root(8, 3) - 2.0) < 0.000001
assert abs(root(64, 3) - 4.0) < 0.000001
print(root)  # <function root at 0x0000022281FDC280> 非内置函数，展示地址
print(abs)  # <built-in function abs> 内置函数展示名字, 没有地址


def div(a, b):
    res1 = a / b
    res2 = a // b
    return res1, res2


assert div(12, 5) == (2.4, 2)


def get_my_print():
    return print


print(get_my_print())
get_my_print()('hello world')


