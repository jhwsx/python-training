"""
实参传递, 传递的是引用关系
"""


def f(b):
    print(id(b))
    print(b)


a = 789
print(id(a))
f(a)

a = 'hello'
print(id(a))
f(a)

a = [1, 2, 3]
print(id(a))
f(a)

