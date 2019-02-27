
# 【1】===函数的创建和使用====
# 1.普通函数的创建和使用
def func():
    print("函数func()被调用。。。。");
    pass
# 函数的调用
func();
# 2.函数的传值
def func_01(a):
    print("函数传值：%d"%a)
    pass
func_01(1000)
print("======函数的传值 :两个值========")
def func_02(a,b):
    print("函数传值：%d，日期：%s"%(a,b))
    pass
func_02(1000,"2019年2月27日")
# 3.直接赋值-带有默认值
def func_03(name = "李白",age = 18):
    print("英雄名称：%s,年龄：%d"%(name,age))
    pass
func_03()
func_03("宫本武藏")
func_03(name="狄仁杰",age=1000)
#4.带返回值的函数
def func_04(a,b):
    c = a+b;
    return c
    pass
print(func_04(2,6))
print(func_03())

