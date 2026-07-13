def f(a, b):
    try:
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)
        print(a ** b)
        [][0]
    except ZeroDivisionError as e:
        print(f"try 语句出 ZeroDivisionError: {e}")
    except TypeError as e:
        print(f"try 语句出 TypeError: {e}")
    except Exception as e:
        print(f"try 语句出 Exception: {e}")

f(12, 0)
f('x', 'y')
f(12, 5)
# object
#     BaseException
#        Exception
#           NameError
#           TypeError
#           SyntaxError
#               TabError
#               IndentionError
#           ValueError
#           AttributeError
#           StopIteration
#           ArithmeticError
#               ZeroDivisionError
#           LookupError
#               KeyError
#               IndexError
