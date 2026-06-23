"""
dict.copy()
- 返回该字典的一个副本, 和原字典完全分离开的
"""
d = {'name': 'Tom', 'age': 18}
new_d = d.copy()
assert new_d == d
assert id(new_d) != id(d)
d.pop('name')
assert d == {'age': 18}
assert d != new_d
assert new_d == {'name': 'Tom', 'age': 18}
