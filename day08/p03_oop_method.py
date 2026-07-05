class Student(object):
    # 类属性
    school = 'hpu'

    def __init__(self, name, age, grade):  # 这里覆盖了 object 类中的 __init__ 方法
        # 实例属性
        self.name = name
        self.age = age
        self.grade = grade

    def study(self, course):  # 对象方法, 记录在类命名空间
        return f'{self.name}在听{course}课'

    @classmethod  # 内置的类方法装饰器
    def play(cls, ball):  # 类方法，记录在类命名空间
        return f'{cls.school}的学生喜欢打{ball}'

    @staticmethod  # 内置的静态方法装饰器
    def exam(course):  # 类方法，记录在类命名空间
        return f'考{course}科目'


stu1 = Student('张三', 16, '大一')  # 实例化
stu2 = Student('李四', 17, '大二')
stu3 = Student('王五', 18, '大三')

# 调用对象方法, 既可以用类对象调用，也可以用实例对象调用(推荐)
print(Student.study(stu1, 'Python'))
print(stu1.study('C++'))
stu1.__init__('王五', 19, '大四')
assert stu1.age == 19
assert stu1.grade == '大四'
Student.__init__(stu1, '王五', 20, '研一')
assert stu1.age == 20
assert stu1.grade == '研一'

# 调用类方法, 既可以用类对象调用(推荐)，也可以用实例对象调用
print(Student.play('篮球'))
print(stu2.play('乒乓球'))

# 调用静态方法, 既可以用类对象调用(推荐)，也可以用实例对象调用
print(Student.exam('英语'))
print(stu3.exam('物理'))

print(Student.__dict__)
