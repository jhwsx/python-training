import re

string = r'a8t\TYh\\n>S\\\M9aa<2KaaaJ3+'

pattern = '\\\\'  # 匹配单反斜杠
p = re.compile(pattern)

lst = p.findall(string)
assert lst == ['\\', '\\', '\\', '\\', '\\', '\\']

pattern = '\\\\\\\\'  # 匹配双反斜杠
p = re.compile(pattern)

lst = p.findall(string)
assert lst == ['\\\\', '\\\\']

pattern = r'\\'  # 匹配单反斜杠, 避免了 python 本身的那次转义
p = re.compile(pattern)  # 正则还会进行一次转义

lst = p.findall(string)
assert lst == ['\\', '\\', '\\', '\\', '\\', '\\']

pattern = r'\\\\'  # 匹配双反斜杠
p = re.compile(pattern)

lst = p.findall(string)
assert lst == ['\\\\', '\\\\']

string = 'a8t\TYh\\n>S\\\M9aa<2\nKaaa\nJ3+'
pattern = r'\n'
p = re.compile(pattern)  # \n 在正则表达式里面会被认为是转义字符
assert p.findall(string) == ['\n', '\n']
