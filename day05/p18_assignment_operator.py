"""
赋值运算符
= 简单的赋值运算符
   增强赋值
+= 加法赋值运算符
-= 减法赋值运算符
*= 乘法赋值运算符
/= 除法赋值运算符
%= 取模赋值运算符
**= 幂赋值运算符
//= 取整赋值运算符
"""
a = 8
b = 3
a += b
assert a == 11

a = 8
b = 3
a -= b
assert a == 5

a = 8
b = 3
a *= b
assert a == 24

a = 8
b = 3
a /= b
assert a == 8 / 3

a = 8
b = 3
a %= b
assert a == 2

a = 8
b = 3
a **= b
assert a == 8 * 8 * 8

a = 8
b = 3
a //= b
assert a == 2
