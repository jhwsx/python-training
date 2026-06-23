"""
字符串 format 方法格式化 2.x 就有的

方法是放置在类中的函数
"""
name = input("请输入您的名字: ")
height = float(input("请输入您的身高(m): "))
weight = float(input("请输入您的体重(kg): "))

bmi = weight / height ** 2
print("{}, 您好! \n您的身高是: {}m\n您的体重是: {}kg\n您的 BMI 为: {}".format(name, height, weight, bmi))
# 指定下标
print("{2}, 您好! \n您的身高是: {0}m\n您的体重是: {1}kg\n您的 BMI 为: {3}".format(height, weight, name, bmi))
# 指定关键字参数
print("{n}, 您好! \n您的身高是: {h}m\n您的体重是: {w}kg\n您的 BMI 为: {b}".format(h=height, w=weight, n=name, b=bmi))
# 精确位数
print("{}, 您好! \n您的身高是: {:.2f}m\n您的体重是: {:.1f}kg\n您的 BMI 为: {:.2f}".format(name, height, weight, bmi))
print("{n}, 您好! \n您的身高是: {h:.2f}m\n您的体重是: {w:.1f}kg\n您的 BMI 为: {b:.2f}".format(h=height, w=weight, n=name, b=bmi))

"""
f-string 格式化 3.6 新增- 推荐的方式
"""
print(f'{name}, 您好! \n您的身高是: {height}m\n您的体重是: {weight}kg\n您的 BMI 为: {bmi}')
print(f'{name}, 您好! \n您的身高是: {height:.2f}m\n您的体重是: {weight:.1f}kg\n您的 BMI 为: {bmi:.2f}')
