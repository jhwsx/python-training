"""
dict.pop(key[, default])
- key：键
- default：指定当键不存在时应该返回的值
- 移除 key 所对应的键值对，并返回 key 对应的值；
  如果 key 不在字典中，则返回 default 指定的值，此时如果 default 未指定值，则报错
"""
d = {'name': 'Tom', 'age': 18}
assert d.pop('age') == 18
assert d == {'name': 'Tom'}
# d.pop('height')  # KeyError: 'height'
assert d.pop('height', 180) == 180
assert d == {'name': 'Tom'}
