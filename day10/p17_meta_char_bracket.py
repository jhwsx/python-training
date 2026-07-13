import re
"""
[]
用于表示一个字符集：
- 字符可以单独列出，比如 [amk] 匹配 'a'，'m'，或者 'k'
- 可以表示字符范围，通过用 - 将两个字符连起来
- 特殊字符在字符集中，失去它的特殊含义
- 特殊序列，如 \d \s \w 在字符集中可以被接受
- 不在字符集范围内的字符可以通过取反来进行匹配，如果字符集首字符是 `^` ，
  所有不在字符集内的字符将会被匹配， `^` 如果不在字符集首位，就没有特殊含义
"""
# - 字符可以单独列出，比如 [amk] 匹配 'a'，'m'，或者 'k'
p = re.compile(r'[amk]')  # 等价于 r'a|m|k'
lst = p.findall('I have a monkey')
assert lst == ['a', 'a', 'm', 'k']
string = 'ae7bdecd3'
p = re.compile(r'[de][367]')
lst = p.findall(string)
assert lst == ['e7', 'd3']
p = re.compile(r'[de]|[367]')  # 等价于r'[de367]'
lst = p.findall(string)
assert lst == ['e', '7', 'd', 'e', 'd', '3']
p = re.compile(r'de|367')
lst = p.findall(string)
assert lst == ['de']
p = re.compile(r'de367')
lst = p.findall(string)
assert lst == []

# - 可以表示字符范围，通过用 - 将两个字符连起来
p = re.compile(r"[a-y]")
lst = p.findall("ahzyqAHZYQ")
assert lst == ['a', 'h', 'y', 'q']

p = re.compile(r"[0-5][A-Y]")
lst = p.findall("a0hzyq125A6HZYQ")
assert lst == ['5A']

p = re.compile(r"[a-zA-Z]")
lst = p.findall("AabZ12c")
assert lst == ['A', 'a', 'b', 'Z', 'c']
p = re.compile(r"[a-z]", flags=re.IGNORECASE)  # re.I/re.IGNORECASE 进行忽略大小写匹配
lst = p.findall("AabZ12c")
assert lst == ['A', 'a', 'b', 'Z', 'c']

# - 特殊字符在字符集中，失去它的特殊含义
p = re.compile(r'[.+]')
lst = p.findall('abc')
assert lst == []
p = re.compile(r'[.+]')
lst = p.findall('a.b+c.d+')
assert lst == ['.', '+', '.', '+']

# - 特殊序列，如 \d \s \w 在字符集中可以被接受
p = re.compile(r'[\d]')  # 可以简化为 r'\d'
lst = p.findall('a1234b')
assert lst == ['1', '2', '3', '4']
p = re.compile(r'[\d+]')
lst = p.findall('a1234b+')
assert lst == ['1', '2', '3', '4', '+']
p = re.compile(r'[a\sb]')
lst = p.findall('adb a bc')
assert lst == ['a', 'b', ' ', 'a', ' ', 'b']
p = re.compile(r'[\w]')
lst = p.findall('adb_a b!c')
assert lst == ['a', 'd', 'b', '_', 'a', 'b', 'c']

# - 不在字符集范围内的字符可以通过取反来进行匹配，如果字符集首字符是 `^` ，
# 所有不在字符集内的字符将会被匹配， `^` 如果不在字符集首位，就没有特殊含义

