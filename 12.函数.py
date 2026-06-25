#1.1 函数定义
"""
def 函数名(参数列表(可选)):
    '''函数文档说明（可选，用于描述函数功能）'''
    函数体代码
    return 返回值
"""

#1.2 调用    语法：函数名(参数列表)
#1.3.1 无参数无返回值的函数
def sad():
    print("不知为何的惆怅")
sad()       #不知为何的惆怅

#1.3.2 带参数的函数
def unknown(time):
    print(f"你好，{time}！")
unknown("明天")       #你好，明天！
unknown("昨日")       #你好，昨日！

#2.1 位置参数（调用时按参数定义的顺序依次传值，参数数量必须和定义时完全一致）
def add(a, b):
    print(a + b)
add(3, 5)       #8

#2.2 默认参数（定义函数时给参数设置默认值；调用时如果不传该参数，就自动使用默认值）
# 注：默认参数必须写在普通位置参数的后面
def power(date = "今天", emotion = "好"):
    print(f"日期为{date}, 心情为{emotion}")
power()                     #日期为今天, 心情为好
power("明天")                #日期为明天, 心情为好
power(emotion = "不好")      #日期为今天, 心情为不好

#2.3 可变位置参数 *args（接收任意多个位置参数，会把所有传入的参数自动打包成一个元组，在函数内可遍历使用）
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    print(total)
sum_all(1, 2, 3)        #6

#2.4 可变关键字参数 **kwargs（接收任意多个关键字参数，会把所有传入的键值对自动打包成一个字典）
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="无缘言之", age=19, gender="男")
'''
name: 无缘言之
age: 19
gender: 男
'''

#3.返回值 return（将函数的计算结果返回给调用处，同时立即终止函数的执行）
#3.1 无返回值，执行结束后默认返回 None（空值） （就是前面那些）

#3.2 单返回值
def add(a, b):
    return a + b            # 将结果返回给调用方
result = add(4, 6)     # 用变量接收返回值
print(result)               #10

#3.3 多返回值
def calc(a, b):
    sum_ab = a + b
    diff_ab = a - b
    return sum_ab, diff_ab  # 返回两个结果

s, d = calc(10, 3)     # 解包接收两个返回值
print(s, d)                 #13 7

#4.变量作用域（变量可以被访问的有效范围）
#4.1 局部变量（在函数内部定义的变量，只能在函数内部使用，函数执行结束后就会销毁）
def func():
    x = "好人"      # 局部变量
    print(x)

func()          #好人
# print(x)      # 报错：外部无法访问函数内的局部变量

#4.2 全局变量（在函数外部定义的变量，整个代码文件中都可以访问）
y = "人"        # 全局变量

def func():
    print(y)    # 函数内可以读取全局变量

func()          #人

#4.3 global 关键字（如果想在函数内部修改全局变量的值，必须先用 global 声明，否则会被当成新的局部变量）
count = 0

def add_count():
    global count    # 声明此处使用全局变量 count
    count += 1

add_count()
add_count()
print(count)        #2