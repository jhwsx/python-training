"""
for 嵌套
"""

"""
输出
1 2 3 4
5 6 7 8
"""
for row in range(1, 3):
    if row > 1:
        print()
    for num in range(1 + 4 * (row - 1), 1 + 4 * row):
        print(num, end=' ')
print()

"""
九九乘法表
"""
for row in range(1, 10):
    for column in range(1, row + 1):
        print(f'{column}x{row}={column * row}', end='\t')
    print()
