"""
str(object='')

- 将object转化为字符串形式并返回。
"""
print(str)  # <class 'str'>
assert str() == ''
assert str('hello') == 'hello'
assert str(0) == '0'
assert str(0.1) == '0.1'
assert str(True) == 'True'
assert str(3+4j) == '(3+4j)'
assert str([]) == '[]'
assert str(()) == '()'
assert str({}) == '{}'
assert str(None) == 'None'
assert str(['a', 'b', True]) == "['a', 'b', True]"
