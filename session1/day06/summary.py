a = 1
b = 2
c = 1
print(" a: %s \n b: %s \n c: %s" % (id(a), id(b), id(c)))
print(" -----")
x = [a, b, c]
print(" x: %s \n ------ \n x[0]: %s \n x[1]: %s \n x[2]: %s" %
      (id(x), id(x[0]), id(x[1]), id(x[2])))
print(" -----")
y = x
x += [3, 4]
print(" x: %s, y: %s" % (id(x), id(y)))

x = x + [3, 4]
print(" -----")
print(" x: %s \n ------ \n x[0]: %s \n x[1]: %s \n x[2]: %s" %
      (id(x), id(x[0]), id(x[1]), id(x[2])))
a = 3
print(" a: %s" % (id(a)))

dic = {"key1": 1}
print(id(dic))
for key in dic.keys():
    print(id(key), id(dic[key]))


print("=======\n")
print("{} {}".format("hello", "world"))
print("{1} {0}".format("hello", "world"))

# >>> print('%f' % 1.11)  # 默认保留6位小数
# 1.110000
# >>> print('%.1f' % 1.11)  # 取1位小数
# 1.1
# >>> print('%e' % 1.11)  # 默认6位小数，用科学计数法
# 1.110000e+00
# >>> print('%.3e' % 1.11)  # 取3位小数，用科学计数法
# 1.110e+00
# >>> print('%g' % 1111.1111)  # 默认6位有效数字
# 1111.11
# >>> print('%.7g' % 1111.1111)  # 取7位有效数字
# 1111.111
# >>> print('%.2g' % 1111.1111)  # 取2位有效数字，自动转换为科学计数法
# 1.1e+03


