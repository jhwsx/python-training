"""
多重继承
- 继承顺序：先找当前类，再按照从左往右的顺序依次找对应的父类
"""


class A:
    pass


class B:
    pass


class C(B, A):
    pass


class Sportsman:
    state = 'China'

    @staticmethod
    def exercise():
        print('锻炼')

    @staticmethod
    def eat():
        print("吃很多")


class Student:
    @staticmethod
    def study():
        print('读书')

    @staticmethod
    def eat():
        print("吃一点")


class SportsStudent(Sportsman, Student):
    pass


SportsStudent.study()
SportsStudent.exercise()
SportsStudent.eat()

