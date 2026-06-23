"""
set.update(*iterables)
- 更新集合，添加来自 iterables 中的所有元素
"""
s = {2, 1}
s.update('hello', (1, 2), [3, 4, 5], {'a': 1, 'b': 1})  # 可以传入多个 iterable
print(s)  # {1, 2, 3, 'e', 4, 5, 'b', 'l', 'a', 'h', 'o'}
s.update()   # 也可以不传入任何 iterable
