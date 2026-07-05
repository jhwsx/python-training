"""
issubclass(class, classinfo)

- class：类对象
- classinfo：类对象或者由多个类对象构成的元组
- 判定 class 是否为 classinfo 的子类
- 该函数会把自己视作为自己的子类
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


assert issubclass(C, C)
assert not issubclass(C, B)
assert issubclass(C, A)
assert not issubclass(A, C)
assert issubclass(C, (A, B))
