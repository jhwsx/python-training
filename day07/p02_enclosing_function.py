"""
闭包函数需要满足三个条件：
1.嵌套函数
2.外部函数的返回值是内部函数的引用
3.内部函数用到了外部函数中定义好的名称
"""

# Enclosing 作用域：闭包函数外的函数中的区域
# 在这里 Enclosing 作用域的名称有：a, b, e
def outer(a):
    b = 700

    def inner(c):
        # 内部函数会把它用到的外部函数中的名称记录一份
        print(locals())  # {'c': 800, 'a': 500, 'b': 700, 'e': 1000}
        return a + b + c + e + g

    e = 1000
    # print(locals())
    return inner


g = 2000
f = outer(500)
print(f(800))
