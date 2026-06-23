"""
序列的切片操作，语法：seq[start:end:step]
start: 起始索引，闭区间
    如果 start 没有指定，
        步长为正数，默认从最左边开始取数据，相当于为 0 或者 -len(seq)
        步长为负数，默认从最右边开始取数据，相当于为 -1 或者 len(seq)-1
end: 结束索引，开区间
    如果 end 没有指定，
        步长为正数，默认取数据到最右边，相当于为 len(seq)
        步长为负数，默认取数据到最左边，相当于为 -len(seq)-1
step: 步长，默认为 1
    步长为正数，表示从左往右取数据
    步长为负数，表示从右往左取数据

注意：
正向索引和反向索引可以同时使用
第一个冒号总是不可以省略，第二个冒号是可以省略的
切片操作时索引超出范围不会报错
如果start到end的方向和step的方向不一致，则取不到数据，结果为空序列

"""
s = "Welcome to China"

# 对字符串切片
assert s[3:7:1] == 'come'
assert s[3:7] == 'come'
assert s[-5:-2:1] == 'Chi'

assert s[-2:-4:-1] == 'ni'
assert s[2:0:-1] == 'le'

assert s[0:9:4] == 'Wot'

assert s[-1:-9:-4] == 'aC'

assert s[:7] == 'Welcome'
assert s[-5:] == 'China'

assert s[:-6:-1] == 'anihC'
assert s[-10::-1] == 'emocleW'

# 复制
assert s[:] == 'Welcome to China'
assert s[0:len(s):1] == 'Welcome to China'
# 反转
assert s[::-1] == 'anihC ot emocleW'
assert s[-1:-len(s)-1:-1] == 'anihC ot emocleW'

assert s[0:100] == 'Welcome to China'
assert s[:-100:-1] == 'anihC ot emocleW'

assert s[0:100:-1] == ''

# 对列表切片
lst = [1, 2, 3, 4, 5, 6]
assert lst[0:2] == [1, 2]
assert lst[::-1] == [6, 5, 4, 3, 2, 1]
assert lst[::] == [1, 2, 3, 4, 5, 6]

# 对元组切片
t = (1, 2, 3, 4, 5, 6)
assert t[1::2] == (2, 4, 6)
