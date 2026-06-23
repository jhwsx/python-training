"""
lst.append(object)
在列表的尾部追加一个元素，原地操作，返回 None
"""

lst = [1, 2, 3]
assert None == lst.append(4)
lst.append(5)
assert lst == [1, 2, 3, 4, 5]

lst = [1, 2, 3]
lst.append('hello')
assert lst == [1, 2, 3, 'hello']

lst = [1, 2, 3]
lst[len(lst):] = ['hello']
assert lst == [1, 2, 3, 'hello']

"""
lst.extend(iterable)
使用 iterable 中的所有元素来扩展列表，等价于 lst[len(lst)] = iterable
"""
lst = [1, 2, 3]
lst.extend([4, 5, 6])
assert lst == [1, 2, 3, 4, 5, 6]
lst = [1, 2, 3]
lst[len(lst):] = [4, 5, 6]
assert lst == [1, 2, 3, 4, 5, 6]
