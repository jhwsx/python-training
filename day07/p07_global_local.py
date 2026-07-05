def outer():
    global a, b
    a, b, c, d = 3, 4, 5, 6
    assert a == 3
    assert b == 4

    def inner():
        global a, b
        nonlocal c, d
        a, b, c, d = 7, 8, 9, 0

    inner()
    assert c == 9
    assert d == 0


a, b = 1, 2
outer()
assert a == 7
assert b == 8
