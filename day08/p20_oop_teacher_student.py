class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.show()

    def get_up(self):
        print(f'{self.name}睁开眼睛')
        print(f'{self.name}起身')
        print(f'{self.name}穿好衣服')

    def wash(self):
        print(f'{self.name}刷牙')
        print(f'{self.name}洗脸')

    def eat(self):
        print(f'{self.name}吃菜')
        print(f'{self.name}扒饭')

    def sleep(self):
        print(f'{self.name}脱掉外套')
        print(f'{self.name}躺下')
        print(f'{self.name}闭眼')

    def show(self):
        pass


class Student(Person):

    __count_stu = 0

    def __init__(self, name, age, grade):
        self.grade = grade
        super().__init__(name, age)
        Student.__count_stu += 1

    def login(self):
        print(f'{self.name}输入账号密码')
        print(f'{self.name}登录成功')

    def study(self):
        print(f'{self.name}看视频')
        print(f'{self.name}查资料')
        print(f'{self.name}写代码')

    def show(self):
        print(f'大家好，我叫{self.name}, 今年{self.age}岁，目前读{self.grade}')

    @classmethod
    def show_count(cls):
        print(f'当前学生人数为{cls.__count_stu}')


stu1 = Student('张三', 16, '大一')
stu2 = Student('李四', 17, '大二')
stu3 = Student('王五', 18, '大三')
Student.show_count()


class Teacher(Person):

    __count_teacher = 0

    def __init__(self, name, age, department):
        self.department = department
        super().__init__(name, age)
        Teacher.__count_teacher += 1

    def clockin(self):
        print(f'{self.name}录入指纹')
        print(f'{self.name}打卡成功')

    def work(self):
        print(f'{self.name}授课')
        print(f'{self.name}答疑')
        print(f'{self.name}写代码')

    def show(self):
        print(f'大家好，我叫{self.name}, 今年{self.age}岁，目前在{self.department}部门工作')

    @classmethod
    def show_count(cls):
        print(f'当前老师人数为{cls.__count_teacher}')


t1 = Teacher('Tom', 35, 'AI1')
t2 = Teacher('John', 36, 'AI2')
t3 = Teacher('Peter', 37, 'AI3')
Teacher.show_count()

