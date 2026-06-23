"""
all(iterable)
- 如果 iterable 中的所有元素 bool 判定都为 True，则返回 True
any(iterable)
- 如果 iterable 中存在至少一个元素 bool 判定为 True，则返回 True
"""
tup = (1, True, 'hello', 3 + 4j, {1, 2, 3}, [1, 2])
assert all(tup)
assert any(tup)
tup = (1, False, 'hello', 3 + 4j, {1, 2, 3}, [1, 2])
assert not all(tup)
assert any(tup)

tup = ('', 0, 0.0, None, 0j, set(), {}, [], ())
assert not any(tup)

