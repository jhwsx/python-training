"""
Python 有 6 种标准数据
数字(Number), 特点：不可变，不是序列
    整数 int
    浮点数 float
    布尔值 bool True和False
    复数 complex: 实部+虚部，表示为 a + bj 或者 a + bJ
字符串(String), 特点：可变，是序列
    单行字符串
    多行字符串
"""
i = 789
print(i)
i = -789
print(i)
i = 0
print(i)

f = 7.89
print(f)

f = -7.89
print(f)

f = 0.0
print(f)

f = 0.23
print(f)

f = .23
print(f)

f = 5.
print(f)

# 科学计数法
e = 1e7
print(e)

e = 1E8
print(e)

b = True
print(b)

b = False
print(b)

c = 3 + 4j
print(c)

c = 4 + 5J
print(c)

c = 6j
print(c)

c = 2 + 1j  # 1 不可以省略
print(c)

d = True + True
print(d)
