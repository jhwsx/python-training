import re

p = re.compile(r'<.*>')
m = p.search('<a> b <c>')
assert m.group() == '<a> b <c>'

p = re.compile(r'<.*?>')
m = p.search('<a> b <c>')
assert m.group() == '<a>'

p = re.compile(r"ab+?")
m = p.search("abbbc")
assert m.group() == 'ab'

p = re.compile(r"ab??")
m = p.search("abc")
assert m.group() == 'a'
