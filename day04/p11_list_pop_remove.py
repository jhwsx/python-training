"""
list.remove(x)

- 删除列表中从左到右遇到的第一个 x 元素，无返回值
- 原地操作
- 如果没有这样的元素，则报错
"""
lst = [1, 3, 5, 3, 7, 9]
ret = lst.remove(3)
assert ret is None
assert lst == [1, 5, 3, 7, 9]
lst.remove(3)
assert lst == [1, 5, 7, 9]
# lst.remove(3)  # ValueError: list.remove(x): x not in list

"""
list.pop(i=-1)

- i: 要删除并返回的元素的索引
- 删除列表中指定索引（默认最后一个）的元素并返回该元素
- 原地操作
- 索引超出范围，则报错
"""
lst = [1, 3, 5, 3, 7, 9]
assert lst.pop() == 9
assert lst == [1, 3, 5, 3, 7]
assert lst.pop(1) == 3
assert lst == [1, 5, 3, 7]
lst.pop(100)  # IndexError: pop index out of range
