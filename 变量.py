#一、1.变量名 = 值 :
apple = 5
print(apple)  #5

#2.变量之间的赋值 ：
pear = apple
print(pear)    #5

#3.表达书赋值：计算 -> 结果赋值 ：
num = 1 * 2
print(num)    #2

#ex：不带引号代表变量名，先赋值然后用（带引号是直接用的数据/值）

#4.变量可反复赋值，以后面的为准 ：
a = 1
a = "好"
print(a)    #好

#5.给多个变量一起赋值（变量名和值要一一对应） :
a, b, c = 1, 2, 3 #看看，现在前面输出的a可没一起变，前面变之前就先输出了
print(a, b, c)    #1 2 3

"""
6.命名规则：1..只能由字母、数字、下划线 _ 组成，不能包含空格、-、中文、特殊符号（@ # $等）
2..不能以数字开头，只能用字母或下划线开头
3..严格区分大小写：Name 和 name 是两个完全不同的变量
4..不能使用 Python 内置关键字（如 if、for、class、def、return、while、import 等）
5..当然，记得养成命名好习惯，别图省事
"""

#二、1.1整数 int（整型）
broken_heart = 1
print(broken_heart) #1
print(type(broken_heart))    #<class 'int'>

#1.2浮点数 float（浮点型，小数）
print(type(114.514))    #<class 'float'>

#1.3布尔类型 bool[只有两个值：True（等价整数 1）、False（等价整数 0）]
print(type(True)) #<class 'bool'>

#1.4复数 complex(实部 + 虚部)
num = 1 + 2j
print(type(num)) # <class 'complex'>

#2.字符串：单引号；双引号；三单引号（支持换行、多行文本）；三双引号（常用于多行注释、文档字符串）
#注：字符串内部包含引号时，外层用不同引号即可不用转义
print(type("a"))    #<class 'str'>

#3.空值：None，表示「空、无、没有任何值、不存在」,区别于数字0、空字符串""、空列表[]、布尔False