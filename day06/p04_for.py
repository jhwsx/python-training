"""
for 变量 in 可迭代对象:
    循环体
"""
lst = [672, 3.14, 'hello', (3, 1, 6)]
for e in lst:
    print(e)

string = 'hello'
for e in string:
    print(e)

tup = (1, 2, 3)
for e in tup:
    print(e)

d = {'name': 'Tom', 'age': 18}
for e in d:
    print(e)

s = {'a', '1', 'e'}
for e in s:
    print(e)

d = {'name': 'Tom', 'age': 18}
view_keys = d.keys()
view_values = d.values()
view_items = d.items()
for e in view_keys:
    print(e)
for e in view_values:
    print(e)
for e in view_items:
    print(e)

it = zip('abcde', (1, 2, 3, 4, 5))
for e in it:
    print(e)
