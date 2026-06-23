"""
set.remove(elem)
- 从集合中移除指定元素。如果指定元素不存在，则报错
- 原地操作，没有返回值
"""
s = {1, 2, 3, 4}
s.remove(3)
assert s == {1, 4, 2}
# s.remove(5)  # KeyError: 5

"""
set.discard(elem)
- 从集合中移除指定元素。如果指定元素不存在，则不做任何操作
- 原地操作，没有返回值
"""
s = {1, 2, 3, 4}
s.discard(3)
assert s == {1, 4, 2}
s.discard(5)
