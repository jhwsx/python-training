"""
set
- 可变，不是序列
- 集合用的少
- 集合用花括号定义，元素是单个的对象
- 集合是无序的(跟定义的顺序是不一样的，但并不是乱序的)
- 集合中不能存在可变的数据，如列表，字典，集合
- 集合是可变的
- 集合会自动去重
"""
s = {456, 3.14, True, 'hello', 3+4j, ('a', 'b')}
print(s)
# s = {[]}  # TypeError: unhashable type: 'list'
# s = {{}}  # TypeError: unhashable type: 'dict'
# s = {{1, 2, 3}}  # TypeError: unhashable type: 'set'

s = {1, 2, 1, 2}
assert s == {1, 2}

"""
空字符串:   ''     str()
空列表:     []     list()
空元组:     ()     tuple()
空字典:     {}     dict()
空集合：     无     set()
"""
s = set()  # 空集合
assert str(s) == 'set()'
string = ''  # 空字符串
assert type(string).__name__ == 'str'
string = str()
assert type(string).__name__ == 'str'
tup = ()
assert type(tup).__name__ == 'tuple'
tup = tuple()
assert type(tup).__name__ == 'tuple'
