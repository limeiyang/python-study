#coding=utf-8
# 在Python2.x版本中，不支持中文显示，需要添加#coding=utf-8

# 【1】===注释方式====
#  单行数值  Ctrl+/
"""
多行注释
"""
'''
多行注释
'''
# 【2】====输出语句====
# 一条语句结束之后可以不添加分号
print("2019年2月25日 武汉工程大学Python实训班");
# python 2.x中的输出语法
# print "2019年2月25日 武汉工程大学Python实训班"
# 【3】====变量=====
# python是动态属性的语言，前面不需要添加数据类型,数据类型在被赋值的时候定义
a1 = 1;
print(type(a1))
s1 = "武汉工程大学Python实训班";
print(type(s1));
a2 = 1.1
print(type(a2));
# 输出语句多个输出,数据之前用逗号分隔
print(a1,s1,a2)
#【4】===运算符====
"""
+ - * / %
"""
print(4+2)
print(4-2)
# 【注意】"/"运算中，两个整数相除，会保获取一个浮点型的一位小数
print(4/2)
# 【注意】在两个整数相除，除不尽情况，会保留一个四舍五入16位小数
print(5/3)
#  "//"双除号；在运算中只会保留整数部分，舍去小数部分
print(5//3)
# 浮动性数据进行运算的时候
print(5.0/3)
# 浮点型数据在除不尽的情况下，会保留原浮点型小数位数，用0代替；
print(5.0//3);
# "**"表示乘方 5的3次方
print(5**3);
print("***"*10);
# 练习：取余
# 【5】====比较运算符====
# 常规比较运算
print(4<5)
print(4<=5)
# python中支持连续比较运算
"""
if(4<a&&4<9){

}
"""
# 声明一个变量 a3
a3 = 5
if 4<a3<9:
    print("正常输出。。。")
    pass #占位符
else:
    print("错误输出。。。")
    pass

if 4<a3<9:
    print("人坐了了座位上，书包没有用了");
    pass
elif a3<8:
    pass
else:
    pass




























