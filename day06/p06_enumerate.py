"""
枚举操作
enumerate 是一个内置类
enumerate(iterable, start=0)

创建一个 enumerate 类型的数据并返回
该数据是一个迭代器对象, 循环的是索引和元素值的元组
start决定索引的起始值
"""
it = enumerate('ABCDE')
print(it)  # <enumerate object at 0x000002E6AE45A140>
print(type(it))  # <class 'enumerate'>
assert next(it) == (0, 'A')
assert next(it) == (1, 'B')
assert next(it) == (2, 'C')
assert next(it) == (3, 'D')
assert next(it) == (4, 'E')
# next(it)  # StopIteration

it = enumerate('ABCDE', start=2)
assert next(it) == (2, 'A')
assert next(it) == (3, 'B')
assert next(it) == (4, 'C')
assert next(it) == (5, 'D')
assert next(it) == (6, 'E')
# next(it)  # StopIteration

lst = ['a', 'hello', 1]
it = enumerate(lst)
for tup in it:
    print(tup[0], tup[1])

lst = ['a', 'hello', 1]
it = enumerate(lst)
for index, ele in it:
    print(index, ele)
