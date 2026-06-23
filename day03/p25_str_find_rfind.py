"""
str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found within the slice s[start:end].
str.index(sub[, start[, end]])
Like find() but raises ValueError when the substring sub is not found.

str.rfind(sub[, start[, end]])
Return the highest index in the string where substring sub is found within the slice s[start:end].
str.rindex(sub[, start[, end]])
Like rfind() but raises ValueError when the substring sub is not found.

返回的是正向索引

"""
s = 'who knows who cares you'
assert s.find('who') == 0
assert s.rfind('who') == 10
assert s.find('what') == -1
assert s.find('who', 0, 3) == 0
assert s.rfind('who', 0, 3) == 0
prints.rfind('who', 0, 3)()
# s.rindex('what')  # ValueError: substring not found