"""
dict.popitem()
- 从字典中移除最后一个键值对，并返回它们构成的元组(key, value)
"""
d = {'name': 'Tom', 'age': 18}
assert d.popitem() == ('age', 18)
assert d == {'name': 'Tom'}
assert d.popitem() == ('name', 'Tom')
assert d == {}
# d.popitem()  # KeyError: 'popitem(): dictionary is empty'

