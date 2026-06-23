"""
查
"""
d = {'name': 'Jack', 'age': 18, 'height': 175}
assert d['name'] == 'Jack'
assert d['age'] == 18
assert d['height'] == 175
# d['weight']  # KeyError: 'weight'

"""
改
"""
d = {'name': 'Jack', 'age': 18, 'height': 175}
d['name'] = 'Tom'
assert d['name'] == 'Tom'
# d[0:1]  # SyntaxError: invalid syntax

"""
增
"""
d = {'name': 'Jack', 'age': 18, 'height': 175}
d['weight'] = 80
assert d == {'name': 'Jack', 'age': 18, 'height': 175, 'weight': 80}

"""
删
"""
d = {'name': 'Jack', 'age': 18, 'height': 175}
del d['name']
assert d == {'age': 18, 'height': 175}
del d['age'], d['height']  # del 多个用逗号隔开
assert d == {}
# del d['weight']  # KeyError: 'weight'

