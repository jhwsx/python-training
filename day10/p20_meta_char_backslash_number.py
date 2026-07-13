"""
  \number

  匹配数字代表的分组里面的内容（每个括号是一个子组，子组从1开始编号），
  number 必须指定为存在的分组
  在 [ 和 ] 字符集内，任何数字转义都被看作是字符
"""

import re

""" \1匹配的内容和第1组一定一样 """
p = re.compile(r"(.+) \1")
m = p.search("ab abc")
assert m.group() == 'ab ab'
m = p.search("5 5")
assert m.group() == '5 5'

""" 两个组匹配的内容不一定一样 """
p = re.compile(r"(.+) (.+)")
m = p.search("ab abc")
assert m.group() == 'ab abc'
m = p.search("5 5")
assert m.group() == '5 5'

p = re.compile(r'(.+)-\1(\d)\2')
lst = p.findall("ab-ab11 bc-ab12 cd-cd33")
assert lst == [('ab', '1'), ('cd', '3')]

p = re.compile(r"(.+) [\1]")
m = p.search("ab \1abc")
assert m.group() == 'ab \x01'

p = re.compile(r"(.+) [\101]")
m = p.search("ab Aabc")
assert m.group() == 'ab A'
