"""
__str__ 和 __repr__ 方法
是两个魔术方法
要求返回值必须是字符串
1. 当实例对象被直接转字符串(print时，被字符串格式化时，被转为字符串时)时，
会自动调用 __str__ 方法，如果没有找到该方法，则自动调用 __repr__ 方法
2. 当实例对象作为另外一个数据的成员时，只会自动调用 __repr__ 方法
"""


class Dog:
    def __str__(self):
        return '狗'

    def __repr__(self):
        return '汪汪'


d = Dog()
print(d)

print([d])
