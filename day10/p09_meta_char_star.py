import re
"""
*
- 对它前面的正则表达式匹配0到任意次重复，尽量多的匹配（贪婪）
* 不可以放最前面，因为 * 需要前面有可以重复的东西

*? 以非贪婪的方式进行匹配，则尽可能少的字符将会被匹配 
"""

p = re.compile(r'ab*')  # * 表示取[0, +∞)个b
m = p.search('a')
assert m.group() == 'a'
m = p.search('ab')
assert m.group() == 'ab'
m = p.search('abb')
assert m.group() == 'abb'
m = p.search('abbbc')
assert m.group() == 'abbb'

p = re.compile(r'a.*')  # * 表示取[0, +∞)个.(.表示匹配除了换行符以外的任意一个字符)
m = p.search('a')
assert m.group() == 'a'
m = p.search('ab')
assert m.group() == 'ab'
m = p.search('abb')
assert m.group() == 'abb'
m = p.search('abbbc')
assert m.group() == 'abbbc'

# 非贪婪模式
p = re.compile(r'ab*?')  # * 表示取[0, +∞)个b
m = p.search('a')
assert m.group() == 'a'
m = p.search('ab')
assert m.group() == 'a'
m = p.search('abb')
assert m.group() == 'a'
m = p.search('abbbc')
assert m.group() == 'a'
