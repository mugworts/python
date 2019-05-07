# coding=utf-8
import random

print("---基本---")
# 基本
# 返回当前生成器的内部状态
print(random.getstate())
# 不大于K位的Python整数,结果是0~2^10之间的整数
print(random.getrandbits(10))

print("---整数---")
# 整数
# 0-9的整数：
print(random.randrange(10))
# 0-100的偶数
print(random.randrange(0, 101, 2))
# 返回 a <= N <= b， 等同于randrange(a, b+1)。
print(random.randint(1, 9))

print("---list---")
# list
# 从序列随机选择一个元素
print(random.choice(['python', 'node', '种地']))


print("---真值分布---")
# 随机浮点数:  0.0 <= x < 1.0
print(random.random())
# 随机浮点数:  1.1 <= x < 11.1
print(random.uniform(1.1, 11.1))


# 对序列进行洗牌，改变原序列
deck = 'one two three four'.split()
random.shuffle(deck)
print(deck)
