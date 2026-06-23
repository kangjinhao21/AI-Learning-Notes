#1.1 单行格式
#dict1 = {"键1": 值1, "键2": 值2, "键3": 值3}
'''
键必须是不可变类型且唯一(字符串、数字、元组);
值可以是任意类型且可以重复
'''

#1.2 多行规范格式（键值多推荐）
'''
dict2 =
{
    "name": "张三",
    "age": 20,
    "gender": "男"
}
'''

#2.1 查找元素
#2.1.1 dict[key](直接通过键取值，不过不推荐)
#2.1.2 get(key, default)(安全)
series = {"first": "Lobotomy Corporation", "second": "Library", "third": "Limbus Company"}
print(series.get("first"))      #Lobotomy Corporation
print(series.get("fourth","还得熬老头"))     #还得熬老头(默认的话是None)

#2.2 添加/修改元素：字典名[键] = 值（存在修改，不存在添加）
series["second"] = "Library of Ruina"
print(series.get("second"))     #Library of Ruina
series["fourth"] = "小金的神备"
print(series)       #{'first': 'Lobotomy Corporation', 'second': 'Library of Ruina', 'third': 'Limbus Company', 'fourth': '小金的神备'}

#2.3 删除元素
#2.3.1 字典名.pop(键，默认值)
series.pop("fourth")
print(series)       #{'first': 'Lobotomy Corporation', 'second': 'Library of Ruina', 'third': 'Limbus Company'}
print(series.pop("fourth", "还没出"))      #还没出

#2.3.2 字典名.clear：清空所有键值对，变成空字典
all = {"first": "Catherine1", "second": "Catherine2", "third": "Catherine3"}
all.clear()
print(all)      #{}

#2.4.1 keys(): 获取字典所有键
#2.4.2 values(): 获取字典所有值
#2.4.3 items(): 获取字典所有键值对
print(series.keys())        #dict_keys(['first', 'second', 'third'])
print(series.values())      #Library of Ruina
print(series.items())       #dict_items([('first', 'Lobotomy Corporation'), ('second', 'Library of Ruina'), ('third', 'Limbus Company')])