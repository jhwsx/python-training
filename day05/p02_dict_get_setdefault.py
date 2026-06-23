"""
dict.get(key, default=None)

- key：键
- default：如果指定的键不存在时，返回该值，默认为 None
- 返回指定的键对应的值，如果 key 不在字典中，则返回 default
"""

d = dict(name='Tom', age=18, weight=180)
assert d.get('height') is None
assert d.get('name') == 'Tom'
assert d.get('height', 175) == 175
assert d == {'name': 'Tom', 'age': 18, 'weight': 180}

"""
dict.setdefault(key, default=None)

- 如果字典存在指定的键，则返回它的值
- 如果不存在，则返回 default 指定的值，并且新增该键值对
"""
d = dict(name='Tom', age=18, weight=180)
assert d.setdefault('name') == 'Tom'
assert d.setdefault('height', 175) == 175
assert d.setdefault('address') is None
assert d == {'name': 'Tom', 'age': 18, 'weight': 180, 'height': 175, 'address': None}

"""
指定的键是存在的，那么 d[key], d.get(key), d.setdefault(key) 是一样的
"""

"""
指定的键是不存在的，那么
d[key] 是报错的
d.get(key, default) 获取到的是默认值
d.setdefault(key, default) 返回的是默认值，并且给原字典增加一个键值对: key=>default
"""