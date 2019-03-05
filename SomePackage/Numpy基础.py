#NumPy是Python语言的一个扩充程序库。支持高级大量的维度数组与矩阵运算，此外
# 也针对数组运算提供大量的数学函数库。Numpy内部解除了Python的PIL(全局解释器锁),
# 运算效率极好,是大量机器学习框架的基础库!
# https://www.jianshu.com/p/83c8ef18a1e8
import numpy as np

# ==1.创建简单的数组
# 创建简单的列表
list_01 = [1,2,3,4]
# 将列表转换成数组
array_01 = np.array(list_01)
print("列表：",list_01)
print("数组：",array_01)

# ==2.Numpy查看数据的属性
print("数组元素的个数：",array_01.size)
print("数组的形状：",array_01.shape)
print("数组的维度：",array_01.ndim)
print("数组元素的类型：",array_01.dtype)

# ==3.快速创建N维数组的api函数
# 创建10行10列的数值为浮点1的矩阵
array_one_01 = np.ones([10, 10])
print("10行10列浮点1矩阵:\n",array_one_01)
# 创建10行10列的数值为浮点0的矩阵
array_zero_01 = np.zeros([10,10])
print("10行10列数值0矩阵:\n",array_zero_01)

# ==3.Numpy创建随机数组
# 均匀分布
print("创建10行10列的数组（范围0到1之间）：")
array_02 = np.random.rand(10,10)
print(array_02)
print("创建指定范围内的一个数：")
array_03 = np.random.uniform(0,100)
print(array_03)
print("创建指定范围内的一个整数：")
array_04 = np.random.randint(0,100)
print(array_04)

# ==4.正态分布
# 给定均值/标准差/维度的正态分布
print("正态生成4行5列的二维数组:")
array_05 = np.random.normal(1.75,0.1,(4,5))
print(array_05)
print("截取第1至2行的第2至3列（从第0行算起）:")
after_array_05 = array_05[1:3,2:4]
print(after_array_05)

# ==5.改变数组形状（要求前后元素个数匹配）
print("reshape函数的使用：")
array_one_02 = np.ones([20])
print("-->1行20列<--")
print(array_one_02)
print("-->4行5列<--")
array_4_5_ = array_one_02.reshape([4,5])
print(array_4_5_)

# ==6.Numpy计算
# 条件判断
stus_score = np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print("原矩阵：\n",stus_score)
print("条件判断:(>80)\n",stus_score > 80)
# 三目运算
stus_score_01 = np.where(stus_score<80,0,90)
print("三目运算:(小于80变0，大于80变90)\n",stus_score_01)

# ==7.统计运算
# 求每一列的最大值 axis=0表示列
print("每一列的最大值为：")
result_0_max = np.amax(stus_score,axis=0)
print(result_0_max)
# 求每一行的最大值 axis=1表示行
result_1_max = np.amax(stus_score,axis=1)
print(result_1_max)
###### 最小值 将amax改为amin
###### 平均值 将amax改为mean
###### 方差 将amax改为std

# ==8.数据运算
# 数组与数运算
stus_score = np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print("平时成绩加5")
print("加分前:[平时成绩，期末成绩]:\n",stus_score)
stus_score[:, 0] = stus_score[:, 0] + 5
print("加分后:",stus_score)
stus_score = np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
print("平时成绩减半")
print("减分前:[平时成绩，期末成绩]:\n",stus_score)
stus_score[:, 0] = stus_score[:, 0] * 0.5
print("减分后:",stus_score)

# 数组与数组的加减乘除
a = np.array([10,20,30,40])
b = np.array([1,2,3,4])
print("a+b为",a+b)
print("a-b为",a-b)
print("a*b为",a*b)
print("a/b为",a/b)

# 计算规则 (M行, N列) * (N行, Z列) = (M行, Z列)
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 平时成绩占40% 期末成绩占60%, 计算结果
q = np.array([[0.4], [0.6]])
result = np.dot(stus_score, q)
print("最终结果为:")
print(result)

# ==9.矩阵拼接
v_01 = [[0,1,2,3,4,5],
        [6,7,8,9,10,11]]
v_02 = [[12, 13, 14, 15, 16, 17],
      [18, 19, 20, 21, 22, 23]]
print("v_01为",v_01)
print("v_02为",v_02)
# 垂直拼接
v_v_01 = np.vstack((v_01,v_02))
print("v_01和v_02垂直拼接结果为\n",v_v_01)
# 水平拼接
v_h_01 = np.hstack((v_01,v_02))
print("v_01和v_02水平拼接结果为\n",v_01)

# ==10.读取csv文件
# result = np.genfromtxt("地址",delimiter=",")