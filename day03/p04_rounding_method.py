import math

"""
四舍五入
    round(number[, ndigits]) 对 number 做四舍五入，精确到小数点后 ndigits 位
    如果 ndigits 没有指定，则默认保留到整数位
    返回四舍五入后的结果
"""
assert round(7.89, 0) == 8.0
assert round(-7.89, 0) == -8.0

assert round(7.89, 1) == 7.9
assert round(-7.89, 1) == -7.9

# 向上取整
assert math.ceil(7.89) == 8
assert math.ceil(-7.89) == -7

# 向下取整
assert math.floor(7.89) == 7
assert math.floor(-7.89) == -8

# 舍弃小数部分
assert math.trunc(7.89) == 7
assert math.trunc(-7.89) == -7

