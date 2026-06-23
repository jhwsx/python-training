"""
字符串 %格式化

格式化符号：
%s      格式化为字符串，适用于任何对象
%d、%i  格式化为整数，仅适用于数字
%f、%F  格式化为浮点数，默认精确到小数点后六位，仅适用于数字
"""
name = input("请输入您的名字: ")
height = float(input("请输入您的身高(m): "))
weight = float(input("请输入您的体重(kg): "))

bmi = weight / height ** 2
print("%s, 您好! \n您的身高是: %fm\n您的体重是: %fkg\n您的 BMI 为: %.2f" % (name, height, weight, bmi))
# 分开理解
s = "%s, 您好! \n您的身高是: %fm\n您的体重是: %fkg\n您的 BMI 为: %.2f"
new_s = s % (name, height, weight, bmi)
print(new_s)
