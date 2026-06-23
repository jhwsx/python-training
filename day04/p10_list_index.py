"""
list.index(x[, start[, end]])

- x：要找的值
- start：起始索引，默认为 0
- end：结束索引（开区间），默认为 len(lst)
- 返回从左边开始第一次找到指定值时的正向索引，找不到报错
"""
lst = [7, 3, 7, 2, 2, 7, -10, 9]
assert lst.index(3) == 1
assert lst.index(7) == 0
# lst.index(10)  # ValueError: 10 is not in list
assert lst.index(2, 4) == 4
