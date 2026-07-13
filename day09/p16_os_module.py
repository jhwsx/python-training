"""
os 模块提供了很多对目录和文件操作的函数
"""
import os

# 获取当前目录的绝对路径, 返回字符串
print(os.getcwd())

# 获取指定目录包含的文件以及目录, 返回一个以字符串为元素的列表
print(os.listdir('./'))

# 创建多级目录
# os.makedirs(name, exist_ok=False)

os.makedirs('./dir1/dir2/dir3', exist_ok=True)
try:
    os.makedirs('./dir1/dir2/dir3', exist_ok=False)
except FileExistsError as e:
    print(f'FileExistsError: {e}')
os.makedirs('./dir1/dir2/dir3', exist_ok=True)
assert os.path.exists('./dir1/dir2/dir3')

os.removedirs('./dir1/dir2/dir3')
assert not os.path.exists('./dir1/dir2/dir3')

# os.path
filepath = '/dir1/dir2/dir3/a.txt'
assert os.path.basename(filepath) == 'a.txt'
assert os.path.dirname(filepath) == '/dir1/dir2/dir3'
assert os.path.split(filepath) == ('/dir1/dir2/dir3', 'a.txt')
assert os.path.splitext(filepath) == ('/dir1/dir2/dir3/a', '.txt')

with open('empty_file.txt', 'w') as f:
    f.write("")
assert os.path.isfile('empty_file.txt')
os.remove('empty_file.txt')

p1 = 'D:\\python-training\\'
p2 = 'dir1/dir2/dir3'
p3 = '../python.py'
print(os.path.join(p1, p2, p3))
