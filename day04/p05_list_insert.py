"""
lst.insert(index, object)

在指定的位置前插入一个元素，无返回值

index: 要插入元素的位置
object: 要插入的元素

"""
lst = [1, 2, 3]
lst.insert(0, -1)
assert lst == [-1, 1, 2, 3]

lst = [1, 2, 3]
lst.insert(1, -1)
assert lst == [1, -1, 2, 3]

lst = [1, 2, 3]
lst.insert(2, -1)
assert lst == [1, 2, -1, 3]

lst = [1, 2, 3]
lst.insert(3, -1)  # 等价于 append(-1)
assert lst == [1, 2, 3, -1]
