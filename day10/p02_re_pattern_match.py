import re

# 1. 编译正则表达式字符串，返回一个 Pattern 类型的对象
p = re.compile('abcd')
assert type(p) is re.Pattern
print(p)  # re.compile('abcd')

# 2. 用该实例对象调用不同的方法来实现不同的匹配行为
"""
Pattern.match(string[, pos[, endpos]])
- string：要匹配的字符串
- pos：匹配的起始位置，默认为0
- endpos：匹配的结束位置，默认为字符串长度
- 当字符串的起始位置匹配成功，返回Match类的实例对象（
该实例对象包含匹配相关的信息：起始和结束位置、匹配的子串等等）；如果起始位置没有匹配，则返回 None
"""
m = p.match('mktintelabc\tabcdexddkllhabcd\nxyz?.908!@@', pos=12)
print(m)  # <re.Match object; span=(12, 16), match='abcd'>
assert type(m) is re.Match

# 3. 获取匹配内容
c = m.group()
assert c == 'abcd'
assert m.span() == (12, 16)
assert m.start() == 12
assert m.end() == 16

# 匹配失败的场景
p = re.compile('abcd')
m = p.match('mktintelabc\tabcdexddkllhabcd\nxyz?.908!@@')
assert m is None
