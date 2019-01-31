#!/usr/bin/python
'''
lambda:匿名函数
lambda表达式，通常是在需要一个函数，
但是又不想费神去命名一个函数的场合下使用，
也就是指匿名函数。

lambda所表示的匿名函数的内容应该是很简单的，
如果复杂的话，干脆就重新定义一个函数了，使用lambda就有点过于执拗了。

lambda就是用来定义一个匿名函数的，
如果还要给他绑定一个名字的话，就会显得有点画蛇添足，
通常是直接使用lambda函数。如下所示：

add = lambda x, y : x+y
add(1,2)  # 结果为3
'''
# 1.应用在函数式编程中
'''
Python提供了很多函数式编程的特性，如：map、reduce、filter、sorted等
这些函数都支持函数作为参数，lambda函数就可以应用在函数式编程中.
'''
# 1.1 将列表中的元素安装绝对值大小进行升序排列
list1 = [3,5,-4,-1,0,-2,-6]
list2 = sorted(list1,key = lambda x: abs(x))
print('lambda方法：',list2)


# 普通方法
def get_abs(x):
    return abs(x)
list3 = sorted(list1,key = get_abs)
print('普通方法：',list3)


# 2.应用在闭包中
def get_y(a,b):
    return lambda x:a*x+b
y1 = get_y(1, 1)
print('lambda闭包结果：', y1(1))
# 普通方法闭包
def get_y2(a, b):
    def func(x):
        return a*x+b
    return func
y2 = get_y2(1, 1)
print('普通方法闭包结果：', y2(1))

# 3. 两个参数
# 两数相加(reduce函数详见13)
from functools import reduce
print(reduce(lambda x,y: x + y, [1,2,3,4,5]))
