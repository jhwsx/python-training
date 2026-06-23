"""
获取序列指定索引的元素：seq[index]
   index 超过范围的话，会报错

获取第一个元素 seq[0] / seq[-len(seq)]
获取最后的元素 seq[-1] / seq[len(seq) - 1]
"""
s = 'Welcome'
# s[100]  # IndexError: string index out of range
assert s[0] == 'W'
assert s[-1] == 'e'
assert len(s) == 7
assert s[len(s) - 1] == 'e'
assert s[-len(s)] == 'W'

"""
len(s)
s 可以是个容器，比如：字符串，列表，元组，字典，集合等
返回容器的长度，即容器中的元素的个数
"""
assert len([1, 2, 3]) == 3
assert len((1, 2, 3)) == 3
assert len({1, 2, 3}) == 3
assert len(r'\n') == 2
assert len('\n') == 1

lst = [1, 3.14, 'World', [True, "Hi"]]
assert len(lst) == 4
assert lst[3][1][0] == 'H'
