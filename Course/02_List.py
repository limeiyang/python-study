# Python中的数据结构
# 【1】=====序列=====
# Python中最基础的数据结构就是序列
# 序列中的所有元素都可以通过下标或者索引进行提取；从0开始
# 【2】====索引===
# 序列提取用中括号
s1 = "武汉工程大学Python实训课程！";
print(s1[1])
# 在Python中，根据当前的序列双向定义索引：正向从0开始，反向从-1开始
print(s1[-1]);
print(s1[6],s1[-11]);
# 【3】====分片====
s2 = "武汉工程大学Python实训课程！";
# 字符串分片提取：使用所有访问每一个元素，
# 两个索引实现分片效果，中间用":"进行分割，数据提取包前不包后[0:5)
print(s2[0:6])
# 反向下标提取:也需要根据数据左右顺序进行前后写入下标
print(s2[-5:])
# 【4】===集合的分片处理====
number01 = [1,2,3,4,5,6,7,8,9,0];
print(number01[0:5]);
print(number01[-3:-1]);
print(number01[3:])
print(number01[:])
# 更长的分片提取
print(number01[0:9:3])
# 【5】=====序列的相加======
print("千锋教育"+"Python课程");
print([1,2,3]+[4,5,6]);
# print("千锋教育"+[1,2,3]);
# x序列相加：需要两个相同数据结构的序列才能继续操作;
# 测试
print([1,2,3]*5);
# 【6】====in 用法 -  成员资格====
s3 = "2019年2月26日武汉工程大学Python实训课程！"
# 返回两个参数：True False
print("武汉工程大学" in s3);
print("武汉学" in s3);
if "Python" in s3:
    print("包含Python字段");
    pass
else:
    print("不包含。。。");
    pass
# 输入语句 - 获取到的数据类型 = 字符串类型
name_01 = input("请输入您要查找的内容：\n");
print(type(name_01));
if name_01 in s3:
    print("存在")
    pass
else:
    print("不存在。。。")
    pass
# 【7】===序列的长度 - 大小
number02 = [1,2,3,4,5,6,7,8,9,0]
# len(序列)
print(len(number02));
# 序列最大值
print(max(number02));
print(min(number02));
ab = "qwertyuiop"
print(max(ab))
# 【8】===序列的基本操作===
# 01.序列的改变--赋值
x = ["跳一跳","消灭病毒","斗地主","欢乐麻将"];
print(x[0])
x[0] = "绝地求生";
print(x)
# 删除一个元素
del x[0]
print(x)
# 扩展
x1 = ["跳一跳","消灭病毒","斗地主","欢乐麻将"];
x1[0:2] = ["篮球","炸金花"];
print(x1)
# 通过分片形式删除
del x1[1:3];
print(x1)
# 添加一个元素
x2 = ["跳一跳","消灭病毒","斗地主","欢乐麻将","斗地主"];
x2.append("狼人杀");
print(x2)
# 插入数据
x2.insert(0,"欢乐狼人杀");
print(x2);
# 查询元素在列表中出现的次数
print(x2.count("斗地主"))
# 根据元素名称删除一个元素
x2.remove("跳一跳")
print(x2)
# 添加一个序列
x3 = ["跳一跳","欢乐麻将","斗地主"];
x4 = ["明星大作战","不服来挑战"]
print("=========2019年2月26日 16:30:05=========")
print(x3+x4)
print(x3)
x3.extend(x4)
print(x3)
# 删除元素下标进行删除:pop函数调用返回要删除的元素
print(x3.pop(0))
print(x3)
# 对序列的排序
number03 = [7,4,6,3,1,9,0];
# sort排序：从小到大排序
number03.sort();
print(number03)




