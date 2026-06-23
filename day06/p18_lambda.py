"""
定义匿名函数的语法：
lambda par1, par2, ..., parN: func_body(一个表达式)
调用匿名函数的语法：

"""


# def f():
#     print('hello world')


(lambda: print('hello world'))()

f = lambda: print('hello world')  # PEP 8: E731 do not assign a lambda expression, use a def
f()


# def f(a, b):
#     print(a + b)


(lambda x, y: print(x + y))(4, 5)


def f(a, b):
    return a + b


ret = (lambda x, y: x + y)(4, 5)
assert ret == 9


lst = ['1.txt', '10.xlsx', '3.pdf', '100.py']
lst.sort(key=(lambda file: int(file.split('.')[0])))
assert lst == ['1.txt', '3.pdf', '10.xlsx', '100.py']
