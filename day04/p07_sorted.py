"""
sorted(iterable, [key], reverse=False)

- iterable：要排序的可迭代对象
- key：指定一个函数，在排序之前，每个元素都先应用这个函数之后再排序
- reverse：默认为 False，代表升序，指定为 True 则为降序
- 对可迭代对象进行排序，以列表形式返回排序之后的结果
"""

lst = [3, 2, 7, -10, 9]
new_lst = sorted(lst)
assert lst == [3, 2, 7, -10, 9]
assert new_lst == [-10, 2, 3, 7, 9]

s = 'welcome'
new_lst = sorted(s)
assert s == 'welcome'
assert new_lst == ['c', 'e', 'e', 'l', 'm', 'o', 'w']

s = 'welcome'
new_lst = sorted(s, key=str.upper)
print(new_lst)
