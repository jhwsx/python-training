"""
计算函数
"""


def f(x, w, s):
    print(2 * x + 3 * w - s + 1)


"""
传位置参数, 实参会根据从左到右的顺序传递给对应的形参
"""
f(2, 3, 1)
f(1, 2, 3)
f(3, 1, 2)

"""
传关键字参数, 实参会根据指定的名称传递给同名的形参, 和位置顺序无关
"""
f(x=1, w=2, s=3)
f(x=1, s=3, w=2)
f(w=2, s=3, x=1)

"""
如果同时使用位置参数和关键字参数，那么所有的关键字参数需要放在
所有的位置参数后面
"""
f(1, w=2, s=3)
f(1, s=3, w=2)
f(1, 2, s=3)
# f(w=2, 1, s=3)  # SyntaxError: positional argument follows keyword argument
# f(1, x=1, w=2, s=3)  # TypeError: f() got multiple values for argument 'x'
# f(1, x=1, w=2)  # TypeError: f() got multiple values for argument 'x'


