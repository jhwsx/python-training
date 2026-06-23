"""
算术运算符
+ 加
- 减
* 乘
/ 除, 结果一定是浮点数
% 取模（求余数）, 余数的符号总是和除数一致
** 幂
// 整除（相当于 / 的结果再向下取整数）
"""
a = 5
b = 2
assert a + b == 7
assert a - b == 3
assert a * b == 10
assert a / b == 2.5
assert a % b == 1
assert a ** b == 25
assert a // b == 2

a = 5
b = -2
assert a + b == 3
assert a - b == 7
assert a * b == -10
assert a / b == -2.5
assert a % b == -1  # 被除数 - 除数 * 商 = 余数 5 - (-2) * -3 = 5 - 6 = -1
assert a ** b == 0.04
assert a // b == -3

a = -5
b = 2
assert a + b == -3
assert a - b == -7
assert a * b == -10
assert a / b == -2.5
assert a % b == 1  # 被除数 - 除数 * 商 = 余数 -5 - 2 * -3 = -5 + 6 = 1
assert a ** b == 25
assert a // b == -3

a = -17
b = -6
assert a / b == 17 / 6
assert a % b == -5  # 被除数 - 除数 * 商 = 余数 -17 - (-6 * 2) = -17 + 12 = -5
assert a // b == 2
