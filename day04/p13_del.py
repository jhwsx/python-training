"""
del 关键字
通过解除引用关系，来得到删除数据的目的
"""
lst = [1, 2, 3, 4, 5]
del lst
# print(lst)  # NameError: name 'lst' is not defined
# print(blabla)  # NameError: name 'blabla' is not defined

lst2 = [1, 2, 3, 4, 5]
lst3 = lst2
del lst2
assert lst3 == [1, 2, 3, 4, 5]

lst4 = [1, 2, 3, 4, 5]
del lst4[1]
assert lst4 == [1, 3, 4, 5]

a = 1
lst5 = [a, 2, 3, 4, 5]
del a
assert lst5 == [1, 2, 3, 4, 5]

b = 1
lst6 = [b, 2, 3, 4, 5]
del lst6[0]
assert lst6 == [2, 3, 4, 5]

lst7 = [1, 2, 3, 4, 5]
del lst7[:]
assert lst7 == []

a = [1]
b = [a]
a.insert(0, b)
print(a)
print(b)


