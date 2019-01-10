#!/usr/bin/python
# 以上的以#！开头的固定格式，如果本文件命名没有指明格式，则系统会以此来判断用python来执行

print("1.---------------------")
# 1. 定义sayhello函数
def sayhello(a):
    print("hello函数",a)
sayhello(100) # 调用

print("2.---------------------")
# 2. 全局变量 global
def fun01():
    global x
    x = 2
    y = 2
    print("函数中的全局变量X", x)
    print("函数中的变量y", y)
x = 50
y = 50
fun01()
print("现在的x：", x)
print("现在的y：", y)

print("3.---------------------")
# 3. 默认形参
def fun02(num01, num02 = 2):
    print("结果是",num01 * num02)
fun02(2)
fun02(2, 5)

def fun03(a,b,c=3):
    print("a=",a,"b=",b,"c=",c)
    return 0# 返回值
fun03(1,2)
fun03(1,b=3,c=4)# 指定赋值

print("4.---------------------")
# 4. 文档字符串 DocStrings
def fun04(a):
    '''Print this Dostrings

    这是文档字符串.
    '''
    print("a=",a)
fun04(1006)
print(fun04.__doc__)