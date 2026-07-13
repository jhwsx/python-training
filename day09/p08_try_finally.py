def f(a, b):
    try:
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)
        print(a ** b)
    except ZeroDivisionError as e:
        print(f"try 语句出 ZeroDivisionError: {e}")
    except TypeError as e:
        print(f"try 语句出 TypeError: {e}")
    except Exception as e:
        print(f"try 语句出 Exception: {e}")
    else:
        print("try 语句正常执行")
    finally:
        print('finally 语句执行了')


f(12, 0)
f('x', 'y')
f(12, 5)
