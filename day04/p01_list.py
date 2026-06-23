"""
列表
特点：可变，是序列
列表用方括号定义，对于元素没有类型限制
"""
lst = []
print(lst)

lst = [1, 2, 3]
print(lst)
assert len(lst) == 3

# 列表对它的元素没有类型限制
lst = [1, 'Hello', 0.15, 3+4j, True, ['a', 'b'], (1, 2), {"one": 1, "two": 2}, {"one", "two", "three"}]
print(lst)

"""
inplace 原地操作
修改列表, 针对一个元素
语法：lst[index] = object
"""
lst = [1, 2, 3]
lst[1] = -5
assert lst == [1, -5, 3]
lst[2] = 'ab'
assert lst == [1, -5, 'ab']

"""
inplace 原地操作
修改列表，针对多个元素
语法：lst[start:end:step] = iterable
start 是左闭的, end 是右开的
"""
lst = [1, 2, 3]
# lst[0:] = 1  # TypeError: can only assign an iterable
# 区间长度等于可迭代对象长度, step 可以大于 1
lst1 = [1, 2, 3, 4, 5]
lst1[1:3] = [1, 2]
assert lst1 == [1, 1, 2, 4, 5]
lst2 = [1, 2, 3, 4, 5]
lst2[1::2] = [-1, -3]
assert lst2 == [1, -1, 3, -3, 5]
lst = [1, 2, 3, 4, 5]
lst[1:3] = (1, 2)
assert lst == [1, 1, 2, 4, 5]
lst = [1, 2, 3, 4, 5]
lst[1:3] = 8, 9  # 封包为元组 (8, 9)
assert lst == [1, 8, 9, 4, 5]
lst = [1, 2, 3, 4, 5]
lst[1:3] = 'ab'
assert lst == [1, 'a', 'b', 4, 5]

# 区间长度不等于可迭代对象长度，step 必须是 1，否则会报错
# 替换其中一部分, 元素变多
lst3 = [1, 2, 3, 4, 5]
lst3[1:2] = [6, 6]
assert lst3 == [1, 6, 6, 3, 4, 5]
# lst3[1:2:2] = [6, 6]  # ValueError: attempt to assign sequence of size 2 to extended slice of size 1
# 替换其中一部分, 元素变少
lst4 = [1, 2, 3, 4, 5]
lst4[1:4] = [6, 6]
assert lst4 == [1, 6, 6, 5]
# 清空
lst5 = [1, 2, 3, 4, 5]
lst5[:] = []
assert lst5 == []
# 完整替换
lst6 = [1, 2, 3, 4, 5]
lst6[:] = [2, 4, 6, 8, 10, 12]
assert lst6 == [2, 4, 6, 8, 10, 12]
# 在最前面插入
lst7 = [1, 2, 3, 4, 5]
lst7[:0] = [0, 0]
assert lst7 == [0, 0, 1, 2, 3, 4, 5]
# 在尾部追加
lst8 = [1, 2, 3, 4, 5]
lst8[len(lst8):] = [6, 6]
assert lst8 == [1, 2, 3, 4, 5, 6, 6]
# 在当中某个位置前插入
lst9 = [1, 2, 3, 4, 5]
lst9[1:1] = [6, 6]
assert lst9 == [1, 6, 6, 2, 3, 4, 5]
