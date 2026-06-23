"""
S.count(sub[, start[, end]]) -> int

sub: 要查找的字符串
start: 开始索引，默认为 0
end: 结束索引（开区间）, 默认为 len(str)
返回值：int，表示 sub 在字符串中出现的次数
"""
s = 'hello world'
assert s.count('l') == 3
assert s.count('l', 0, 5) == 2
assert s.count('') == len(s) + 1  # 空字符串 '' 在字符串中，出现在每两个字符之间，以及开头和结尾！
assert s.count('wo', 6) == 1
