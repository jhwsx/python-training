import re
"""
^
- 匹配字符串的开头
- MULTILINE 模式下，还会继续匹配换行后的开头
"""
p = re.compile(r'ab')
lst = p.findall('abcd\nabfabg')
assert lst == ['ab', 'ab', 'ab']

p = re.compile(r'^ab')  # 可以理解为 ^ 匹配字符串开头的空字符串
lst = p.findall('abcd\nabfabg')
assert lst == ['ab']

"""
re.M     /     re.MULTILINE
- 多行匹配，影响 ^ 和 $
- 设置以后， `^` 匹配字符串的开始，和每一行的开始；`$` 匹配字符串尾，和每一行的结尾
"""
p = re.compile(r'^ab', flags=re.MULTILINE)  # 可以理解为 ^ 匹配每一行开头的空字符串
lst = p.findall('abcd\nabfabg')
assert lst == ['ab', 'ab']

