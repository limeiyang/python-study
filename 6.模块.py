#!/usr/bin/python

# 1. sys模块
import sys
print("您输入的命令为:")
for i in sys.argv:
    print(i)
print(sys.path)
'''
运行结果:

PS D:\工作文件\程序代码\python_demo> python 6.模块.py hello world
您输入的命令为:
6.模块.py
hello
world
['D:\\工作文件\\程序代码\\python_demo', 'D:\\Python 3.7.0\\python37.zip',
 'D:\\Python 3.7.0\\DLLs', 'D:\\Python 3.7.0\\lib', 'D:\\Python 3.7.0'
 ......]
'''

# 2. 字节编译的.pyc文件
'''
在说这个问题之前，我们先来说两个概念，PyCodeObject和pyc文件。
我们在硬盘上看到的pyc自然不必多说，而其实PyCodeObject则是Python编译器
真正编译成的结果。我们先简单知道就可以了，继续向下看。
当python程序运行时，编译的结果则是保存在位于内存中的PyCodeObject中，
当Python程序运行结束时，Python解释器则将PyCodeObject写回到pyc文件中。
当python程序第二次运行时，首先程序会在硬盘中寻找pyc文件，如果找到，
先对.pyc文件和.py文件的最近一次的修改时间进行判断，如果.pyc文件的修改时间晚于.py文件，
说明.py文件中的源代码未修改过，则直接载入，否则就重复上面的过程。
所以我们应该这样来定位PyCodeObject和pyc文件，我们说pyc文件其实是PyCodeObject的一种持久化保存方式。
'''

# 3. from import 语句
'''
form sys import argv
就可以直接使用argv，而不用sys.argv
for sys import *
可直接使用sys里面的所有模块

注：多使用inport sys 
    可以使得程序更加易懂解读
'''

# 4. 模块的 __name__
'''
每个模块都有一个名称，在模块中可以通过语句来找出模块的名称。这在一个场合特别有用
——就如前面所提到的，当一个模块被第一次输入的时候，这个模块的主块将被运行。假如我
们只想在程序本身被使用的时候运行主块，而在它被别的模块输入的时候不运行主块，我们该
怎么做呢？这可以通过模块的__name__属性完成。
'''
if __name__ == '__main__':
    print("This program is being run by itself")
else:
    print("I am being imported from another module")
'''
运行结果：

$ python 6.模块.py
This program is being run by itself

$ python
>>> import 6.模块
I am being imported from another module
>>>
'''

# 5. 创建自己的模块
# modelfile.py
def mymodel():
    print("i am a model (love jiaxin)")
version = '1.0'

'''
在另一个文件中导入此模块
import modelfile
modelfile.mymodel()
print("version:",modelfile.version)

也可以另一种导入方法
from modelfile import mymodel,version
mymodel()
print("version:",version)
运行得到输出:
i am a model (love jiaxin)
version:1.0
'''

# 6. dir() 函数
'''
你可以使用内建的dir函数来列出模块定义的标识符。标识符有函数、类和变量。
当你为dir()提供一个模块名的时候，它返回模块定义的名称列表。如果不提供参数，它返回当
前模块中定义的名称列表。
例如：
import sys
dir(sys)

输出：
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__stderr__']

dir的一些其他输出
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'sys']
>>>
>>> del a # delete/remove a name
>>>
>>> dir()
['__builtins__', '__doc__', '__name__', 'sys']
>>
'''