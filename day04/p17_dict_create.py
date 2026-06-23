"""
1.直接在空字典里面写键值对
"""
d = {'chinese': 100, 'math': 95, 'english': 100}
print(d)

"""
2.定义一个空字典，往里面添加键值对
"""

d = {}
d['name'] = 'Peter'
d['age'] = 18
d['height'] = 175
assert d == {'name': 'Peter', 'age': 18, 'height': 175}

"""
3.把键值对作为关键字参数传入
dict(**kwargs)

"""
d = dict(name='Peter', age=18, weight=75)
assert d == {'name': 'Peter', 'age': 18, 'weight': 75}

"""
4.用可迭代对象来构建字典
可迭代对象的每个元素要包含两个元素
dict(iterable)
"""
d = dict([('name', 'Tom'), ('age', 28)])
assert d == {'name': 'Tom', 'age': 28}
# d = dict('ABCDEF')  # ValueError: dictionary update sequence element #0 has length 1; 2 is required
d = dict([('A', '1'), 'B2', ['C', '3']])
assert d == {'A': '1', 'B': '2', 'C': '3'}
d = dict(('A1', 'B2', 'C3'))  # 这个不标准
assert d == {'A': '1', 'B': '2', 'C': '3'}

"""
zip(*iterables)
- 返回一个迭代器，在迭代操作时，其中的第 i 个元组包含来自每个可迭代对象的第 i 个元素
- 当所输入可迭代对象中最短的一个被耗尽时，迭代器将停止迭代
- 不带参数时，它将返回一个空迭代器
"""
print(zip)
z = zip('abcd', [1, 2, 3, 4], ('one', 'two', 'three', 'four'))
print(list(z))
print(tuple(z))
z = zip('abcd', [1, 2, 3, 4], ('one', 'two', 'three', 'four'))
assert next(z) == ('a', 1, 'one')
assert next(z) == ('b', 2, 'two')
assert next(z) == ('c', 3, 'three')
assert next(z) == ('d', 4, 'four')
# next(z)  # StopIteration
"""
5.用映射结构来构建字典
dict(mapping)
"""
d = dict(zip(['name', 'age'], ['Tom', 28]))
print(d)
