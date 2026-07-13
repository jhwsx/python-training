import re

# 1. 编译正则表达式字符串，返回一个 Pattern 类型的对象
p = re.compile('abcd')
assert type(p) is re.Pattern
print(p)  # re.compile('abcd')

# 2. 用该实例对象调用不同的方法来实现不同的匹配行为
"""
Pattern.findall(string[, pos[, endpos]])

- string：要匹配的字符串
- pos：匹配的起始位置，默认为0
- endpos：匹配的结束位置，默认为字符串长度
- 对字符串从左往右扫描，找到所有不重复匹配，以列表的形式返回，如果有子组，那么只保留子组的捕获内容，
如果子组多个（至少两个子组），则以元组形式构建列表，如果没有找到匹配的，则返回空列表
"""
lst = p.findall('mktintelabc\tabcdexddkllhabcd\nxyz?.908!@@')
assert lst == ['abcd', 'abcd']
assert type(lst) is list

# 匹配失败的场景
p = re.compile('abc d')
lst = p.findall('mktintelabc\tabcdexddkllhabcd\nxyz?.908!@@')
assert lst == []
