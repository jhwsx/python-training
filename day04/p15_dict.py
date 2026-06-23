"""
字典的元素是以键值对(key: value)的形式存在的, 是一种映射结构
元素之间用逗号隔开
元素被花括号包裹
字典不是序列
    序列的特点：
    有元素 ok
    元素有顺序 ok
    元素有下标（索引） ng
字典是可变的, 可以进行原地操作
字典的键不能存在可变数据, 字典的值没有限制
    元组可以为键
    字符串可以为键
    整数可以为键
    列表不可以为键
    字典不可以为键
字典的键会自动去重（保留第一个重复项），对应的值做更新
当字典作为一个 iterable 进行操作时，只有键参与迭代, 值不参与迭代
"""
d = {'name': 'Jack', 'age': 18, 'height': 175}
print(type(d))
print(d)
assert len(d) == 3
assert d['name'] == 'Jack'

# 字典是可变的, 可以进行原地操作
d['name'] = 'Peter'
assert d['name'] == 'Peter'

# 字典的键不能存在可变数据, 字典的值没有限制
# d = {[]: 'value'}  # TypeError: unhashable type: 'list'
# d = {{}: 'value'}  # TypeError: unhashable type: 'dict'
d = {(): 'value'}
print(d)
d = {"key": "value"}
print(d)
d = {1: 'one'}
print(d)

# 字典的键会自动去重（保留第一个重复项），对应的值做更新
d = {'name': 'peter', 'age': 18, 'height': 1.75, 'weight': 75, 'age': 80, 'age': 19}
assert d == {'name': 'peter', 'age': 19, 'height': 1.75, 'weight': 75}

# 当字典作为一个 iterable 进行操作时，只有键参与迭代, 值不参与迭代
d = {'name': 'Jack', 'age': 18, 'height': 175}
assert '#'.join(d) == 'name#age#height'
lst = list(d)
assert lst == ['name', 'age', 'height']
tup = tuple(d)
assert tup == ('name', 'age', 'height')
lst = [1, 3, 5, 7, 9]
lst[1:3] = d
assert lst == [1, 'name', 'age', 'height', 7, 9]
lst = [1, 3, 5, 7, 9]
lst.extend(d)
assert lst == [1, 3, 5, 7, 9, 'name', 'age', 'height']
lst = sorted(d)
assert lst == ['age', 'height', 'name']
