import re

"""
.

- 匹配除了换行符以外的任意一个字符
- DOTALL 模式下，它将匹配包括换行符的任意一个字符
"""

p = re.compile(r'ab.c')
lst = p.findall('ab8c ab-c ab.c ab\nc ab\tc ab+6c')
assert lst == ['ab8c', 'ab-c', 'ab.c', 'ab\tc']

"""
编译模式
re.S    /     re.DOTALL
- 使 ` . ` 匹配包括换行在内的所有字符，没有设置时 ` . ` 是不能匹配换行符的
"""

p = re.compile(r'ab.c', flags=re.DOTALL)
lst = p.findall('ab8c ab-c ab.c ab\nc ab\tc ab+6c')
assert lst == ['ab8c', 'ab-c', 'ab.c', 'ab\nc', 'ab\tc']
