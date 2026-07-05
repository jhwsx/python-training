s = 'hello'
s1 = s.replace('o', '')
assert s1 == 'hell'
assert isinstance(s1, str)

lst = list((1, 2, 3))
lst.append(4)
assert lst == [1, 2, 3, 4]
assert isinstance(lst, list)

r = range(10)
print(r)
