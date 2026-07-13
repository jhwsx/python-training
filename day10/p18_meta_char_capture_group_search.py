"""
(...)

捕获分组，匹配括号内的任意正则表达式，并标识出该分组的开始和结尾。
组从 0 开始编号，组 0 始终存在，它表示整个正则，所以Match的对象方法都将组 0 作为默认参数；
子组从左到右编号，从 1 向上编号
分组匹配的内容可以在之后其他分组用 \number 进行再次引用
"""

import re

p = re.compile('abcdefg.+')
m = p.search('abcdefghijk')
print(m)
assert m.group() == 'abcdefghijk'  # 获取0组的匹配内容
assert m.group(0) == 'abcdefghijk'  # 获取0组的匹配内容
# m.group(1)  # IndexError: no such group

p = re.compile('a(bc)d(efg)(.+)')
m = p.search('abcdefghijk')
print(m)
"""
Match.group(*groupN)   

- 参数是不定长参数
- groupN：对应的组号，默认为 0，返回整个匹配结果
- 返回一个或者多个子组的匹配结果，如果有多个参数，结果就是一个元组
"""
assert m.group() == 'abcdefghijk'  # 获取0组的匹配内容
assert m.group(0) == 'abcdefghijk'  # 获取0组的匹配内容
assert m.group(1) == 'bc'
assert m.group(2) == 'efg'
assert m.group(3) == 'hijk'
assert m.group(0, 1, 2, 3) == ('abcdefghijk', 'bc', 'efg', 'hijk')

"""
Match.span([group])
- 返回一个元组，包含 (Match.start([group]), Match.end([group]))，group默认为 0
"""
assert m.span() == (0, 11)
assert m.span(1) == (1, 3)
assert m.span(2) == (4, 7)
assert m.span(3) == (7, 11)

"""
Match.start([group])
- 返回对应 group 匹配开始的位置，group默认为 0

Match.end([group])
- 返回对应 group 匹配结束的位置，group默认为 0
"""
assert m.start() == 0
assert m.end() == 11
assert m.start(1) == 1
assert m.end(1) == 3
assert m.start(2) == 4
assert m.end(2) == 7
assert m.start(3) == 7
assert m.end(3) == 11
