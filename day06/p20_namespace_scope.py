import builtins
import math
import random


def fun1(x, y):
    num = 666
    print(locals())


def fun2(x, y):
    num = 777
    print(locals())


num = 789
fun1(1, 2)
fun1(3, 4)
print(globals())
