"""
s.startswith(prefix[, start[, end]]) -> bool

prefix: 匹配的前缀，可以是字符串或者是由字符串组成的元组（元素中只要一个元素满足即可）
start: 开始索引，不指定默认为 0
end: 结束索引（闭区间）, 不指定默认为 len(str)

start 必须小于 end
返回值：布尔值，True 表示字符串是在 [start, end) 是以 prefix 指定的值开始的

s.endswith(suffix[, start[, end]]) -> bool

suffix: 匹配的后缀，可以是字符串或者是由字符串组成的元组（元素中只要一个元素满足即可）
start: 开始索引，不指定默认为 0
end: 结束索引（闭区间）, 不指定默认为 len(str)

start 必须小于 end
返回值：布尔值，True 表示字符串是在 [start, end) 是以 suffix 指定的值结束的
"""
s = 'hello world'
assert s.startswith('h')
assert s.startswith('he')
assert not s.startswith('eh')
assert s.startswith('wo', 6)
assert not s.startswith('ld', -1, -len(s))
assert s.startswith('ld', -2)

assert s.endswith('d')
assert s.endswith('o', 0, 5)
assert s.endswith(('d', 'ld'))
