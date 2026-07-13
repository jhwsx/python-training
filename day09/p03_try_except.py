def f(a, b):
    try:
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)
        print(a ** b)
    except:
        print("try 语句出异常了")


f(12, 5)
f(12, 0)
f('x', 'y')
