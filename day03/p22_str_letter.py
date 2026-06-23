"""
str.capitalize()
将字符串的首字母变成大写，其他字母变小写，并返回

str.title()
将字符串中所有单词的首字母变成大写，其他字母变小写，并返回

str.upper()
将字符串中所有字符变成大写，并返回

str.lower()
将字符串中所有字符变成小写，并返回

str.swapcase()
将字符串中所有大写字符变成小写，小写变成大写，并返回
"""
s = 'hello 中国, welCome to CHINA!'
assert s.capitalize() == 'Hello 中国, welcome to china!'
assert s.title() == 'Hello 中国, Welcome To China!'
assert s.upper() == 'HELLO 中国, WELCOME TO CHINA!'
assert s.lower() == 'hello 中国, welcome to china!'
assert s.swapcase() == 'HELLO 中国, WELcOME TO china!'
