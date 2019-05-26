
# # encoding=utf8
# list = [1, '2', '3', 'p']

# # 方法1
# print('遍历列表方法1: ')
# print(id(list))
# for i in list:
#     print("序号：%s   值：%s, 地址 %d" % (list.index(i) + 1, i, id(i)))

# print('\n遍历列表方法2：')
# # 方法2
# for i in range(len(list)):
#     print("序号：%s   值：%s" % (i + 1, list[i]))

# # 方法3
# print('\n遍历列表方法3：')
# for i, val in enumerate(list):
#     print("序号：%s   值：%s" % (i + 1, val))

# # 方法3
# print('\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：')
# for i, val in enumerate(list, 2):
#     print("序号：%s   值：%s" % (i + 1, val))

# a = "I'm %s. I'm %d year old" % ('Vamei', 99)
# print(a)
# print("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})


# list1 = [1, 2, 5, 4]
# list3 = sorted(list1)
# print(list1)
# print(list3)
# list2 = list1.sort()


# list4 = list(range(10))
# print(list4)


alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# stop_index 逻辑上要大于 start_index
# 正整数stop_index>start_index
# 负数：stop_index<start_index & step<0

print(alist[1:8:3])
# 全部，正向取值
print(alist[:])
# 全部，反向取值
print(alist[-1:-11:-1])
# stop_index > len(list), 不报错
print(alist[-1:-12:-1])


# # 取前一部分
# >>> alist[:5]
# [0, 1, 2, 3, 4]

# # 取后一部分
# >>> alist[-5:]
# [5, 6, 7, 8, 9]

# # 取偶数位置元素
# >>> alist[::2]
# [0, 2, 4, 6, 8]

# # 取奇数位置元素
# >>> alist[1::2]
# [1, 3, 5, 7, 9]




# alist[:0] = ['a','b','c']
# print(alist)

alist[1:3] = ['a','b','c']
print(alist)


string = "abcde"
print(string[1:3])


