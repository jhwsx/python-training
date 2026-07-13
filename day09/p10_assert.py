try:
    a = 1
    b = 2
    assert a == b, 'a != b'
except AssertionError as e:
    print(e)


try:
    a = 1
    b = 2
    # assert a == b
    if a != b:
        raise AssertionError('a != b')
except AssertionError as e:
    print(e)
print('ending')
