"""
多态
- 多态性是指具有不同内容的方法可以使用相同的方法名，则可以用一个方法名调用不同内容的方法
"""

class Apple:
    @staticmethod
    def change():
        print('变成苹果汁')


class Banana:
    @staticmethod
    def change():
        print('变成香蕉汁')


class Mango:
    @staticmethod
    def change():
        print('变成芒果汁')


class Juicer:
    @staticmethod
    def work(fruit):
        fruit.change()


Juicer.work(Apple)
Juicer.work(Banana)
Juicer.work(Mango)
