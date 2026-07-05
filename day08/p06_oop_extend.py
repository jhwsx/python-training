"""
继承
所有的类都默认继承内置的 object 类，通常不用显式地写出来
子类继承父类后，就可以调用父类中的属性和方法
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class Person:
    state = 'China'

    @staticmethod
    def eat():
        print('吃饭')

    @staticmethod
    def sleep():
        print('睡觉')


class Student(Person):

    @staticmethod
    def study():
        print('读书')


class Worker(Person):

    @staticmethod
    def work():
        print('工作')


assert Student.state == 'China'
Student.eat()
Student.study()
Worker.sleep()
Worker.work()
