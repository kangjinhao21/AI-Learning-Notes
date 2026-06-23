#1.1 空列表
list1 = []
list2 = list()
print(list2)    #[]

#1.2 存放相同类型元素
num_list = [10, 20, 30, 40]
str_list = ["苹果", "香蕉", "橙子"]
print(str_list)     #['苹果', '香蕉', '橙子']

#1.3 存放不同类型元素
mix_list = [18, "张三", True, 3.14]
print(mix_list)     #[18, '张三', True, 3.14]

#1.4 嵌套列表（二维列表）
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list)      #[[1, 2], [3, 4], [5, 6]]

#2.1 索引(可正向/负向)
list = ['回', '答', '我']
print(list[2])      #我

#2.2 切片(列表[起始索引:结束索引:步长]，左闭右开)
lst = [0, 1, 2, 3, 4, 5]
print(lst[1:4])    #[1, 2, 3]
print(lst[::2])    #[0, 2, 4]
print(lst[::-1])   #[5, 4, 3, 2, 1, 0]

#2.3 可修改
lst = [1, 2, 3]
lst[0] = 100  #直接通过索引重新赋值
print(lst)    #[100, 2, 3]

#3.列表嵌套(俄罗斯套娃)
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1])   #[3, 4]
print(nested_list[1][0])    #3

#4.1 添加元素
main = ["罗兰"]
main.append("安吉莉卡")     #末尾追加
print(main)     #['罗兰', '安吉莉卡']
main.insert(1, "安吉拉")   #指定索引位置插入
print(main)     #['罗兰', '安吉拉', '安吉莉卡']
main.extend(["Ayin", 2])
print(main)     #['罗兰', '安吉拉', '安吉莉卡', 'Ayin', 2]

#4.2 查找元素
print(main.index("罗兰"))    #0
print(main.count("罗兰"))    #1

#4.3 删除元素
main.remove("Ayin")     #删除列表中第一个匹配该值的元素，无返回值
print(main)     #['罗兰', '安吉拉', '安吉莉卡', 2]
main.pop(2)     #默认()空着删除最后一个元素，返回被删值
print(main)     #['罗兰', '安吉拉', 2]
main.clear()      # 清空列表所有元素
print(main)     #[]
#del lst[索引数]       # 删除指定索引元素

#4.4 排序与反转
homo = [1, 9, 1, 9, 8, 1, 0]
'''
字母的话先按首字母 ASCII 码从小到大排；
大写字母 ASCII 数值 < 小写字母，所以大写单词排在前面；
首字母相同就比较第二个字母，依次往后。
'''
#print(homo.sort())可不行，打印的是该方法的返回值(没有返回值)，输出 None
homo.sort()     #原地升序排序
print(homo)     #[0, 1, 1, 1, 8, 9, 9]
homo.sort(reverse=True)     #降序
print(homo)     #[9, 9, 8, 1, 1, 1, 0]
homo.reverse()  #倒过来
print(homo)     #[0, 1, 1, 1, 8, 9, 9]