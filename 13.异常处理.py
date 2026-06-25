#Python 异常处理（用于捕获程序运行时的错误（异常），避免程序直接崩溃，同时可用于错误日志记录、资源清理等场景）
"""
1.try-except
优先执行 try 代码块内的代码
若全程无异常，跳过所有 except 块，继续向下执行
若发生异常，立刻终止 try 内后续代码，匹配对应 except 分支并执行
"""
#1.1 捕获单个异常
try:
    num = int(input("输入一个数字: "))
    result = 10 / num
    print("计算结果:", result)
except ZeroDivisionError:
    print("错误：除数不能为 0")

#1.2 捕获多个异常
#1.2.1 写多个 except 分支，分别处理不同类型的错误
try:
    num = int(input("输入一个数字: "))
    result = 10 / num
    print("计算结果:", result)
except ValueError:
    print("错误：请输入有效的整数")
except ZeroDivisionError:
    print("错误：除数不能为 0")

#1.2.2 用元组一次性捕获多种异常，共用同一段处理逻辑
try:
    num = int(input("输入一个数字: "))
    result = 10 / num
    print("计算结果:", result)
except (ValueError, ZeroDivisionError) as e:        # as e 可以获取异常对象的详细描述信息，方便调试和日志记录。
    print(f"发生错误: {e}")

#2.1 else 子句（仅在 try 块未发生任何异常时才会执行，用于将 “可能出错的代码” 和 “成功后才执行的逻辑” 解耦）
try:
    file = open("data.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("错误：目标文件不存在")
else:
    content = file.read()       # 文件打开成功后，再执行读取操作
    print(content)
    file.close()

#2.2 finally 子句（无论是否发生异常、异常是否被捕获，最终都会执行，通常用于释放资源（关闭文件、断开数据库连接、释放锁等））
try:
    file = open("data.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("错误：目标文件不存在")
finally:
    if "file" in locals():
        file.close()
    print("资源清理完成")           # 无论打开成功或失败，都尝试清理资源

"""
异常种类：
1.语法与代码结构类
1.1 SyntaxError（语法错误）
最基础的语法错误，代码不符合 Python 语法规则时触发。
常见场景：括号 / 引号不配对、控制语句缺少冒号、关键字拼写错误。

1.2 IndentationError（缩进错误）
SyntaxError 的子类，Python 依靠缩进划分代码块，缩进不统一、层级错误时触发。

1.3 TabError（制表符缩进错误）
IndentationError 的子类，代码中混用 Tab 和空格进行缩进且无法对齐时触发。

2.数据类型与值类
2.1 TypeError（类型错误）
操作或函数接收到的参数类型不匹配时触发。
常见场景：不同类型直接运算、对不可迭代对象遍历、函数传参数量不符。

2.2 ValueError（值错误）
参数类型正确，但值的内容不合法、不在预期范围内时触发。
常见场景：类型转换失败、传入无效枚举值。

2.3 NameError（名称错误）
使用了未定义的变量、函数或类名时触发。
常见场景：变量名拼写错误、超出作用域访问变量、使用未导入的对象。

3.序列与映射访问类
3.1 IndexError（索引越界错误）
访问列表、元组、字符串等序列时，下标超出有效范围触发。

3.2 KeyError（键不存在错误）
访问字典中不存在的键时触发。

4.属性与对象操作类
AttributeError（属性错误）
对象不存在指定的属性或方法时触发。
常见场景：调用对象没有的方法、访问不存在的实例属性。

5.导入与模块类
5.1 ImportError（导入错误）
从模块中导入指定对象失败时触发。

5.2 ModuleNotFoundError（模块未找到）
ImportError 的子类（Python 3.6+ 新增），尝试导入不存在的模块时触发，是最常见的导入异常。

6.文件与系统 IO 类
6.1 FileNotFoundError（文件未找到）
尝试打开不存在的文件或目录时触发。

6.2 PermissionError（权限错误）
没有足够的读写权限操作文件 / 目录时触发。

6.3 IsADirectoryError（目录操作错误）
把目录当作普通文件来读写时触发。

7.运算与执行类
7.1 ZeroDivisionError（除零错误）
除法或取模运算中除数为 0 时触发。

7.2RecursionError（递归深度超限）
RuntimeError 的子类，递归调用层数超过 Python 默认递归深度（默认约 1000 层）时触发。

8.其他
8.1 AssertionError（断言失败）
assert 断言语句的条件不成立时触发，多用于调试和参数校验。

8.2 StopIteration（迭代停止）
迭代器没有更多元素时触发，for 循环内部会自动捕获该异常。

8.3 KeyboardInterrupt（键盘中断）
用户按下 Ctrl+C 中断程序时触发，直接继承 BaseException，不属于普通 Exception 子类。

8.4 RuntimeError（运行时错误）
通用运行时异常，其他分类无法覆盖的运行错误归为此类，也常用作自定义异常的基类。
"""