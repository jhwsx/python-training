"""
range 是一个内置类
range([start,] stop[, step])

- 按照 step 生成从 start 到 stop 的整数序列（不可变）
- start：起始值，闭区间，默认为 0
- stop：结束值，开区间
- step：步长，默认为 1

如果只传 start 和 stop，那么 step 默认是 1
如果只传一个参数，会传给 stop，那么 start 默认是 0，step 默认是 1
创建一个 range 类型的数据并返回
该数据是一个等差的整数序列, 如 1 3 5 7 或者 7 5 3 1
该数据是不可变的
"""
r = range(1, 10, 2)
assert type(r).__name__ == 'range'
print(r)  # range(1, 10, 2)
assert len(r) == 5
assert r[0] == 1
assert r[1] == 3
assert r[2] == 5
assert r[3] == 7
assert r[4] == 9
assert r[:2] == range(1, 5, 2)  # 切片不降维
assert r[::2] == range(1, 10, 4)
assert list(r) == [1, 3, 5, 7, 9]
assert tuple(r) == (1, 3, 5, 7, 9)

total = 0
for i in range(11):
    total += i
assert total == 55

lst = ['hello', 'a', True]
for i in range(len(lst)):
    print(lst[i])
