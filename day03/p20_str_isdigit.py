"""
def isdigit(self) -> bool

判断字符串中的每个字符是否都是数字型的字符

"""
s = '1234'
assert s.isdigit()

s = '-1234'
assert not s.isdigit()

s = '1.34'
assert not s.isdigit()

s = '3 + 4j'
assert not s.isdigit()

s = 'hello123'
assert not s.isdigit()
