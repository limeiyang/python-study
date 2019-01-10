#!/usr/bin/python
# 异常处理
'''
我们可以使用try..except语句来处理异常。我们把通常的语句放在try-块中，而把我们的错误处
理语句放在except-块中。
'''
import sys
try:
    s = input('Enter something --> ')
except EOFError:# 点击 ctrl+d 激活此报错
    print('\nWhy did you do an EOF on me?')
    sys.exit() # exit the program
except:# 其他错误
    print('\nSome error/exception occurred.')
    # here, we are not exiting the program
print('Done')

# 引发异常
'''
这里，我们创建了我们自己的异常类型，其实我们可以使用任何预定义的异常/错误。这个新
的异常类型是ShortInputException类。它有两个域——length是给定输入的长度，atleast则是程序
期望的最小长度。
在except从句中，我们提供了错误类和用来表示错误/异常对象的变量。这与函数调用中的形参
和实参概念类似。在这个特别的except从句中，我们使用异常对象的length和atleast域来为用户
打印一个恰当的消息。
'''
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    s = input('Enter something --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
# Other work can continue as usual here
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException as x:
    print('ShortInputException: The input was of length %d,was expecting at least %d' % (x.length, x.atleast))
else:
    print('No exception was raised.')

# try finally
'''
假如你在读一个文件的时候，希望在无论异常发生与否的情况下都关闭文件，该怎么做呢？这
可以使用finally块来完成。注意，在一个try块下，你可以同时使用except从句和finally块。如果
你要同时使用它们的话，需要把一个嵌入另外一个。
使用finally
'''
import time
try:
    f = open('poem.txt')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line)
finally:
    f.close()
    print('Cleaning up...closed the file')