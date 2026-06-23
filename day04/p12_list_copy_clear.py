"""
list.copy()

返回一个该列表的副本，等价于 x = lst[:] (当你把切片放在 = 右边，它才会创建新列表（拷贝）)
"""
lst = [1, 2, 3, 4, 5]
lst2 = lst.copy()
assert lst == lst2
assert id(lst) != id(lst2)

lst3 = lst[:]
assert lst == lst3
assert id(lst) != id(lst3)

"""
list.clear()

删除列表中的所有元素，无返回值，等价于 del lst[:]
原地操作

del 是一个关键字
"""
lst = [1, 2, 3, 4, 5]
lst.clear()
assert lst == []
