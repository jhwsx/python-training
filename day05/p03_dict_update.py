"""
dict.update([other])
- 用 other 来更新原字典, 没有返回值
- other 可以像 dict 的构造那样传参
"""
d = {'name': 'Tom'}
# update(**kwargs)
d.update(age=18)
assert d == {'name': 'Tom', 'age': 18}
# update(iterable)
d.update([('height', 180)])
assert d == {'name': 'Tom', 'age': 18, 'height': 180}
# update(mapping)
d.update(zip(['address'], ['China']))
d.update({'weight': 75})
assert d == {'name': 'Tom', 'age': 18, 'height': 180, 'address': 'China', 'weight': 75}
