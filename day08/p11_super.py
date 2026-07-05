"""
super(type, object).attr/method
super 是一个内置类
- type：只能传类对象
- object：可以是实例对象，也可以是类对象
- attr/method：要调用的属性或方法
- 效果：根据object的继承顺序，用object调用type下一个顺序类中的attr/method
- 适用场景：在子类重写父类方法或属性之后，想再调用父类的该方法或属性
"""


class Person:
    state = 'China'
    name = 'person'

    @staticmethod
    def study():
        print('不学习')


class Student(Person):
    name = 'student'

    @staticmethod
    def study():
        print('读书')


class GoodStudent(Student):
    name = 'goodstudent'

    @staticmethod
    def study():
        # super().study() 报错
        print("苦读")


class Sportsman:
    def eat(self):
        print("吃很多")

    @classmethod
    def study(cls):
        print('不学习')

class Student:
    def eat(self):
        print("吃一点")

    @classmethod
    def study(cls):
        print('学习')


class SportsStudent(Sportsman, Student):
    def eat(self):
        super().eat()  # 等价于
        # super(type(self), self).eat()
        print("吃非常非常多")

    @classmethod
    def study(cls):
        super(Sportsman, cls).study()
        super(cls, cls).study()
        super().study()
        print('半学')


ss = SportsStudent()
ss.eat()

SportsStudent.study()