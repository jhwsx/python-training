"""
complex(real=0, imag=0) 这里是默认参数

- 创建一个 real + imag*1j 的复数并返回
- 如果第一个参数是字符串，它将被解释为复数，此时不能传第二个参数
- 如果没有传实参，则返回0j
"""

print(complex)  # <class 'compex'>
print(complex())  # 0j
print(complex(3.2, 4))  # (3.2+4j)
print(complex(3.2))  # (3.2+0j)
print(complex('3.2'))  # (3.2+0j)
# print(complex('3.2', '4'))  # TypeError: complex() can't take second arg if first is a string
# print(complex('3.2', 4))  # TypeError: complex() can't take second arg if first is a string
print(complex('3.2+4j'))  # (3.2+4j)
print(complex('3.2 + 4j'))  # ValueError: complex() arg is a malformed string
print(complex(3, 2j))  # (1+0j)
