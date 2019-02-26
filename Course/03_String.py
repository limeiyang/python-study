
# 【1】=====字符串的格式化========
# %d表示数字 %s表示文本
format01 = "请注意，欢迎来%d号机器，来自%s的%s来本网咖上网，奖励%d小时免费游玩！！"
# 使用模板
print(format01%(21,"诺克萨斯","最强王者",100));
# 表示小数：%.3f ;
format02 = "狄仁杰,今年%d岁，体重：%.3f公斤"
print(format02%(400,40.23));
# 【2】====find()函数====
s1 = "请注意，欢迎来21号机器，注意，来自诺克萨斯的最强王者来本网咖上网，奖励100小时免费游玩！！"
# find函数，如果能够找到的情况下，返回从起点开始匹配到的元素下标，如果找不到返回-1
print(s1.find("注意"));
print(s1.find("QQ"))
#  防守对方的束缚对方[诺克萨斯]第三方的身份的说法
# 查找一个区间内是否有对应元素：
# 第一个参数：要匹配的元素字符串，第二个：开始查询的区间下标，第三个：结束查询的区间下标
print(s1.find("注意",3,20))
# 两个参数：第二个数值参数表示开始下标；
print(s1.find("注意",3))
# 【3】===join===做数组元素拼接
# 该方法：将数组中的元素提取拼接成字符串格式；
# 可以在两个元素中间插入文本
a1 = ["狄仁杰","曹操","李白","后羿"];
print("---".join(a1))
# 【4】大小写转换
print("Hello Python ".lower()); # 转换成小写
print("Hello Python".upper())# 转换成大写
# 判断大小写
print("H".isupper())
print("H".islower())
# 【5】===字符串替换====
print("请注意，诺克斯撒欢迎来21号机器，注意，来自诺克斯撒的最强王".replace("诺克斯撒","诺克萨斯"));
# 【6】===去除一个字符串的前后空格
print("    武汉工程大学Python实训     ")
print("    武汉工程大    学Python实训     ".replace(" ","").strip())





