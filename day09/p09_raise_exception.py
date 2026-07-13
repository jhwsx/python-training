"""
raise 语句可以主动的抛出异常
raise 后面可以是异常实例/异常类/没有内容
"""


def div1(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def div2(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def div3(a, b):
    if b == 0:
        raise
    return a / b


div1(12, 0)
div2(12, 0)
div3(12, 0)
