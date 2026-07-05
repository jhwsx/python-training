"""
封装
在属性名或方法名前面加两个下划线开头，声明为私有属性或私有方法
私有属性或私有方法只能在类的内部被调用，不能在类的外部直接被调用
"""


class Student(object):
    # 类属性
    school = 'hpu'
    __food = 'rice'  # food 是私有属性

    def __init__(self, name, age, grade):  # 这里覆盖了 object 类中的 __init__ 方法
        # 实例属性
        self.name = name
        self.__age = age
        self.grade = grade

    def study(self, course):
        return self.__self_study(course)

    def __self_study(self, course):  # 私有的对象方法
        return f'{self.name}在听{course}课'

    @classmethod
    def play(cls, ball):
        return f'{cls.school}的学生喜欢打{ball}'

    @staticmethod
    def exam(course):
        return f'考{course}科目'

    @classmethod
    def get_food(cls):
        return cls.__food

    def get_age(self):
        return self.__age


assert Student.school == 'hpu'
# Student.__food  # AttributeError: type object 'Student' has no attribute '__food'
assert Student.get_food() == 'rice'

stu1 = Student('张三', 16, '大一')
assert stu1.get_age() == 16


# stu1.__self_study('Python')  # AttributeError: 'Student' object has no attribute '__self_study'
print(stu1.__dict__)
print(Student.__dict__)
print(Student._Student__self_study(stu1, 'Python'))
