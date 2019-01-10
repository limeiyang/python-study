# 长字符 (双引号和单引号一样)
str01 = "my name is limeiyang my name is limeiyang my name is limeiyang my name is limeiyang "
str02 = "my name is limeiyang " \
        "my name is limeiyang my name is limeiyang my name is limeiyang "
# 直接换行，自动加 \

str03 = """
    原格式输出
         原格式
                   哦！
"""

print("str01为", str01)
print("str02为", str02)
print("str03为", str03)

print(str01[4])
print(str01[-4])
print(str01[3:7])
print(str01[3:7:2])
# print(str01[开始:结束:步长])

# 转义字符
# D:\abc\pic.png
print("D:\abc\pic.png")
print("D:\\abc\\pic.png")
# R r 取消转移字符
print(r"D:\abc\pic.png")

# 字符串格式打印
print('================')
str04='goodword'
print("%s" % str04)
print("%10s" % str04)
print("%.2s" % str04)
print("%10.2s" % str04)
