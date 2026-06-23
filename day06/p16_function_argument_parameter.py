"""
必须参数：对于形参来说的，必须接收一个实参的形参，多了少了都不行
默认参数：对于形参来说的，接收到实参的话，使用实参；否则，使用默认值
        默认参数必须放在必须参数的后面
位置参数：对于实参来说的，按照从左到右的顺序将实参传递给对应的形参
关键字参数：对于实参来说的，按照指定的名称将实参传递给对应的形参，与位置顺序无关
        关键字参数必须放在位置参数的后面
不定长参数
        对于形参来说的，
            *args
            **kwargs
                必须放在所有形参的最后面
"""


def f(a, b, c):
    pass


# f(1)  # TypeError: f() missing 2 required positional arguments: 'b' and 'c'
# f(1, 2)  # TypeError: f() missing 1 required positional argument: 'c'

def f(a, b, c=9, *d, **e):
    assert a == 1
    assert b == 2
    assert c == 3
    assert d == (4, 5)
    assert e == {}


f(1, 2, 3, 4, 5)


def f(a, b, *d, c=9, **e):
    assert a == 1
    assert b == 2
    assert d == (3, 4, 5)
    assert c == 9
    assert e == {}


f(1, 2, 3, 4, 5)


def f(a, *d, b, c=9, **e):
    pass


# f(1, 2, 3, 4, 5)  # TypeError: f() missing 1 required keyword-only argument: 'b'
f(1, 2, 3, 4, b=5)
f(1, 2, 3, 4, b=5, x=6, y=7)
# f(1, 2, 3, 4, b=5, x=6, a=7)  # TypeError: f() got multiple values for argument 'a'
