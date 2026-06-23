"""
特殊参数
- 默认情况下，实参的传递形式可以是位置参数或关键字参数
- 可以用 / 和 * 来限制参数的传递形式
- 其中 / 为仅限位置参数，限制在它之前的形参只能接收位置参数
- 其中 * 为仅限关键字参数，限制在它之后的形参只能接收关键字参数
- 这两个特殊参数只是为了限制参数的传递形式，不需要为它们传入实参
"""


def f(a, b, c, d, e):
    pass


f(a=1, b=2, c=3, d=4, e=5)
f(1, b=2, c=3, d=4, e=5)
f(1, 2, c=3, d=4, e=5)
f(1, 2, 3, d=4, e=5)
f(1, 2, 3, 4, e=5)
f(1, 2, 3, 4, 5)


def f(a, b, /, c, d, e):
    pass


# f(a=1, b=2, c=3, d=4, e=5)  # TypeError: f() got some positional-only arguments passed as keyword arguments: 'a, b'
# f(1, b=2, c=3, d=4, e=5)  # TypeError: f() got some positional-only arguments passed as keyword arguments: 'b'
f(1, 2, c=3, d=4, e=5)
f(1, 2, 3, d=4, e=5)
f(1, 2, 3, 4, e=5)
f(1, 2, 3, 4, 5)

def f(a, b, c, *, d, e):
    pass


f(a=1, b=2, c=3, d=4, e=5)
f(1, b=2, c=3, d=4, e=5)
f(1, 2, c=3, d=4, e=5)
f(1, 2, 3, d=4, e=5)
# f(1, 2, 3, 4, e=5)  # TypeError: f() takes 3 positional arguments but 4 positional arguments (and 1 keyword-only argument) were given
# f(1, 2, 3, 4, 5)  # TypeError: f() takes 3 positional arguments but 5 were given


def f(a, b, /, c, *, d, e):
    pass


# f(a=1, b=2, c=3, d=4, e=5)  # TypeError: f() got some positional-only arguments passed as keyword arguments: 'a, b'
# f(1, b=2, c=3, d=4, e=5)  # TypeError: f() got some positional-only arguments passed as keyword arguments: 'b'
f(1, 2, c=3, d=4, e=5)
f(1, 2, 3, d=4, e=5)
# f(1, 2, 3, 4, e=5)  # TypeError: f() takes 3 positional arguments but 4 positional arguments (and 1 keyword-only argument) were given
# f(1, 2, 3, 4, 5)  # TypeError: f() takes 3 positional arguments but 5 were given

# help(sorted)  # sorted(iterable, /, *, key=None, reverse=False)
