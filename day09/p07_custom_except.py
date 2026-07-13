class MyZeroDivisionError:

    def __init__(self, msg=''):
        self.__msg = msg

    def __str__(self):
        return f'{self.__msg}'


class MyZeroDivisionError2(Exception):
    pass


e = MyZeroDivisionError()
print(e)
e = MyZeroDivisionError('division by zero')
print(e)
e = MyZeroDivisionError2('division by zero', 'hello', 'world', 'hi')
print(e)

e = ZeroDivisionError('division by zero')
print(e)
