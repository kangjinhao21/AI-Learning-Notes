#input函数(cin??)
name = input("你的名字：") #姓名保存到name变量
print(name,"我找到你了") #name 我找到你了 "问 -> 反应（一丝期待） -> 答“

age = input("小伙子，你多大了：")
print(age, type(age))   #34 <class 'str'>,字符串和数字可是心意相悖的哦（指运算不了）

#解决方式：int（）或float（），转类型
num_1 = int(input("1+1等于多少："))
num_2 = int(input("2+2等于多少："))
print(num_1 + num_2)  #6 , 同理可以把int换成float