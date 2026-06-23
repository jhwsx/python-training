"""
list.count(x)

- 返回元素 x 在列表中出现的次数
"""
lst = [7, 3, 7, 2, 2, 7, -10, 9]
assert lst.count(2) == 2
assert lst.count(7) == 3
assert lst.count(100) == 0
