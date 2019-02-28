
# 【1】===字典的创建和使用====
# Python字典：键值对形式出现
dic01 = {"001":"王宝强","002":"黄渤","003":"孙耀威"}
# 通过key提取value
print(dic01["002"]);
# 【2】将一个序列转换成字典的格式:序列中一个元素的格式：("name","张云雷")
items = [("name","张云雷"),("age","18")]
items.append(("phone","18000"))
print(items)
dic_02 = dict(items);
print(dic_02);
# 【3】===直接生产一个字典===
dic_03 = dict(name = "孟鹤堂",age = "16");
print(dic_03)
# 扩展 - 使用成员资格
print("age" in  dic_03);
# 【4】===删除一个键值对的数据====
# 删除整个对于项
del dic_03["age"]
print(dic_03);
dic01 = {"001":["fdsf"],"002":["fdsf"],"003":["fdsf"]}
print(dic01)
#Key值：可以允许：String类型，整型，浮点型，序列
# value值：没有限制
# 【4】===清空字典====
dic01.clear()
print(dic01,dic01.clear())





