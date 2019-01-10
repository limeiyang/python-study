# 单独定义变量
num01 = 1
num02 = 3.14
num03 = False
str01 = "www.baidu.com"

# 多个变量赋值
num04 = num05 = num06 = 4

# 一次定义多个
num07, num08, num09 = 1, 2, 3

print("num08 是",num08)


# 数据类型
print(1+2)
print("1+80")
print(True)
print("hello", "world")
print("hello" + "world")

num1 = 100
num2 = -99.25
num3 = (100>722)
str1 = "world"

print(type(num1))
print(type(num2))
print(type(num3))
print(type(str1))

# 内存地址
num1=100
num2=200
num3=100
print('num1',id(num1))
print('num2',id(num2))
print('num3',id(num3))
# 发现num1和num3地址一样，python相同的值只存一份

