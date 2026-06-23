"""
float([x])

- x：接收数字或特定字符串
- 将x转换为浮点数并返回，如果没有给x指定值，则返回0.0
"""

print(float)  # <class 'float'>
print(float())  # 0.0
print(float(7.89))  # 7.89
print(float(-7.89))  # -7.89
print(float(7))  # 7.0
print(float("7.89"))  # 7.89
print(float("-7.89"))  # -7.89
print(float("7"))  # 7.0
print(float(True))  # 1.0
print(float(False))  # 0.0
# print(float(3 + 4j))  # TypeError: can't convert complex to float
# print(float("hello"))  # ValueError: could not convert string to float: 'hello'
# print(float("7.89hello"))  # ValueError: could not convert string to float: '7.89hello'
assert int(float('7.89')) == 7