import pandas as pd
import numpy as np
# Pandas是基于Numpy开发出的,专门用于数据分析的开源Python库

# 1.Pandas的两大核心数据结构
# -------      series(一维数组)：键值对 的结构
#   通过Numpy数组结构创建Series
series_01 = pd.Series(np.arange(4,10))
print("Numpy数组是:\n",np.arange(4,10))
print("转换成Series:\n", series_01)
#   通过Python数组创建Series，并指定索引
series_02 = pd.Series([11,12,14],index=["北京","上海","深圳"])
print("通过Python创建的Series:\n",series_02)
#   通过Python字典创建Series
series_03 = pd.Series({"北京":11,"上海":12,"深圳":14})
print("通过Python字典创建Series:\n",series_03)
# ------      DataFrame(多特征数据,既有行索引,又有列索引)
# 创建一个3行4列的DataFrame类型数据
DataFrame_01 = pd.DataFrame(np.arange(10,22).reshape(3,4))
print("3行4列DataFrame数据:\n",DataFrame_01)
print("打印第一行数据:\n",DataFrame_01[:1])
print("打印第一列数据:\n",DataFrame_01[:][0])

# 2.DataFrame的属性
# 读取数据
result = pd.read_csv("student.csv")
print("csv文件内容为:\n",result)
print("数据的形状:\n",result.shape)
print("每列数据的类型信息:\n",result.dtypes)
print("数据的维数\n",result.ndim)
print("数据的索引(起/始/步长)\n",result.index)
print("打印每一列 属性的名称\n",result.columns)
print("将数据放到数组中显示\n",result.values)

print("-->前5个:")
print(result.head(5))
print("-->后5个:")
print(result.tail(5))
# 打印描述信息(实验中好用)
print("-->描述信息:")
print(result.describe())

# 3.Panda数据读取(以CSV为例)
'''
pandas.read_csv(filepath_or_buffer, sep=",", names=None, usecols = None)

filepath_or_buffer : 文件路径(本地路径或url路径)
sep: 分隔符
names: 列索引的名字
usecols: 指定读取的列名

返回的类型: DataFrame  
'''
# 打印特点字段，指定数量的信息
print(result["姓名"][0:6])
print("读取后返回的数据类型为——>",type(result))
# 通过布尔索引过滤数据
print("年龄大于23岁的人",result[result["age"]>23])