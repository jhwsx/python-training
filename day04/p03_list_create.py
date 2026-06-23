"""
list([iterable])
"""
assert list() == []
assert list("hello") == ['h', 'e', 'l', 'l', 'o']
assert list([1, 2, 3]) == [1, 2, 3]
assert list((1, 2, 3)) == [1, 2, 3]
assert list({'one': 1, 'two': 2}) == ['one', 'two']
assert ''.join(list("hello")) == 'hello'
