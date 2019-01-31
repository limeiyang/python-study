#!/usr/bin/python
'''
reduce() 函数会对参数序列中元素进行累积。
！！！在python3中已将reduce函数从全局名字空间移除，
现在被放置在 functools 模块中
'''
# 两数相加
from functools import reduce
def add(x, y):
    return x + y
sum1 = reduce(add, [1,2,3,4,5])

# 或者用lambda函数（详见12）
sum2 = reduce(lambda x,y:x+y, [1,2,3,4,5])

print("[1,2,3,4,5]的和为", sum1)
print("[1,2,3,4,5]的和为", sum2)