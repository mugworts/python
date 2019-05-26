# encoding=utf8

# 三种创建方式

dic1 = {"sex": 1}
dic2 = dict([('name', 'simuty'), ("age", 1)])
dic3 = dict(age=2, name='python', sex=1)
print(dic1)
print(dic2)
print(dic3)
'''
{'sex': 1}
{'name': 'simuty'}
{'age': 2}
'''

# 删除指定元素
del dic3['age']
dic3.pop('name')
print(dic3)

# 清空字典
dic3.clear()
print(dic3)

del dic3
# print(dic3)
'''
{'age': 2, 'name': 'python', 'sex': 1}
{'sex': 1}
{}
Traceback (most recent call last):
  File "dic.py", line 28, in <module>
    print(dic3)
NameError: name 'dic3' is not defined
'''

print(dic2.get('name'))
print(dic2.get('noExist'))
'''
simuty
None
'''

print(dic2.items())

a_dict = dict(k=4, z=2)
a_dict.update(dict(l=1))
# b = {1: 1, 2: 3}
print(a_dict)

a_dic = {"k": 1}
b_dic = {'k': 2, "x": 3}
a_dic.update(b_dic)
print(a_dic)

print(b_dic.popitem())
print(b_dic)
print("====")

dic = {'k': 2, "x": 3}
# 1  直接遍历字典获取键，根据键取值
for key in dic:
    print(key, dic[key])

# 2  利用items方法获取键值，速度很慢，少用！
for key, value in dic.items():
    print(key, value)

# 3  利用keys方法获取键
for key in dic.keys():
    print(key, dic[key])

# 4  利用values方法获取值，但无法获取对应的键。
for value in dic.values():
    print(value)

set1 = {1, 2, 3}
set2 = {5, 4, 3}

print(set1 ^ set2)
print(set1 - set2)
print(set2 - set1)
print(set1 & set2)
print(set1 | set2)

a = {1, 2, 3, 4}
print(a)
b = a.add(5)
print(b)
