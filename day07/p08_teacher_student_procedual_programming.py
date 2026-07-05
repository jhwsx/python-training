def get_up(name):
    print(f'{name}睁开眼睛')
    print(f'{name}起身')
    print(f'{name}穿好衣服')

def wash(name):
    print(f'{name}刷牙')
    print(f'{name}洗脸')

def eat(name):
    print(f'{name}吃菜')
    print(f'{name}扒饭')

def login(name):
    print(f'{name}输入账号密码')
    print(f'{name}登录成功')

def study(name):
    print(f'{name}看视频')
    print(f'{name}查资料')
    print(f'{name}写代码')

def sleep(name):
    print(f'{name}脱掉外套')
    print(f'{name}躺下')
    print(f'{name}闭眼')

def show(name, age, grade):
    print(f'大家好，我叫{name}, 今年{age}岁，目前读{grade}')

count_stu = 0
name1 = '张三'
age1 = 16
grade1 = '大一'

show(name1, age1, grade1)
count_stu += 1
get_up(name1)
wash(name1)
eat(name1)
login(name1)
study(name1)
eat(name1)
study(name1)
eat(name1)
sleep(name1)


name2 = '李四'
age2 = 17
grade2 = '大二'

show(name2, age2, grade2)
count_stu += 1
get_up(name2)
wash(name2)
eat(name2)
login(name2)
study(name2)
eat(name2)
study(name2)
eat(name2)
sleep(name2)


name3 = '王五'
age3 = 18
grade3 = '大三'

show(name3, age3, grade3)
count_stu += 1
get_up(name3)
wash(name3)
eat(name3)
login(name3)
study(name3)
eat(name3)
study(name3)
eat(name3)
sleep(name3)

print(f'当前学生人数为{count_stu}')
