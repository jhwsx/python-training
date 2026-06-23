# 什么是编程语言

编程语言是人类与计算机沟通的桥梁，是一种通过特定语法规则组合而成的形式化语言，用于向计算机传递指令。



# 编程语言发展历程

编程语言经历了3个主要阶段：机器语言、汇编语言、高级语言

**机器语言**：用二进制编码表示的机器指令，是CPU能直接识别并执行的唯一一种语言。

**汇编语言**：符号语言。用与机器指令含义相近的英文缩写、字母和数字等符号来替代机器指令。

**高级语言**：机器语言和汇编语言都是面向机器（硬件）的语言，占用内存少，执行速度快，但用起来繁琐费时，可移植性差；而高级语言是面向用户的语言，更接近人类的自然语言，且无论何平台，只要配备上相应的高级语言的编译或解释程序，就可以实现通用。



# 两种核心翻译机制

计算机只能直接识别并执行机器语言，所以需要把高级语言翻译为机器能执行的形式，编译与解释就是两种核心翻译机制：

**编译方式**：源代码文件经过编译器翻译成目标程序文件，然后计算机再执行该目标程序。

**解释方式**：源代码文件经过解释器逐句读取，逐句翻译，逐句执行，并不产生目标程序文件。



# Python是什么样的语言

Python是Guido van Rossum（吉多·范罗苏姆，荷兰籍计算机科学家）在1989年圣诞节期间为了打发无聊的圣诞节而开发的一种简单优雅的编程语言。保守估计，目前世界上已知的编程语言超过了800种，但真正流行的编程语言也就那么几种。TIOBE 排行榜（每月初更新）很好的反映了各种编程语言的热门程度。

TIOBE 排行榜：https://www.tiobe.com/tiobe-index/

![](Files/TIOBE.png)



# Python环境搭建

**安装Python**

- 官方宣布，2020年1月1日，停止Python2的更新，Python2.7被确定为最后一个Python2.x 版本。Python3和Python2是有差别的，现在学习Python，通常选择Python 3.x版本。

- 可以通过Anaconda搭建环境，Anaconda包含了conda、Python以及一大堆安装好的工具包，这样会比直接安装Python，再去手动安装一堆的工具包更方便。

- anaconda官方下载地址：https://repo.anaconda.com/archive/

- anaconda清华镜像下载地址：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

**安装IDE**

- 安装好Python之后其实就可以编写代码了，但通常我们还是会选择在IDE（集成开发环境）中编写代码，因为 IDE 集成了代码编写功能、编译功能、分析功能、调试功能等一体化的服务，可以显著提高工作效率、降低错误率。
- 主流的Python IDE有：PyCharm、VSCode、Jupyter、Spyder、WingIDE等
- PyCharm（windows）下载地址：https://download.jetbrains.com/python/pycharm-community-2024.1.5.exe
- PyCharm（mac）下载地址：https://download.jetbrains.com/python/pycharm-community-2024.1.5-aarch64.dmg

