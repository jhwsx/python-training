"""
推导式
"""
"""
列表推导式
- 格式：[exp for子句]
- 格式：[exp for子句 更多的for子句或者if子句]
"""
lst = [i ** 2 for i in range(1, 11)]
assert lst == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lst = [(i, i + 1) for i in range(1, 5)]
assert lst == [(1, 2), (2, 3), (3, 4), (4, 5)]
lst = [i for i in range(1, 11) if i % 2 == 0]
assert lst == [2, 4, 6, 8, 10]
# 类比
lst = []
for i in range(1, 11):
    if i % 2 == 0:
        lst.append(i)
assert lst == [2, 4, 6, 8, 10]

"""
字典推导式
- 格式：{k: v for子句}
- 格式：{k: v for子句 更多的for子句或者if子句}
"""
d = {k: v for (k, v) in (['name', 'Tom'], ['age', 18])}
assert d == {'name': 'Tom', 'age': 18}

"""
集合推导式
- 格式：{exp for子句}
- 格式：{exp for子句 更多的for子句或者if子句}
"""
s = {i for i in range(10)}
assert s == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
