# encoding=utf8
var1 = 'Hello World!'
var1 = "Python"
# 在 python 中赋值语句总是建立对象的引用值，而不是复制对象。因此，python 变量更像是指针，而不是数据存储区域，
print(var1)

# 三括号注释
var2 = """
>>> a = "asd"
>>> id(a)
4431000496
>>> a = "122"
>>> id(a)
4431000552
"""
print(var2)


# 第二部分

# 填充
var3 = "1234"
print(var3.center(10, "*"))
print(var3.ljust(10, '^'))
print(var3.rjust(10, "^"))
print(var3.zfill(10))
# 返回值
'''
***1234***
1234^^^^^^
^^^^^^1234
0000001234
'''

# 删减
var4 = "55785"
print(var4.strip("5"))
print(var4.lstrip("5"))
print(var4.rstrip("5"))

# 返回值
'''
78
785
5578
'''


# 变形
var5 = "thank yoU"
print(var5.lower())
print(var5.upper())
print(var5.capitalize())
print(var5.swapcase())
print(var5.title())

'''
thank you
THANK YOU
Thank you
THANK YOu
Thank You
'''

# 切分
var6 = "7890"
# 有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
print(var6.partition('9'))
print(var6.partition('2'))
print(var6.rpartition("0"))
var7 = "abz\nzxy"
print(var7.splitlines())
print(var7.split("z"))
print(var7.rsplit("z"))


# 连接
var8 = "ikaf"
print(var8.join("0000"))

# 判定
var9 = "kj45"
# 长度>0 && 都是字母或都是数字 true 否则false
print(var9.isalnum())
# 长度>0 &&  都是字母 true 否则false
print(var9.isalpha())
print(var9.isdigit())
print(var9.islower())
print(var9.isupper())
print(var9.isspace())
print(var9.istitle())
print(var9.startswith('k'))
print(var9.endswith('5'))


# 查找
var10 = "1234567890zxc123vbndfgh"
print(var10.count('123', 0, len(var10)))
# 返回第一个满足条件的位置
print(var10.find('3', 0, len(var10)))
#
print(var10.index('3', 0, len(var10)))
# 找不到返回-1
print(var10.rfind('mm', 0, len(var10)))
# 找不到报错
# print(var10.rindex('mm', 0, len(var10)))

# 替换
var11 = "aaaa111222hhhjjjkkk"
print(var11.replace("a", "b", 2))
# print(var11.translate())
#  translate(table[,deletechars])

# 编码解码
# 编码就是将字符串转换成字节码，涉及到字符串的内部表示。
# 解码就是将字节码转换为字符串，将比特位显示成字符。

var12 = "什么鬼"
print(var12.encode())
print(var12.encode().decode())

'''
b'\xe4\xbb\x80\xe4\xb9\x88\xe9\xac\xbc'
什么鬼
'''
