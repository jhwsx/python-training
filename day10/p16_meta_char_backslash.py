"""
\
① 转义正则元字符
正则特殊符号 ^ $ * + ? . ( ) [ ] { } | \ 前面加 \，变成普通文本字符。
例：想匹配文本 $，正则写 \$。
② 构造转义序列
搭配字母形成特殊匹配符号：
\n 换行、\d 数字、\s 空白、\w 字母数字下划线等。
"""
import re

string = 'aA2...c7+8d..J9++0.+++H'
p = re.compile(r'.')
lst = p.findall(string)
assert lst == ['a', 'A', '2', '.', '.', '.', 'c', '7', '+', '8', 'd', '.', '.', 'J', '9', '+', '+', '0', '.', '+', '+', '+', 'H']
p = re.compile(r'\.')
lst = p.findall(string)
assert lst == ['.', '.', '.', '.', '.', '.']
p = re.compile(r'\.+')
lst = p.findall(string)
assert lst == ['...', '..', '.']
p = re.compile(r'\+')
lst = p.findall(string)
assert lst == ['+', '+', '+', '+', '+', '+']
p = re.compile(r'\++')
lst = p.findall(string)
assert lst == ['+', '++', '+++']

# \A 匹配字符串的开头，类似 ^, 区别在于: MULTILINE 模式下，\A 不识别换行
p = re.compile(r'^ab')
lst = p.findall('abcd\nabfg')
assert lst == ['ab']
p = re.compile(r'^ab', flags=re.MULTILINE)
lst = p.findall('abcd\nabfg')
assert lst == ['ab', 'ab']
p = re.compile(r'\Aab')
lst = p.findall('abcd\nabfg')
assert lst == ['ab']
p = re.compile(r'\Aab', flags=re.MULTILINE)
lst = p.findall('abcd\nabfg')
assert lst == ['ab']

# \Z 匹配字符串的末尾，类似 $, 区别在于: MULTILINE 模式下，\Z 不识别换行
p = re.compile(r'cd\Z')
lst = p.findall('abcd')
assert lst == ['cd']
lst = p.findall('abcd\n')
assert lst == []
p = re.compile(r'cd\Z', flags=re.MULTILINE)
lst = p.findall('abcd\nef')
assert lst == []
p = re.compile(r'\Z')
lst = p.findall('abcd\n')
assert lst == ['']

# \b 匹配空字符串，但只在单词开始或结尾的位置，即匹配一个单词边界
p = re.compile(r'er\b')
m = p.search('never')
assert m.group() == 'er'
m = p.search('verb')
assert m is None
p = re.compile(r'\ber')
m = p.search('error')
assert m.group() == 'er'

p = re.compile(r'\ba\b')
m = p.search('I have a dog')
assert m.group() == 'a'
m = p.search('alpha')
assert m is None

# \B 匹配空字符串，但不能在单词开始或结尾的位置，即匹配非单词边界
p = re.compile(r'er\B')
m = p.search('never')
assert m is None
m = p.search('verb')
assert m.group() == 'er'
p = re.compile(r'\Ba\B')
m = p.search('I have two dogs')
assert m.group() == 'a'
lst = p.findall('I have a panda')
assert lst == ['a', 'a']

# 正则里面的单词成分：字母，数字，下划线，不带有特殊符号的文字
p = re.compile(r'er\B')
lst = p.findall('error')
assert lst == ['er']
lst = p.findall('er123')
assert lst == ['er']
lst = p.findall('er_123')
assert lst == ['er']
lst = p.findall('er呃呃')
assert lst == ['er']
lst = p.findall('er-123')
assert lst == []
lst = p.findall('er+123')
assert lst == []
lst = p.findall('er!hello')
assert lst == []
lst = p.findall('er! hello')
assert lst == []

# /w 匹配单词成分
p = re.compile(r'a\wb')
lst = p.findall('adba9ba_ba b')
assert lst == ['adb', 'a9b', 'a_b']
lst = p.findall('adb a9b a_b a我b a b a+b a~b a-b a\tb')
assert lst == ['adb', 'a9b', 'a_b', 'a我b']

# /W 匹配非单词成分
p = re.compile(r'a\Wb')
lst = p.findall('adba9ba_ba b')
assert lst == ['a b']
lst = p.findall('adb a9b a_b a我b a b a+b a~b a-b a\tb')
assert lst == ['a b', 'a+b', 'a~b', 'a-b', 'a\tb']

# \d 匹配任意一个数字字符
p = re.compile(r'\d')
lst = p.findall('a1234b')
assert lst == ['1', '2', '3', '4']
lst = p.findall('a7TH12bkNB34d096')
assert lst == ['7', '1', '2', '3', '4', '0', '9', '6']
p = re.compile(r'\d+')
lst = p.findall('a1234b')
assert lst == ['1234']
lst = p.findall('a7TH12bkNB34d096')
assert lst == ['7', '12', '34', '096']

# \D 匹配任意一个非数字字符
p = re.compile(r'\D')
lst = p.findall('a1234b')
assert lst == ['a', 'b']
lst = p.findall('a7TH12bkNB34d096')
assert lst == ['a', 'T', 'H', 'b', 'k', 'N', 'B', 'd']
p = re.compile(r'\D+')
lst = p.findall('a1234b')
assert lst == ['a', 'b']
lst = p.findall('a7TH12bkNB34d096')
assert lst == ['a', 'TH', 'bkNB', 'd']

# \s 匹配任何一个空白符（空白符包括空格，换行符，制表符）
p = re.compile(r'a\sb')
lst = p.findall('adb a bc')
assert lst == ['a b']
p = re.compile(r'a\sc')
lst = p.findall('a c a\nc a\tc abc a+c a化c a?c')
assert lst == ['a c', 'a\nc', 'a\tc']

# \S 匹配任何一个非空白符（空白符包括空格，换行符，制表符）
p = re.compile(r'a\Sb')
lst = p.findall('adb a bc')
assert lst == ['adb']
p = re.compile(r'a\Sc')
lst = p.findall('a c a\nc a\tc abc a+c a化c a?c')
assert lst == ['abc', 'a+c', 'a化c', 'a?c']
