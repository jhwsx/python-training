"""
题目: 请设计一个学生管理系统, 包含一下内容:

1. 学生类(Student):
   - 包括属性: 学生姓名(name)、学生年龄(age)、学生成绩(score)
   - 包括功能:
     - 获取学生信息(get_info): 返回该学生的姓名、年龄和成绩。

2. 班级类(ClassRoom):
   - 包括属性: 班级名称(name)、班级学生列表(students)、所有班级列表(classes)
   - 包括功能:
     - 添加学生(add_student): 将学生对象添加到指定班级的学生列表中, 如果该学生已经在指定班级中则无需重复添加, 如果该学生在其它班则调班。
     - 移除学生(remove_student): 将学生对象从指定班级的学生列表中移除, 如果该学生不在指定班级则无需移除。
     - 获取指定班级的学生信息(get_students_info): 输出指定班级的所有学生信息, 如果没有指定班级, 则默认输出所有班级的所有学生信息。

要求:
1. 实现上述内容。
2. 编写相关测试代码。
"""


class Student:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def __repr__(self):
        return f'姓名:{self.__name},年龄:{self.__age},成绩:{self.__score}'

    def get_info(self):
        return self.__repr__()


class ClassRoom:

    __classes = []

    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_student(self, student):
        # 查看该学生是否在其他班, 在则移除
        for cls in ClassRoom.__classes:
            if cls is not self and cls.__students.count(student) > 0:
                cls.remove_student(student)

        # 把该学生放到指定的班级
        if self.__students.count(student) <= 0:
            self.__students.append(student)

        # 把班级放到班级列表中
        if ClassRoom.__classes.count(self) <= 0:
            ClassRoom.__classes.append(self)

    def remove_student(self, student):
        # 在指定的班，则移除
        if self.__students.count(student) > 0:
            self.__students.remove(student)

        # 班里没学生了
        if len(self.__students) == 0:
            ClassRoom.__classes.remove(self)  # 撤销班级

    def __repr__(self):
        return f'班级:{self.__name}, 学生:{self.__students}'

    @staticmethod
    def get_students_info(class_name=None):
        # 遍历班级列表
        for cls in ClassRoom.__classes:
            if class_name == cls.__name:
                return cls
        return ClassRoom.__classes


# 组建一班
stu1 = Student('张三', 18, 100)
print(stu1.get_info())
stu2 = Student('李四', 19, 120)
print(stu2.get_info())

cr1 = ClassRoom('一班')
cr1.add_student(stu1)
cr1.add_student(stu2)
cr1.add_student(stu2)

print(ClassRoom.get_students_info('一班'))

# 组建二班
stua = Student('Peter', 18, 99)
print(stua.get_info())
stub = Student('Tom', 19, 98)
print(stub.get_info())
stuc = Student('John', 20, 97)
print(stuc.get_info())

cr2 = ClassRoom('二班')
cr2.add_student(stua)
cr2.add_student(stub)
cr2.add_student(stuc)
print(ClassRoom.get_students_info('二班'))

# 二班，John 离开
cr2.remove_student(stuc)
cr2.remove_student(stuc)
print(ClassRoom.get_students_info('二班'))

# 二班的 Tom 转到一班
cr1.add_student(stub)
print(ClassRoom.get_students_info('一班'))
print(ClassRoom.get_students_info('二班'))

# 二班的 Peter 转到一班
cr1.add_student(stua)
print(ClassRoom.get_students_info('一班'))
print(ClassRoom.get_students_info('二班'))

print(ClassRoom.get_students_info())

