""" 
请用户输入三个不同的整数, 输入时用空格隔开, 利用条件语句判断出这三个整数中的最大值
"""
input_content = input('请输入三个不同的整数（用空格隔开）: ')
str_lst = input_content.split()
int_lst = [int(x) for x in str_lst]
max_value = int_lst[0]
if max_value < int_lst[1]:
    max_value = int_lst[1]
if max_value < int_lst[2]:
    max_value = int_lst[2]
print(max_value)


"""
实现程序：请用户输入一个正整数 n, 程序计算并输出该整数「各位数字之积」与「各位数字之和」的差

示例:
输入: n = 234
输出: 15 

解释:
各位数之积 = 2 * 3 * 4 = 24 
各位数之和 = 2 + 3 + 4 = 9 
结果 = 24 - 9 = 15
"""
num_str = input('请输入一个正整数：')
# 判定是不是正整数
# if not num_str.isdigit() or not int(num_str):
num = int(num_str)
# 计算有多少位数字
digits = 1
num_copy = num
while True:
    num_copy //= 10
    if num_copy == 0:
        break
    digits += 1

# 获取每位数字，存放在列表中
lst = []
num_copy = num
for _ in range(digits):
    lst.append(num_copy % 10)
    num_copy //= 10
lst.reverse()

# 计算各位数字之积，之和
product = 1
summ = 0
for elem in lst:
    product *= elem
    summ += elem

# 计算差
diff = product - summ
print(diff)

"""
已知字典 d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}, 计算键和值中所有数字类型的数据之和

即: 100 + 8.1 + True + 3+4j = (112.1+4j)
"""
d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}
# 把字典的键和值作为元素存放到列表中
lst = []
lst.extend(d.keys())
lst.extend(d.values())

summ = 0
for elem in lst:
    if type(elem) in (int, float, bool, complex):
        summ += elem
print(summ)

summ = 0
num_type = (int, float, bool, complex)
for k, v in d.items():
    if type(k) in num_type:
        summ += k
    if type(v) in num_type:
        summ += v
print(summ)

summ = 0
num_type = (int, float, bool, complex)
for k in d:
    v = d[k]
    if type(k) in num_type:
        summ += k
    if type(v) in num_type:
        summ += v
print(summ)
"""
定义函数实现：
函数传入一个整数列表nums，把该列表中的偶数变成平方值，奇数保持原值。

示例：
输入：nums = [5, 6, 2, 1, 7, 4, 9]
输出：[5, 36, 4, 1, 7, 16, 9]
"""


def transform(v):
    for i in range(len(v)):
        if v[i] % 2 == 0:
            v[i] **= 2


nums = [5, 6, 2, 1, 7, 4, 9]
transform(nums)
print(nums)

"""
定义函数实现: 对于一个任意的正整数, 判断其是否为阿姆斯特朗数。

如果一个n位正整数等于其各位数字的n次方之和, 则称该数为阿姆斯特朗数。 例如1**3 + 5**3 + 3**3 = 153。

比如1000以内的阿姆斯特朗数:  1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""


def is_amstrong(num):
    digits = 1
    copy = num
    while True:
        copy //= 10
        if copy == 0:
            break
        digits += 1

    # 获取每位数字，存放在列表中
    container = []
    num_copy = num
    for _ in range(digits):
        container.append(num_copy % 10)
        num_copy //= 10
    container.reverse()

    # 遍历数字列表，计算是否是阿姆斯特朗数
    ret = 0
    for digit in container:
        ret += digit ** digits
    if ret == num:
        return True
    else:
        return False


for n in range(1, 1000):
    if is_amstrong(n):
        print(n, end=' ')
