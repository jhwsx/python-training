# string = 'hello world', 如何切片可以输出 'hello w'?
string = 'hello world'
assert string[:7] == 'hello w'

# string = 'hello world', 如何切片(不是索引)可以输出空格字符?
string = 'hello world'
assert string[5:6] == ' '

# string = 'hello world', 如何切片(不是索引)可以输出 'd'?
string = 'hello world'
assert string[-1:-2:-1] == 'd'
assert string[-1:] == 'd'

# string = 'hello world', string[5:-1]的结果是什么?
string = 'hello world'
assert string[5:-1] == ' worl'

# string = 'hello world', string[1:9:2]的结果是什么?
string = 'hello world'
assert string[1:9:2] == 'el o'

# string = 'hello world', string[-2:4:-2]的结果是什么?
string = 'hello world'
assert string[-2:4:-2] == 'lo '

# 给定时间字符串 t = "2025/10/28-14:35:48"，提取月份和分钟数并计算它们的乘积
t = "2025/10/28-14:35:48"
month = int(t[5:7])
minute = int(t[14:16])
assert month == 10
assert minute == 35
assert month * minute == 10 * 35
# 还可以用分隔

# 给定字符串 s = "12a3a4AA5A"，求出'A'字符和'a'字符的数量差
s = "12a3a4AA5A"
bigACnt = s.count('A')
assert bigACnt == 3
smallACnt = s.count('a')
assert smallACnt == 2
assert bigACnt - smallACnt == 1


"""
编写一个程序, 帮助水果店实现计价功能:
请用户输入水果品种, 水果单价(元/kg)和重量(kg),
计算出需要花费的金额并做格式化输出

例:
用户输入水果品种为: 苹果
输入单价为: 3.98
输入重量为: 2.58
根据用户输入数据计算出总价为: 10.2684

请用三种字符串格式化方式输出如下结果:
您购买了2.58kg的苹果, 单价为3.98元/kg, 您需要支付10.27元!
"""
'''
name = input('用户输入水果品种为: ')
price = float(input('输入单价为: '))
weight = float(input('输入重量为: '))
total = price * weight
print('根据用户输入数据计算出总价为: ', total)

# %格式化
print('您购买了%.2fkg的%s, 单价为%.2f元/kg, 您需要支付%.2f元!' % (weight, name, price, total))
# format格式化
print('您购买了{:.2f}kg的{}, 单价为{:.2f}元/kg, 您需要支付{:.2f}元!'.format(weight, name, price, total))
# f-string格式化
print(f'您购买了{weight:.2f}kg的{name}, 单价为{price:.2f}元/kg, 您需要支付{total:.2f}元!')
'''
# 已知 lst = [1, 3, 2, 6, 1, 1, 41], 程序实现: 求lst中最后一个为1的元素的索引
lst = [1, 3, 2, 6, 1, 1, 41]
rlist = lst[::-1]
rindex = rlist.index(1)
assert len(lst) - 1 - rindex == 5
assert -rindex - 1 == -2

"""
编写程序实现: 请用户输入用逗号隔开的一串数字, 输出转化成元组后的数据

例:
用户输入:  1,2,3,45,678
程序输出:  ('1', '2', '3', '45', '678')
"""
'''
string = input('用户输入: ')
lst = string.split(',')
assert lst == ['1', '2', '3', '45', '678']
assert tuple(lst) == ('1', '2', '3', '45', '678')
'''






