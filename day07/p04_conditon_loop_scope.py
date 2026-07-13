"""
条件语句，循环语句不会引入新的作用域
"""

a = 100

if True:
    a = 300
    assert a == 300

assert a == 300

b = 100

for i in range(3):
    b = i

assert b == 2
