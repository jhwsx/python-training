def f():
    a = 789
    print(id(a))
    return a


b = f()
print(id(b))


def g():
    a = [1, 2, 3]
    print(id(a))
    return a


b = g()
print(id(b))
