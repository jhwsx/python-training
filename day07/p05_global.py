import inspect


def f1():
    global a  # 把当前作用域的所有 a 声明为全局
    a = 4
    print(f'line {inspect.currentframe().f_lineno}: a = {a}')

    def f2():
        global a  # 把当前作用域的所有 a 声明为全局
        a = 3
        print(f'line {inspect.currentframe().f_lineno}: a = {a}')

    f2()
    print(f'line {inspect.currentframe().f_lineno}: a = {a}')

a = 1
f1()
print(f'line {inspect.currentframe().f_lineno}: a = {a}')
