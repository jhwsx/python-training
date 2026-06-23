"""
break
终止 break 所在的循环
"""

for _ in range(4):
    for i in range(3):
        if i >= 2:
            break
        else:
            print(i)
