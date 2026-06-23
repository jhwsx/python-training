"""
print(*values, ..., sep=' ', end='\n', file=None, flush=False)
*values 不定长参数，可以接受0个或者多个位置参数，贪婪的, 不能接受关键字参数
sep, end, file, flush 是默认参数
没有返回值, 即返回 None
"""
print(1, 0.1, "hello", 3 + 4j, True)
print(1, 0.1, "hello", 3 + 4j, True, sep=',')  # 这里的 sep=，是关键字参数的形式
print("hello, ", end='')
print("world")

