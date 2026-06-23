"""
比较运算符
判定两个对象值的大小关系
返回布尔值：True 或者 False
== 等于
!= 不等于
> 大于
< 小于
>= 大于或者等于
<= 小于或者等于
"""
a = 456
b = 789
c = 789
assert b == c
assert a != b
assert b > a
assert a < b
assert b >= a
assert a <= b

a = 'hello'
b = 'hi'
assert a < b

a = [1, 2, 3]
b = [1, 2]
assert a > b

a = [1, 2, 3]
b = (1, 2)
# assert a > b  # TypeError: '>' not supported between instances of 'list' and 'tuple'

a = {1, 2, 3}
b = {1, 2}
assert a > b


