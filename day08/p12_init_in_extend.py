class A:

    def __init__(self, name):
        self.name = name
        self.Q()

    def Q(self):
        print(self.name, 'Q方法被调用')


class B(A):
    pass


b = B('张三')
b.Q()


class C(A):

    def __init__(self, name):
        self.name = name


c = C('赵六')
c.Q()


class D(A):

    def __init__(self, name):
        super(D, self).__init__('李四')
        self.name = name


d = D('王五')
d.Q()
