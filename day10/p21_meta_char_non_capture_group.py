"""
(?:…)

- 非捕获分组，并不创建新的组合，所匹配的子字符串不能在执行匹配后被获取或是之后在模式中被引用
"""
import re


# 非捕获分组的一个作用
# 1.把括起来的内容作为一个整体

p = re.compile('a(?:bc)d(efg)(.+)')
m = p.search('abcdefghijk')
assert m.group() == 'abcdefghijk'
assert m.group(1) == 'efg'
assert m.group(2) == 'hijk'

p = re.compile('a(?:bc)d(?:efg)(.+)')
m = p.search('abcdefghijk')
assert m.group() == 'abcdefghijk'
assert m.group(1) == 'hijk'


p = re.compile('a(?:bc)d(?:efg)(?:.+)')
m = p.search('abcdefghijk')
assert m.group() == 'abcdefghijk'
# m.group(1)  # IndexError: no such group

p = re.compile(r'(ab)+')
# (ab)+ +取3 (ab)(ab)(ab)
# 0组匹配到 'ababab' 1组捕获到 'ab'
lst = p.findall('abababb')
assert lst == ['ab']

p = re.compile(r'(?:ab)+')
# (ab)+ +取3 (?:ab)(?:ab)(?:ab)
# 0组匹配到 'ababab'
lst = p.findall('abababb')
assert lst == ['ababab']

# 提取手机号码的中间四位
p = re.compile(r'\d{3}(\d{4})\d{4}')
phone = '13917130230'
lst = p.findall(phone)
assert lst == ['1713']

