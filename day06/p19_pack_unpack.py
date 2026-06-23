"""
解包：
    在赋值过程中的解包
        基本序列赋值
        增强序列赋值
    在传参过程中的解包
        在函数传实参时，*iterable 表示对该 iterable 解包，把它的元素变成位置参数
        在函数传实参时，**dict 表示对该 dict 解包，把它的元素变成关键字参数
"""
# 基本序列赋值
a, b, c = 5, 9, 1
assert a == 5
assert b == 9
assert c == 1

# 增强序列赋值
a, *b, c = 1, 2, 3, 4, 5  # *b 不是贪婪的
assert a == 1
assert b == [2, 3, 4]
assert c == 5


def f(x, y, z):
    assert x == 1
    assert y == 2
    assert z == 3


lst = [1, 2, 3]
# 在函数传实参时，*iterable 表示对该 iterable 解包，把它的元素变成位置参数
f(*lst)

d = {1: 'one', 2: 'two', 3: 'three'}
f(*d)


def f(x, y, z):
    assert x == 'one'
    assert y == 'two'
    assert z == 'three'


# 在函数传实参时，**dict 表示对该 dict 解包，把它的元素变成关键字参数
d = {'x': 'one', 'y': 'two', 'z': 'three'}
f(**d)


def f(*args, **kwargs):  # 不定长参数
    print(args)  # (1, 2, 3)
    print(kwargs)  # {'name': 'Tom', 'age': 18}


lst = [1, 2, 3]
d = {'name': 'Tom', 'age': 18}
f(*lst, **d)  # 解包
f(1, 2, 3, name='Tom', age=18)
