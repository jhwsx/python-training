"""
str.join(iterable)

- iterable：包括str、list、tuple、dict、set等
- 将可迭代对象中的元素（元素必须是字符串）以指定的字符串连接，返回新的字符串
"""
assert ','.join('hello world') == 'h,e,l,l,o, ,w,o,r,l,d'
assert '='.join(['1', '2', '3']) == '1=2=3'
assert ', '.join(('1', '2', '3')) == '1, 2, 3'
assert ';'.join({'one': 1, 'two': 2}) == 'one;two'
print('###'.join({'one', 'one', 'two', 'three'}))  # 多次运行结果不一样，因为 set 是无序的
# '+'.join([1, 2, 3])  # TypeError: sequence item 0: expected str instance, int found
