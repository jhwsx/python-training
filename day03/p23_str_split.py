"""
str.split(sep=None, maxsplit=-1)

通过指定的分隔符对字符串进行分割，以列表的形式返回

sep: 分隔符，不指定时默认为所有的空白符，并且丢弃掉结果中的空字符串
maxsplit: 最大分隔次数，默认为-1，表示不限制
返回值: 返回列表
"""
s = 'hello world'
assert s.split('l') == ['he', '', 'o wor', 'd']
assert s.split('ll') == ['he', 'o world']
assert s.split(' ') == ['hello', 'world']
# s.split('')  # ValueError: empty separator
s = ' ab  \t1234   \ncde'
assert s.split(' ') == ['', 'ab', '', '\t1234', '', '', '\ncde']
assert '1<>2<>3'.split('<>') == ['1', '2', '3']
assert '1<>2<>3'.split('<>', 1) == ['1', '2<>3']
assert '   1   2   \t3\n   '.split() == ['1', '2', '3']
