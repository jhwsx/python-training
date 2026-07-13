import re
"""
?
对它前面的正则表达式匹配0到1次， 尽量多的匹配（贪婪）

?? 以非贪婪的方式进行匹配，则尽可能少的字符将会被匹配 
"""

p = re.compile(r'ab?')  # * 表示取[0, 1]个b
m = p.search('a')
assert m.group() == 'a'
m = p.search('ab')
assert m.group() == 'ab'
m = p.search('abb')
assert m.group() == 'ab'
m = p.search('abbbc')
assert m.group() == 'ab'

p = re.compile(r'a.?')  # * 表示取[0, 1] 个.(.表示匹配除了换行符以外的任意一个字符)
m = p.search('a')
assert m.group() == 'a'
m = p.search('ab')
assert m.group() == 'ab'
m = p.search('abb')
assert m.group() == 'ab'
m = p.search('abbbc')
assert m.group() == 'ab'

# 非贪婪模式
p = re.compile(r'ab??')  # * 表示取[0, 1]个b
m = p.search('a')
assert m.group() == 'a'
m = p.search('ab')
assert m.group() == 'a'
m = p.search('abb')
assert m.group() == 'a'
m = p.search('abbbc')
assert m.group() == 'a'
