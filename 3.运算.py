# 打印格式
num1='limeiyang'
num2='python'
num3=100
print(num1,num2,num3)
print(num1,num2,num3,sep='中间间隔')

# 默认的print会带有换行，用end控制
print(num1,num2,num3,end=' ') # 给end一个空格
print('这一行会跟着上面那一行的')

# 输出到文件
str01='我想要输出到TXT文件中'
my_file01 = open('D:\savepy.txt','w') # write: 写入
print(str01,file=my_file01)

# 格式化输出--------
'''
%c 字符
%s 通过str()字符串转换来格式化
%i 有符号的十进制整数 
%d 有符号的十进制整数
%u 无符号的十进制整数
%o 八进制整数
%x（%X）十六进制整数
%e（%E）索引符号 科学计数法
%f 浮点实数
%g（%G） %f和%e的简写（可以表示用小数（6位有效数字），不然用科学计数法）
'''
num4 = 200
print("十进制输出 %d" % num4)
print("十六进制输出 %x" % num4)
print("八进制输出 %o" % num4)
print("八进制输出",bin(num4))

# 放到一行
print("十进制输出 %d 十六进制输出 %x 八进制输出 %o" %(num4,num4,num4))

# 浮点数
num5=3.141592657
print("保留两位小数",round(num5,2)) #如果小于2个小数，不会补0 如3.00
print("保留两位小数 %.2f" % num5) #会补0

'''
 /   除数，保留小数
 //  除数，保留整数
 **  求幂，a的b次方
'''

# 逻辑运算符
# and or not 而不是符号
print(True and False)
print(True or False)

# 成员运算符
# in / not in
# 场景一：判断一个字符串中是否包含另一个字符串
str02 = "my name is limeiyang"
if 'name' in str02 :
    print("包含")
else:
    print("不包含")

# 场景二：判断集合中是否包含某一个元素
list01 = [111,222,333,444,555]
if 111 in list01:
    print("baohan")
else:
    print("bubaohan")

# 身份运算符
# is / not is 判断两个对象是否引用同一内存空间
num6 = 100
num7 = 100
print("num6和num7是否相等" , num6 == num7)
print("num6和num7是否相等" , num6 is num7)
str03 = 'home'
str04 = 'home'
print("str03和str04是否相等",str03 == str04)
print("str03和str04是否相等",str03 is str04)
# 反例 (存很大字符串时地址不同)
str05 = "home"*100
str06 = "home"*100
print("str05和str06是否相等",str05 == str06)
print(id(str05))
print(id(str06))
print("str05和str06是否相等",str05 is str06)

# 三元运算符
num8 = 100
num9 = 200
num10 = num8 if num8 > num9 else num9
print(num10)