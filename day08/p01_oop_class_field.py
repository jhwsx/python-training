# object 类是所有类的父类
# 所有类默认集成 object 类
class Student(object):
    # 类属性
    school = 'hpu'
    # Student.school2 = 'hpu'  # Error

    # 方法：定义在类中的函数
    # 魔术方法(特殊方法)：官方定义好的，以 __ 开头和结尾的方法
    # 魔术方法特点：通常不需要主动调用，在特定情况下会被自动触发
    def __init__(self, name, age, grade):  # 这里覆盖了 object 类中的 __init__ 方法
        # 实例属性
        self.name = name
        self.age = age
        self.grade = grade
        print(locals())


print(Student)
"""
__new__: 该魔术方法在实例化时被自动触发, 并返回实例化对象，这是构造方法
__init__: 该魔术方法也在实例化时被自动触发, 用来对实例化对象进行属性定制，这是初始化方法
    1.每次实例化时，会先自动调用 __new__(cls, *args, **kwargs)方法, 把要实例化的类对象传递给 cls 参数
    2.__new__ 方法根据 cls 创建对应的裸的实例化对象，
    3.接着还会调用 __init__ 方法, 把裸的实例化对象传递给 self 参数
    4.__init__ 方法对接收到的裸的实例化对象做属性定制操作（增加属性, 是原地操作）, 这个方法没有返回值
    4.__new_方法返回该实例化对象
"""
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
