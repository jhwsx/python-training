"""
成员运算符
- 判断某个对象是否为指定 iterable 的元素
- 返回值：True，False
in 在其中 object in iterable
not in 不在其中 object not in iterable
"""
string = "hello world"
assert 'he' in string
assert 'f' not in string
lst = [56, 8, [1, 2], True, 'hello']
assert [56, 8] not in lst
assert [1, 2] in lst
assert 'he' not in lst
assert True in lst
