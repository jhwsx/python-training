"""
list.sort([key], reverse=False)

- key：必须指定一个可调用对象（比如：函数，类）
- reverse：默认为False，代表升序，指定为True，则为降序
- 对原列表进行排序，无返回值
"""

lst = [3, 2, 7, -10, 9]
lst.sort()
assert lst == [-10, 2, 3, 7, 9]

lst = [3, 2, 7, -10, 9]
lst.sort(reverse=True)
assert lst == [9, 7, 3, 2, -10]

lst = [3, 2, 7, -10, 9]
lst.sort(key=abs)
assert lst == [2, 3, 7, 9, -10]

lst = [6, 8, '2', 0, 1]
# lst.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lst = [[1, 3, 2], [1, 2, 1], [7, 9]]
lst.sort(reverse=True)
assert lst == [[7, 9], [1, 3, 2], [1, 2, 1]]

"""
字符串之间可以进行大小比较，是逐个字符进行比较的，
比较字符在 Unicode 里对应的整数大小

chr(i) 返回整数 i 在 Unicode 里对应的字符
ord(c) 返回字符 c 在 Unicode 里对应的整数
"""
print(chr(48))
print(ord('超'))
lst = ['3', '2', '7', '-10', '9']
lst.sort(key=int)
assert lst == ['-10', '2', '3', '7', '9']


def f(item):
    return abs(int(item))


lst = ['3', '2', '7', '-10', '9']
lst.sort(key=f)
assert lst == ['2', '3', '7', '9', '-10']
