
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


list4 = list(range(10))
print(list4)


list5 = [ ... for i in list4 ]
print(list5)