"""
方法重写
- 在继承关系中，当父类的方法不能满足子类的需求时，可以在子类重写父类的该方法
"""


class Animal:
    def __init__(self, food):
        self.food = food

    def eat(self):
        print(f'动物喜欢吃{self.food}')


class Cat(Animal):
    def eat(self):
        print(f'猫喜欢吃{self.food}')


class Dog(Animal):
    def eat(self):
        print(f'狗喜欢吃{self.food}')


a = Animal('🥩')
a.eat()

c = Cat('🐟')
c.eat()

d = Dog('🍎')
d.eat()