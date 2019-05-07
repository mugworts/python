# coding=utf-8


import math
# print(dir(math))
# print(abs(-10))
# print(cmp(1, 3))
# print(math.exp(2))
# print(math.ceil(1.2), math.ceil(-1.2))
# print(math.floor(1.2))
# print(max([12, 1]))

import random
# 随机生成一个0-1的数字
print(random.random())
# 随机从给定数据中筛选出一个数字
print(random.choice([1, 2, 3, 4]))
# 输出 100 <= number < 1000 间的偶数
print(random.randrange(100, 1000, 2))
list = [20, 16, 10, 5];
print(random.uniform(2.5, 10.0))

print(random.shuffle([20, 16, 10, 5]))