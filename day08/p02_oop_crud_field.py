class Student(object):
    # 类属性
    school = 'hpu'
    # Student.school2 = 'hpu'  # NameError: name 'Student' is not defined

    def __init__(self, name, age, grade):  # 这里覆盖了 object 类中的 __init__ 方法
        # 实例属性
        self.name = name
        self.age = age
        self.grade = grade
        # print(locals())


stu1 = Student('张三', 16, '大一')  # 实例化
stu2 = Student('李四', 17, '大二')
stu3 = Student('王五', 18, '大三')
# print(globals())
# 访问实例属性
assert stu1.name == '张三'
assert stu2.age == 17
assert stu3.grade == '大三'
# 获取属性的方法
# getattr(object, name[,default])
# 返回 object 对象(实例对象或者类对象)的 name 属性值（name参数为字符串）
# 如果 name 属性不存在，且提供了 default 值，则返回 default 值；否则，触发 AttributeError
assert getattr(stu1, 'name') == '张三'
assert getattr(stu2, 'age') == 17
assert getattr(stu3, 'grade') == '大三'
# getattr(stu1, 'whatthefuck')  # AttributeError: 'Student' object has no attribute 'whatthefuck'
assert getattr(stu1, 'blabla', 10086) == 10086
assert getattr(Student, 'school') == 'hpu'
# 访问类属性
# 实例对象间接访问类属性(先查找实例属性，再查找类属性)
assert stu3.school == 'hpu'
# 类直接访问类属性（推荐）
assert Student.school == 'hpu'

"""
修改实例属性
"""
stu1.age = 24
assert stu1.age == 24
"""
修改类属性, 只能用类
"""
Student.school = 'zu'
assert Student.school == 'zu'

"""
增加类属性(动态定义类属性)
"""
Student.state = 'china'
assert Student.state == 'china'

"""
增加实例属性(动态定义实例属性)
"""
stu1.school = 'hu'
assert stu1.school == 'hu'
assert Student.school == 'zu'

"""
setattr(object, name, value)
将 object 的 name 属性设置为 value，属性不存在则新增属性（name 参数为字符串）
"""
setattr(stu1, 'gender', 'M')  # 新增
assert getattr(stu1, 'gender') == 'M'
setattr(stu1, 'age', 20)  # 修改
assert stu1.age == 20
setattr(Student, 'province', 'henan')  # 新增
assert getattr(Student, 'province') == 'henan'
setattr(Student, 'school', 'jit')
assert Student.school == 'jit'

"""
删除属性
"""
del stu1.name, stu1.age, Student.state
delattr(stu1, 'gender')
delattr(Student, 'province')

"""
判断有无属性
hasattr(object, name)
判断 object 对象是否包含 name 属性（name 参数为字符串）
此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的
"""
assert not hasattr(stu1, 'gender')
assert hasattr(stu1, 'grade')
assert hasattr(Student, 'school')
