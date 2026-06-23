"""
while 判定条件:
    循环体
"""
# 请输出1 到 10 之间的所有整数
num = 1
while num <= 10:
    print(num)
    num += 1

# 请输出1 到 10 之间的所有奇数
num = 1
while num <= 10:
    if num % 2 != 0:
        print(num)
    num += 1

# 请输出1 到 10 之间的所有偶数
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

# 请输出1 到 10 之间的所有偶数的和
total = 0
num = 1
while num <= 10:
    if num % 2 == 0:
        total += num
    num += 1
assert total == 30

# 请输出1 到 10 之间的所有偶数的积
product = 1
num = 1
while num <= 10:
    if num % 2 == 0:
        product *= num
    num += 1
assert product == 3840

# 请输出1 到 20 之间的所有带 4 的整数
lst = list()
num = 1
while num <= 20:
    if '4' in str(num):
        lst.append(num)
    num += 1
assert lst == [4, 14]
