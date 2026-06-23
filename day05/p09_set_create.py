"""
set([iterable])
"""
string = 'hello world'
s = set(string)
print(s)
lst = list([1, 2, 3, 1, 2, 3])
s = set(lst)
assert len(s) == 3
tup = (1, 2, 3, 1, 2, 3)
s = set(tup)
assert len(s) == 3