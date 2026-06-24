#1.while循环
'''
while 条件表达式:
    循环体代码       # 重复执行的代码（必须缩进）
    更新条件代码     # 避免死循环
'''

#1.1 基础计数
i = 1
count = 0
while i <= 5:
    count += i
    i += 1
print(count)        #15

#1.2 无限循环（配合 break 主动退出）
while True:
    s = input("输入 'quit' 退出：")
    if s == 'quit':
        break
    print("你输入了：", s)       # 输入quit才退出循环

#1.3 嵌套（如while 嵌套 + break 跳出内层循环）
i = 1
while i <= 3:
    print(f"第{i}轮外层")
    j = 1
    while j <= 5:
        if j == 3:
            break  # 只跳出内层while
        print(f"内层j={j}", end=" ")
        j += 1
    print()
    i += 1
'''
第1轮外层
内层j=1 内层j=2 
第2轮外层
内层j=1 内层j=2 
第3轮外层
内层j=1 内层j=2 
'''

#2.for循环（用于遍历可迭代对象（列表、字符串、元组、字典等））
'''
for 变量 in 可迭代对象/次数序列:
    循环体代码
    
range(start, stop, step) 生成整数序列，遵循左闭右开规则（包含 start，不包含 stop）。
range(n)：生成 0 ~ n-1 的整数
range(a, b)：生成 a ~ b-1 的整数
range(a, b, step)：按步长 step 生成整数
'''

#2.1 遍历字符串（逐一取出每一字符）
for char in "Python":
    print(char)
'''
P
y
t
h
o
n
'''

#3.1 break（立即终止整个循环，跳出循环体）
for i in range(1, 6):
    if i == 3:
        break
    print(i)
'''
1
2
'''

#3.2 continue（跳过当前这一次循环，直接进入下一轮循环）
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
'''
1
2
4
5
'''

#4.for / while 搭配 else 使用
for i in range(3):
    print(i)
else:
    print("循环正常结束")
# 输出：0 1 2 循环正常结束（和上面一样一行一个）