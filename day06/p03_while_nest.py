"""
while 嵌套
"""

"""
输出
1 2 3 4
5 6 7 8
"""
row = 1
num = 1
while row <= 2:
    if row > 1:
        print()
    while num <= row * 4:
        print(num, end=' ')
        num += 1
    row += 1
print()
"""
九九乘法表
"""
row = 1
while row <= 9:
    column = 1
    while column <= row:
        print(f'{column}x{row}={column * row}', end='\t')
        column += 1
    print()
    row += 1
