"""
set.copy()
- 返回该集合的一个副本
"""
s = {1, 2, 3, 4}
new_s = s.copy()
assert new_s == s
assert id(new_s) != id(s)
