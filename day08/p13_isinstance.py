"""
isinstance(object, classinfo)

- object：实例对象
- classinfo：类对象或者由多个类对象构成的元组
- 判定 object 是否为 classinfo 的实例对象或者其子类的实例对象
"""


class A:
    pass


class B(A):
    pass


class C(B):
    pass


c = C()
assert isinstance(c, A)
assert isinstance(c, B)
assert isinstance(c, C)
assert isinstance(c, (A, B, C))
a = A()
assert isinstance(a, A)
assert not isinstance(a, B)
