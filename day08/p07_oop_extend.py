class A:
    pass


class B(A):
    pass


class C(B):
    pass


class Person:
    state = 'China'

    @staticmethod
    def study():
        print('不学习')


class Student(Person):
    pass
    # @staticmethod
    # def study():
    #     print('读书')


class GoodStudent(Student):
    pass
    # @staticmethod
    # def study():
    #     print("苦读")


GoodStudent.study()



