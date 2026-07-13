"""
查找路径:

先在当前目录找, 找到则结束
再在项目根目录找, 找到则结束
再在内置目录找（在Anaconda里面的目录里面找）, 找到则结束
还找不到则报错
"""
import sys
import package1.subpackage1.subpackage2
print(sys.path)

# import subpackage2  # ModuleNotFoundError: No module named 'subpackage2'

print(globals())
