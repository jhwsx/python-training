"""
函数会引入新的作用域
"""

a = 789


def f():
    a = 345
    print(a)


f()
print(a)
