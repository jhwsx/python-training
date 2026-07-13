import re
"""
{m}
对其之前的正则表达式指定匹配 m 个重复

"""

p = re.compile(r'ab{2}')  # {2} 表示取 2 个b
m = p.search('a')
assert m is None
m = p.search('ab')
assert m is None
m = p.search('abb')
assert m.group() == 'abb'
m = p.search('abbbc')
assert m.group() == 'abb'

p = re.compile(r'a.{3}')  # {3} 表示取3 个.(.表示匹配除了换行符以外的任意一个字符)
m = p.search('a')
assert m is None
m = p.search('ab')
assert m is None
m = p.search('abb')
assert m is None
m = p.search('abbc')
assert m.group() == 'abbc'
m = p.search('abbbc')
assert m.group() == 'abbb'
