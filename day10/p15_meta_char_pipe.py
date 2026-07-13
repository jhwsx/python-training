"""
|
任意个正则表达式可以用 | 连接，比如 A|B 表示匹配正则表达式 A 或者 B，
一旦有一个先匹配成功，另外的就不会再进行匹配
"""

import re

p = re.compile(r'd|e|b')
m = p.search('abc')
assert m.group() == 'b'
m = p.search('aebcd')
assert m.group() == 'e'
