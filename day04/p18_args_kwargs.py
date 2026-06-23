"""
不定长参数
*args: 可以接收0到无数个位置参数，贪婪的，将它接收到的参数打包成元组，如果没有参数，则打包成空元组
       该形参的位置没有限制
**kwargs: 可以接收0到无数个关键字参数 ，贪婪的，将它接收到的参数打包成字典，如果没有参数，则打包成空字典
          该形参必须放在所有形参的最后
"""


def f(*args, **kwargs):
    print(args)
    print(kwargs)
    assert type(args).__name__ == 'tuple'
    assert type(kwargs).__name__ == 'dict'


f()
f(1, 2, name='Tom', age=18, height=178)

# def g(**kwargs, *args):  # SyntaxError: invalid syntax
#     pass
