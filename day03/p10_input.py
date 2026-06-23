"""
def input(__prompt: object = "") -> str
prompt: 提示信息, 可以是任何类型
接受控制台输入的数据，返回该数据的字符串形式
"""
ret = input("Please input something:\n")
print(ret)
print(type(ret))
