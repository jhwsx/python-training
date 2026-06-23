"""
pass 语句
pass 是一个关键字，表示一个空语句，当它被执行时，不做任何操作，通常用作占位语句，
在语法上需要语句但实际上不需要执行任何操作的情况下使用。
"""
def f():
    pass


def g():
    ...


total = 0
for i in range(11):
    if i % 2 != 0:
        pass
    else:
        total += i
assert total == 30

while True:
    pass
