"""
str.strip([chars])
删除字符串左右两边指定的字符

chars: 指定要删除的字符，如果没有指定，则默认移除空白符（空格符 换行符 制表符）
"""
s = ' \t\nhello \t\nworld \t\n'
new_s = s.strip()
assert new_s == 'hello \t\nworld'

new_s = s.strip('\t ')
assert new_s == '\nhello \t\nworld \t\n'

s = 'hello world'
new_s = s.strip('heldo ')
assert new_s == 'wor'

new_s = s.strip(' ehlod')
assert new_s == 'wor'
