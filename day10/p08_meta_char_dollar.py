import re
"""
$
- 匹配字符串的末尾 或者 匹配在字符串结尾的换行符之前的末尾
- MULTILINE 模式下，还会匹配换行符之前的末尾（换行符可以不在字符串末尾）
"""

p = re.compile(r'cd')
lst = p.findall('acdghcd\nbcd')
assert lst == ['cd', 'cd', 'cd']
p = re.compile(r'cd$')  # 可以理解为 $ 匹配字符串结尾的空字符串
lst = p.findall('acdghcd\nbcd')
assert lst == ['cd']
p = re.compile(r'cd$')  # 可以理解为 $ 匹配在字符串结尾的换行符之前的末尾的空字符串
lst = p.findall('acdghcd\nbcd\n')
assert lst == ['cd']

"""
re.M     /     re.MULTILINE
- 多行匹配，影响 ^ 和 $
- 设置以后， `^` 匹配字符串的开始，和每一行的开始；`$` 匹配字符串尾，和每一行的结尾
"""
p = re.compile(r'cd$', flags=re.MULTILINE)
lst = p.findall('acdghcd\nbcd\n')
assert lst == ['cd', 'cd']

