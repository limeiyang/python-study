import matplotlib.pyplot as plt
import numpy as np

# 生成1024个呈标准正态分布的二维数据组 (平均数是0，方差为1) 作为一个数据集
# 每一个点的颜色值用T来表示
n = 1024    # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)    # for color later on

plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()