"""
转义字符
\\  一个反斜杠
\'  一个单引号
\"  一个双引号
\t  一个横向制表符
\n  一个换行符
"""
s = '\\\\\\'
print(s)

# 路径
path = r'D:\abc\rst\test\name.py'  # r 是 raw 的意思, 原始字符串
print(path)

# 字符串末尾不能存在奇数个反斜杠，会引发语法错误
# ss = 'hello\\\'  # SyntaxError: EOL while scanning string literal
# ss = r'hello\\\'   # SyntaxError: EOL while scanning string literal

# 在列表中, 字符串的定义符号尽量会用单引号来体现，否则使用双引号，不会使用三引号的形式
s1 = 'ab\n1234'
s2 = r'ab\n1234'
s3 = """123'bcd"4eew"""

print([s1, s2, s3])  # ['ab\n1234', 'ab\\n1234', '123\'bcd"4eew']


