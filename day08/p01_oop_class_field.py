# object 类是所有类的父类
# 所有类默认集成 object 类
class Student(object):
    # 类属性
    school = 'hpu'
    # Student.school2 = 'hpu'  # Error

    def __init__(self, name, age, grade):
        # 实例属性
        self.name = name
        self.age = age
        self.grade = grade
        print(locals())


print(Student)
stu1 = Student('张三', 16, '大一')  # 实例化
stu2 = Student('李四', 17, '大二')
stu3 = Student('王五', 18, '大三')
# print(globals())
# 实例命名空间
assert stu1.__dict__ == {'name': '张三', 'age': 16, 'grade': '大一'}
assert stu2.__dict__ == {'name': '李四', 'age': 17, 'grade': '大二'}
assert stu3.__dict__ == {'name': '王五', 'age': 18, 'grade': '大三'}

# 类命名空间
print(Student.__dict__)
