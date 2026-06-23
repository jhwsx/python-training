"""
int([x])
- x: 接收数字或者特定字符串
- 作用：将 x 转换为整数并返回，如果没有给 x 指定值，则返回 0
"""
print(int)  # <class 'int'>
print(int())  # 0
print(int(1))  # 1
print(int(7.89))  # 7，直接舍弃小数部分
print(int(-7.89))  # -7, 直接舍弃小数部分
print(int("1"))  # 1
print(int("-1"))  # -1
# print(int("7.89"))  # ValueError: invalid literal for int() with base 10: '7.89'
print(int(True))  # 1
print(int(False))  # 0
# print(int(3+4j)) # TypeError: can't convert complex to int
# print(int("hello"))  # ValueError: invalid literal for int() with base 10: 'hello'

