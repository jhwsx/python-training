import re
"""
{m,n}
对其之前的正则表达式指定匹配 m 个重复
逗号后面不可以有空格
m 的默认值是 0
n 的默认值是 +∞

{m,n} 的非贪婪模式是 {m,n}?
"""

p = re.compile(r'ab{1,2}')  # {1,2} 表示取 [1,2] 个b
m = p.search('a')
assert m is None
m = p.search('ab')
assert m.group() == 'ab'
m = p.search('abb')
assert m.group() == 'abb'
m = p.search('abbbc')
assert m.group() == 'abb'

p = re.compile(r'a.{1,2}')  # {1,2} 表示取[1,2] 个.(.表示匹配除了换行符以外的任意一个字符)
m = p.search('a')
assert m is None
m = p.search('ab')
assert m.group() == 'ab'
m = p.search('abc')
assert m.group() == 'abc'
m = p.search('abbc')
assert m.group() == 'abb'
m = p.search('abbbc')
assert m.group() == 'abb'

p = re.compile(r'ab{,}')  # 等价于 r'ab*'
m = p.search('a')
assert m.group() == 'a'
m = p.search('ab')
assert m.group() == 'ab'
m = p.search('abb')
assert m.group() == 'abb'
m = p.search('abbbc')
assert m.group() == 'abbb'

# 非贪婪模式
p = re.compile(r'ab{1,2}?')  # {1,2} 表示取 [1,2] 个b
m = p.search('a')
assert m is None
m = p.search('ab')
assert m.group() == 'ab'
m = p.search('abb')
assert m.group() == 'ab'
m = p.search('abbbc')
assert m.group() == 'ab'
