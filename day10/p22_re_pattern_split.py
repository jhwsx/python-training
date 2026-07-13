"""
Pattern.split(string, maxsplit=0)

- string：要匹配的字符串
- maxsplit：最大分割次数，默认为 0，表示不限制次数
- 按照匹配的子串将字符串分割，以列表形式返回
- 如果有捕获分组，那么分组里匹配的内容也会包含在结果中
"""
import re


p = re.compile(r"\W+")  # 匹配到正则表达式的部分就是切割点
lst = p.split('Words, words,!@words.')
assert lst == ['Words', 'words', 'words', '']
lst = p.split('Words, words,!@words.', maxsplit=2)
assert lst == ['Words', 'words', 'words.']

p = re.compile(r"(\W+)")
lst = p.split('Words, words,!@words.')
assert lst == ['Words', ', ', 'words', ',!@', 'words', '.', '']

p = re.compile(r"(\W)+")
# 0组第1次匹配成功 (\W)(\W), 0组匹配到 ', ', 1组捕获到 ' '
# 0组第2次匹配成功 (\W)(\W)(\W), 0组匹配到 ',!@', 1组捕获到 '@'
# 0组第3次匹配成功 (\W)(\W), 0组匹配到 '.', 1组捕获到 '.'
lst = p.split('Words, words,!@words.')
assert lst == ['Words', ' ', 'words', '@', 'words', '.', '']
# 0组第1次匹配成功 (\W)(\W)(\W), 0组匹配到 '...', 1组捕获到 '.'
# 0组第2次匹配成功 (\W)(\W), 0组匹配到 ', ', 1组捕获到 ' '
# 0组第3次匹配成功 (\W)(\W), 0组匹配到 ', ', 1组捕获到 ' '
# 0组第4次匹配成功 (\W)(\W)(\W), 0组匹配到 '...', 1组捕获到 '.'
lst = p.split('...Words, words, words...')
assert lst == ['', '.', 'Words', ' ', 'words', ' ', 'words', '.', '']
