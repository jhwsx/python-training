class Student(object):
    # 类属性
    school = 'hpu'

    def __init__(self, name, age, grade):  # 这里覆盖了 object 类中的 __init__ 方法
        # 实例属性
        self.name = name
        self.age = age
        self.grade = grade


def my_hasattr(obj, name):
    try:
        getattr(obj, name)
        return True
    except AttributeError:
        return False


assert my_hasattr(Student, 'school')
assert not my_hasattr(Student, 'school2')
