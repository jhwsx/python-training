"""
dict.clear()
- 移除字典中的所有元素，无返回值
"""
d = {'name': 'Tom', 'age': 18}
assert d.clear() is None
assert d == {}

