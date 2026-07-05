import inspect


def f1():
    a = 4
    print(f'line {inspect.currentframe().f_lineno}: a = {a}')

    def f2():
        nonlocal a  # 把当前作用域的 a 声明为 enclosing 作用域的 a
        a = 3
        print(f'line {inspect.currentframe().f_lineno}: a = {a}')

    f2()
    print(f'line {inspect.currentframe().f_lineno}: a = {a}')

a = 1
f1()
print(f'line {inspect.currentframe().f_lineno}: a = {a}')
