#!/usr/bin/python
num = 3
list1 = [0.0 for _ in range(num)]
print(list1)

from functools import reduce
a = [1, 1]
b = [0, 0]
c = reduce(lambda a,b:a+b, list(map(lambda x_y:x_y[0] * x_y[1], list(zip(a,b)))))
print(c)