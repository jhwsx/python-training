"""
dict.keys()
- 返回由字典所有键组成的一个新视图
- 返回的对象是视图对象，这意味着当原字典改变时，视图也会相应改变
"""
d = {'name': 'Tom', 'age': 15, 'height': 162}
view_keys = d.keys()
assert type(view_keys).__name__ == 'dict_keys'
assert str(view_keys) == "dict_keys(['name', 'age', 'height'])"
assert list(view_keys) == ['name', 'age', 'height']
d.pop('height')
assert d == {'name': 'Tom', 'age': 15}
assert str(view_keys) == "dict_keys(['name', 'age'])"

"""
dict.values()

- 返回由字典所有值组成的一个新视图
- 返回的对象是视图对象，这意味着当字典改变时，视图也会相应改变
"""
d = {'name': 'Tom', 'age': 15, 'height': 162}
view_values = d.values()
assert type(view_values).__name__ == 'dict_values'
assert str(view_values) == "dict_values(['Tom', 15, 162])"
assert list(view_values) == ['Tom', 15, 162]
d.pop('name')
assert d == {'age': 15, 'height': 162}
assert str(view_values) == "dict_values([15, 162])"

"""
dict.items()

- 返回由字典所有键和值组成的一个新视图
- 返回的对象是视图对象，这意味着当字典改变时，视图也会相应改变
"""
d = {'name': 'Tom', 'age': 15, 'height': 162}
view_items = d.items()
assert type(view_items).__name__ == 'dict_items'
assert str(view_items) == "dict_items([('name', 'Tom'), ('age', 15), ('height', 162)])"
assert list(view_items) == [('name', 'Tom'), ('age', 15), ('height', 162)]
d.pop('age')
assert str(view_items) == "dict_items([('name', 'Tom'), ('height', 162)])"

"""
字典的视图对象
可迭代性
动态性
	随着原字典的改变而改变
"""
