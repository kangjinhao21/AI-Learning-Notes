#1.从包导入指定模块
#1.1 import 包名.模块名.函数()
import first_package.calc
print(first_package.calc.add(1, 2))     #3

#1.2 from 包名 import 模块名
from first_package import calc
print(calc.multiply(1, 2))         #2

#2.批量导入所有公开成员（from 包名 import *）
#2.1 配置__init__.py

#2.2 批量导入并使用（eg）
# from first_package import *
# greet.hello("博士")        #你好呀，博士！（print(greet.hello("博士")) 多打了一层 print，会多出 None）

from first_package.greet import bye
bye("鸿璐的奶奶")             #再见，鸿璐的奶奶~