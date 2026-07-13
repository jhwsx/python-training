"""
包的作用：
1. 划分模块
2. 避免命名冲突
"""
import package1
import package2
import numpy
# 当包第一次被导入时，若包里面有 __init__.py，则会先执行该文件(pandas, numpy 包都是这样的)
print(package2.__version__)
print(numpy.__version__)
