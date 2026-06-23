"""
条件语句

格式1：
if 判断条件:
    执行代码块
"""
age = 19
if age >= 18:
    print('You are adult!')

"""
格式2：
if 判断条件:
    执行代码块1
else:
    执行代码块2
"""
age = 19
if age >= 18:
    print('You are adult!')
else:
    print('You are not adult!')

"""
格式3:
if 判定条件1:
    执行代码块1
elif 判定条件2:
    执行代码块2
elif 判定条件3:
    执行代码块3
...
else:
    执行代码块n
"""
grade = 90
if grade >= 90:
    print('很好')
    print('但是不要骄傲')
elif grade >= 80:
    print('好')
    print('但是要加油')
elif grade >= 70:
    print('还行')
    print('但是要继续努力')
else:
    print('哎')

"""
if 是必须的，elif和else 不是必须的；elif 可以有多个
"""

"""
if 嵌套
"""
age = 25
has_license = True
if age >= 18:
    if has_license:
        print('可以驾驶车子')
    else:
        print('缺少驾照，不可以驾驶车子')
else:
    print('年龄不够，不可以驾驶车子')
