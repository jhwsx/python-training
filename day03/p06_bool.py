"""
bool([x])

- 根据x指定的值，返回布尔值
- 如果没有给x指定值，则返回False

数字0, 0.0, 0j, False,
空字符串, 空列表, 空元组,
空字典, 空集合, None
...
以上这些数据bool判定为False,
其它数据通常判定为True
"""
print(bool)  # <class 'bool'>
# False
assert not bool()
assert not bool(0)
assert not bool(0.0)
assert not bool(0j)
assert not bool(0J)
assert not bool(False)
assert not bool('')
assert not bool({})
assert not bool([])
assert not bool(())
assert not bool(set())
assert not bool(None)

# True
assert bool(3)
assert bool(3.14)
assert bool(' ')
assert bool('0')
assert bool('False')
assert bool('None')
assert bool('[]')
assert bool(True)
