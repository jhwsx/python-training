"""
str.replace(old, new, count=-1)
- old: 旧字符串
- new: 新字符串
- count: 要替代的旧字符串的最大次数
- 返回替换后的字符串，不影响原来的字符串(字符串是不可变的，不能原地操作)
"""
s = 'hello world'

new_s = s.replace('o', 'A')
assert new_s == 'hellA wArld'

new_s_2 = s.replace('o', 'A', 1)
assert new_s_2 == 'hellA world'

new_s_3 = s.replace('o', 'ABC')
assert new_s_3 == 'hellABC wABCrld'

# 替换失败，返回的还是源字符串
new_s_4 = s.replace('AAA', 'BBB')
assert new_s_4 == s
assert id(new_s_4) == id(s)

# 删除
new_s_5 = s.replace(' ', '')
assert new_s_5 == "helloworld"

new_s_6 = s.replace('', '+')
assert new_s_6 == "+h+e+l+l+o+ +w+o+r+l+d+"
