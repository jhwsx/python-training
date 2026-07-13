"""
Pattern.sub(repl, string, count=0)
sub 是 substitute 的缩写
- repl：替换的字符串 或者 函数
- string：要被匹配后替换的字符串
- count：匹配后替换的最大次数，默认 0，表示替换所有的匹配
"""
import re

p = re.compile(r'blue|white|red')
string = p.sub('colour', 'blue socks and red shoes')
assert string == 'colour socks and colour shoes'
string = p.sub('colour', 'blue socks and red shoes', count=1)
assert string == 'colour socks and red shoes'


def func(matchobj):
    if matchobj.group() == '-':
        return '*'
    return '#'


p = re.compile(r'-{1,2}')
string = p.sub(func, 'pro----gram-files')
assert string == 'pro##gram*files'
