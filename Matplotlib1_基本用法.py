#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

# 1.输出直线
x = np.linspace(-1, 1, 50)
y = 2*x + 1
plt.figure(num = 1)# 设置窗体一
plt.plot(x, y)
plt.show()

# 2.输出弧线
y1 = x**2
plt.figure(num = 2)# 设置窗体二
plt.plot(x, y1)
plt.show()

# 3.在一个窗体（figure）中绘制两张图
plt.figure(num = 3, figsize=(8, 5))
plt.plot(x, y1)
plt.plot(x, y, color = 'red', linewidth = '1.2', linestyle = '--')
plt.show()

# 4.设置坐标轴范围和名称
plt.figure(num = 4)
plt.plot(x, y1)
plt.plot(x, y, color = 'red', linewidth = '1.2', linestyle = '--')
plt.xlim((-1, 2))# 设置横坐标范围-1到2
plt.ylim((-2, 3))# 设置纵坐标范围-2到3
plt.xlabel('I am X')# 设置横坐标名称
plt.ylabel('I am Y')# 设置纵坐标名称
plt.show()

# 5.设置坐标轴刻度范围和名称
plt.figure(num = 5)
plt.plot(x, y1)
plt.plot(x, y, color = 'red', linewidth = '1.2', linestyle = '--')
new_ticks  = np.linspace(-1, 2, 5)# 范围：(-1, 2)个数：5
print(new_ticks)# 打印出范围
plt.xticks(new_ticks)# 设置新的刻度
plt.yticks([-2, -1.8, -1, 1.22, 3],['really bad', 'bad', 'normal', 'good', 'really good'])
# 刻度对应的名称
plt.show()

# 6.设置边框
# -----同5-------
plt.figure(num = 6)
plt.plot(x, y1)
plt.plot(x, y, color = 'red', linewidth = '1.2', linestyle = '--')
new_ticks  = np.linspace(-1, 2, 5)# 范围：(-1, 2)个数：5
print(new_ticks)# 打印出范围
plt.xticks(new_ticks)# 设置新的刻度
plt.yticks([-2, -1.8, -1, 1.22, 3],['really bad', 'bad', 'normal', 'good', 'really good'])
# 刻度对应的名称
#---------------
ax = plt.gca()# 获取当前坐标轴信息
ax.spines['right'].set_color('red')# 设置右边框
ax.spines['top'].set_color('yellow')# 设置上边框
plt.show()

# 7.调整坐标轴
# -----同5-------
plt.figure(num = 7)
plt.plot(x, y1)
plt.plot(x, y, color = 'red', linewidth = '1.2', linestyle = '--')
new_ticks  = np.linspace(-1, 2, 5)# 范围：(-1, 2)个数：5
print(new_ticks)# 打印出范围
plt.xticks(new_ticks)# 设置新的刻度
plt.yticks([-2, -1.8, -1, 1.22, 3],['really bad', 'bad', 'normal', 'good', 'really good'])
# 刻度对应的名称
#---------------
ax = plt.gca()# 获取当前坐标轴信息
# 使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置:bottom (所有的位置:top bottom both default none)
ax.xaxis.set_ticks_position('both')
# 使用.spines 设置边框：x轴；使用.set_position 设置边框位置：y=0的位置；（位置所有属性:outward, axes, data）
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()