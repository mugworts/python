# coding=utf-8

# def add(a, b):
#     return a + b


# print(add(1, 2))


# a = 1


# def func(a):
#     print("在函数内部修改之前,变量a的内存地址为： %s" % id(a))
#     a = 2
#     print(a is a)
#     print("在函数内部修改之后,变量a的内存地址为： %s" % id(a))
#     print("函数内部的a为： %s" % a)


# print("调用函数之前,变量a的内存地址为： %s" % id(a))
# func(a)
# print("函数外部的a为：%s" % a)


# def test(a, b, c):
#     return a+b+c

# print(test(1, 2, 3))


# def test1(a, b, c = 3, d= 2):
#     return (a+b)*c*d
# print(test1(1, 2))

# def power(x, n = 2):
#     return x**n
# ret1 = power(10)   # 使用默认的参数值n=2
# ret2 = power(10, 4)  # 将4传给n，实际计算10**4的值
# ret3 = power(n=1, x=100) # 指定参数值

# print(ret3)

# def func(*para_tumple):
#     print(type(para_tumple))
#     for item in para_tumple:
#         print(item)

# func('a', 'b', 'c')

# li = [1, 2, 3]
# func(li)



# ----------

x = 1
print("第一步：a的内存地址： ", id(x))


def outer():
    x = 2
    print("第二步：x的内存地址： ", id(x))
    def inner():
        x = 3
        # 打印同层
        print("第三步：x的内存地址： ", id(x))
    def inner_up():
        print("第三步(up)：x的内存地址： ", id(x))
    inner()
    inner_up()
    # 打印的是同层x=2，即outer()下侧的同一作用域的x
    print("第四步：x的内存地址： ", id(x))
outer()
print("第五步：x的内存地址： ", id(x))

name ='简单即是美'

def f1():
    print(name)

def f2():
    name = 'Python'
    f1()
f2()