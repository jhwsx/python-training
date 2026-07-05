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
        print("苦读")


# 用 GoodStudent 调用自己的 study 方法
GoodStudent.study()
# 用 GoodStudent 调用 Student 中的 study 方法
super(GoodStudent, GoodStudent).study()
# 用 GoodStudent 调用 Person 中的 study 方法
super(Student, GoodStudent).study()
# 用 Student 调用 Person 中的 study 方法
super(Student, Student).study()
# super(Person, GoodStudent).study()  # AttributeError: 'super' object has no attribute 'study'

# 用 GoodStudent 调用自己的 name 属性
assert GoodStudent.name == 'goodstudent'
# 用 GoodStudent 调用 Student 中的 name 属性
assert super(GoodStudent, GoodStudent).name == 'student'
# 用 GoodStudent 调用 Person 中的 name 属性
assert super(Student, GoodStudent).name == 'person'
# 用 Student 调用 Person 中的 name 方法
assert super(Student, Student).name == 'person'


class Sportsman:
    def eat(self):
        print("吃很多")


class Student:
    def eat(self):
        print("吃一点")


class SportsStudent(Sportsman, Student):
    def eat(self):
        print("吃非常非常多")


ss = SportsStudent()
super(SportsStudent, ss).eat()
super(Sportsman, ss).eat()
