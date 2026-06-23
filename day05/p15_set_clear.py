"""
set.clear()
- 移除集合中的所有元素，无返回值
"""
s = {1, 2, 3, 4}
ret = s.clear()
assert ret is None
assert s == set()
