"""
加法和乘法
对于数字适用，
对于字符串使用，
对于列表适用，
对于元组使用，
"""
a = 'hi'
b = 'no'
assert a + b == 'hino'
assert b + a == 'nohi'
# print(a + 3)  # TypeError: can only concatenate str (not "int") to str
assert a * 3 == 'hihihi'
# b * a  # TypeError: can't multiply sequence by non-int of type 'str'

a = [1, 2]
b = [6, 7, 8]
assert a + b == [1, 2, 6, 7, 8]
assert b + a == [6, 7, 8, 1, 2]
assert a * 3 == [1, 2, 1, 2, 1, 2]
# a * b  # TypeError: can't multiply sequence by non-int of type 'list'

a = (1, 2)
b = (6, 7, 8)
assert a + b == (1, 2, 6, 7, 8)
assert b + a == (6, 7, 8, 1, 2)
assert a * 3 == (1, 2, 1, 2, 1, 2)

"""
增强赋值在操作可变数据时会自动以 inplace 的方式来处理，而普通赋值则仍以新建的方式进行处理
"""
# 列表的例子
a = [6, 8]
a_id = id(a)
b = [9, 0, 1]
a = a + b
assert a == [6, 8, 9, 0, 1]
assert id(a) != a_id

a = [6, 8]
a_id = id(a)
b = [9, 0, 1]
a += b
assert a == [6, 8, 9, 0, 1]
assert id(a) == a_id

# 字符串的例子
a = 'hello'
a_id = id(a)
b = 'world'
a = a + b
assert a == 'helloworld'
assert id(a) != a_id

a = 'hello'
a_id = id(a)
b = 'world'
a += b
assert a == 'helloworld'
assert id(a) != a_id

# 元组的例子
a = (6, 8)
a_id = id(a)
b = (9, 0, 1)
a = a + b
assert a == (6, 8, 9, 0, 1)
assert id(a) != a_id

a = (6, 8)
a_id = id(a)
b = (9, 0, 1)
a += b
assert a == (6, 8, 9, 0, 1)
assert id(a) != a_id
