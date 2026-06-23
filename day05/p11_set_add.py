"""
set.add(elem)
- 将指定元素添加到集合中。如果元素已经存在，则不做任何操作
"""
s = {1, 2, 3}
s.add('hello world')
print(s)
s.add(1)
print(s)
# s.add()  # TypeError: add() takes exactly one argument (0 given)
s.add([1, 2])  # TypeError: unhashable type: 'list'
