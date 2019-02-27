
# 【1】===赋值操作===
a = 1;
b = 2;
# 【2】===序列解包赋值===
x,y,z = "上路","下路","中单";
print(x,y,z)
# 两个变量值进行交换
x,z = z,x
print(x,y,z)
# 【3】===条件语句====
# if elif ... celse
# 判断首位字符做对比
# name = input("请输入要查询的英雄：\n");
# # startswith 从开始0下标进行匹配，直至匹配到对应元素（狄仁）结束
# if name.startswith("狄仁"):
#     print("您查询的英雄为狄仁杰。。。。");
#     pass
# else:
#     pass

# 【3】=========嵌套if判断==========
# 1.先选择英雄，2选择路线
name01 = input("英雄列表:\n1.狄仁杰\n2.曹操 \n3.后裔 \n4.盖伦 \n请选择英雄:" );
if name01=="1":
    print("您选择的英雄为：狄仁杰\n")
    print("1.上路\n2.中路\n3.中单");
    # 强制类型转换 ：格式； 类型（原数据）
    s1 = str(10000);
    print(type(s1))
    number_01 = int(input("请选择路线:"));
    if number_01 == 1:
        print("您选择的英雄走上路")
        pass
    elif number_01 ==2:
        pass
    else:
        pass
    pass
else:
    print("请重新选择，除了狄仁杰，都不会。。。")
    pass

# 【4】=======循环====
print("=============循环语句==============")
array01= ["01.狄仁杰","02.曹操","03.蔡文姬","04.李白","05.甄姬"];
i = 0;
while i<len(array01):
    print(array01[i]);
    i+=1;
    pass

# for循环
print("=======for循环===========")
for name in array01:
    print(name)
    pass
# 4<=i<10
for i in range(4,10):
    print("循环结果："+str(i));
    pass


