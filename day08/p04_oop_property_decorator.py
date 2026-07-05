class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property  # 内置的属性装饰器
    def isadult(self):  # 把该方法装饰成一个只读属性
        return self.age >= 18


p1 = Person('张三', 17)
assert not p1.isadult
p2 = Person('李四', 19)
assert p2.isadult
