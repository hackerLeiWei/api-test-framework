import math
from random import random


print("""
•Beautiful is better than ugly.
•Simple is better than complex.
•Complex is better than complicated.
•Readability counts.
•There should be one -- and preferably only one --obvious way to do it.
•Now is better than never.
""")


print("Hello Python!")
print("Hello World!")

message = "Hello Python! Hello World!"
print(message)
# 换行字符串
message = """
Hello Python!
Hello World!
"""
print(message)
message = "Hello Python! \
     Hello World!"
print(message)
print(message.count("Hello"))
print(message.__len__())
# 首字母大写
print("ada lovelace".title())
# 函数和方法, 可以把方法视为特殊的函数
print(print) # <built-in function print>
print(''.title) # <built-in method title of str object at 0x000001A3D8B3B340>

print("aBc".upper())
print("aBc".lower())
print("aBc c".title()) # 每个单词首字母大写

firstName = "   Wei "
lastName = " Lei   "
fullName = f"Wei {lastName}" # f <==>format 简写
print(fullName)
print(f"name:{firstName.lstrip()} length: {firstName.lstrip().__len__()}") # 删除左侧空格
print(f"name:{lastName.rstrip()} length: {lastName.rstrip().__len__()}") # 删除右侧空格
print(f"name:{fullName.strip()} length: {fullName.strip().__len__()}") # 删除左右空格

message = "removeprefix"
print(message.removeprefix("remove")) # 移除前缀
message = "removeremoveprefix"
print(message.removeprefix("remove")) # 移除前缀
message = "removesuffix"
print(message.removesuffix("suffix")) # 移除后缀
message = "removesuffix.jpg.jpg"
print(message.removesuffix(".jpg")) # 移除后缀

message = "Life's pathetic, let's pythonic."
print(message)
message = 'Life\'s pathetic, let\'s pythonic.'
print(message)

print("Hellp" + "Python") # 字符串拼接
print(("Hellp" + "Python") * 3) # 字符串重复

print(1)
print(123456789)
print(0.5)
print(123_4_5_678912345.0)

print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 ** 3) # // 表示乘方运算 8
print(2 ** 4) # // 表示乘方运算 16
print(2 / 3)
print(2 // 3) # // 表示整数除法 0
print(3 // 3) # // 表示整数除法 1
print(5 // 3) # // 表示整数除法 1
print(6 // 3) # // 表示整数除法 2
print(True)
print(False)
x,y,z = 1,2,3
print(f"{x} {y} {z}")

print(type(x)) # 变量类型
print(type(True)) # 变量类型

fruit = ['apple','banana','orange']
print(fruit.__sizeof__()) # 字节 72
print(fruit.__len__()) # 长度 3
print(len(fruit)) # 长度 3
print(type(fruit)) # 变量类型
print(f"first:{fruit[0]} last:{fruit[-1]}") # 下标，负数倒叙
print(f"last:{fruit[fruit.__len__() - 1]}") # 下标，负数倒叙
print(f"first:{fruit[-fruit.__len__()]}") # 下标，负数倒叙
print(f"\n{fruit}\n")
fruit.append('peach') # 添加
print(f"结尾添加 {fruit}\n")
fruit.insert(0, 'grape') # 插入
print(f"起始位置插入 {fruit}\n")
del fruit[0] # 删除
print(f"删除 del fruit[0]，删除后 {fruit}\n")
element = fruit.pop(2) # 删除并返回指定索引的元素，默认最后一个
print(f"删除 pop（2）: {element} 删除后{fruit}\n")
fruit.remove(fruit[0])
print(f"remove(0) 删除后：{fruit}\n")

numbers = [2,5,8,3,6,9,1,4,7]
print(f"numbers: {numbers}\n")
numbers.sort()
print(f"numbers.sort(), numbers2:{numbers}\n")

numbers2 = [2,5,8,3,6,9,1,4,7]
print(f"numbers2: {numbers2}\n")
numbers3 = sorted(numbers2)   
print(f"numbers3=sorted(numbers2)=:{numbers3}\n")
print(f"numbers2:{hex(id(numbers2))} numbers3:{hex(id(numbers3))}\n")

# 列表操作
for f in fruit: # 只要后续代码保持缩进，人以空格都行，可写很多行代码，直到不再缩进
    print(f"{f}")
    print("。。。")
    print("\n")
print("\n")

range5 = range(5)
print(f"range5:{range5}")

print("\nfor value in range(3):")
for value in range(3):
    print(value)

print("\nfor value in range(1, 3):")
for value in range(1, 3):
    print(value)

print("\nfor value in range(1, 8, 3):")
for value in range(1, 8, 3):
    print(value)
print("\n")
#利用列表推导式直接生成列表
squars = [value**2 for value in range(1,9)]
print(f"推导式 squars =[value**2 for value in range(1,9)]=:{squars}  hex:{hex(id(squars))}\n")
#切片操作总是返回列表的拷贝，所以可以根据原列表创建新列表，深拷贝
squars2 = squars[:]
print(f"squars2 = squars[:]=:{squars2}  hex:{hex(id(squars2))}")
print(f"squars[0:3]:{squars[0:3]}\n") # 取列表中一段数据
print(f"squars[:3]:{squars[:3]}\n") # 取列表中一段数据
print(f"squars[3:]:{squars[3:]}\n") # 取列表中一段数据
print(f"squars[-3:]:{squars[-3:]}\n") # 取列表中一段数据


# 元组，不可改变元素
tuple = ("Pyrhon",1,"Hello")
print(f"元组 tuple:{tuple}\n")
print(f"tuple[0]:{tuple[0]}\n")
(d,m) = divmod(10,3)
print(f"divmod(10,3):{d} {m}\n")

# if:  elif: else:
# 条件测试表达式：一个值为 True 或 False 的表达式
# == 、 != 、 in 、 not in
for n in numbers:
     if n == 3:
         print(f"找到数字3,，退出循环\n")
         break
     else:
         print(f"不是数字3\n")

print(f"3 in {numbers}:{3 in numbers}\n")
print(f"0 not in {numbers}:{0 not in numbers}\n")
print(f"numbers == numbers2:{numbers == numbers2}\n")
print(f"numbers2 == numbers3:{numbers2 == numbers3}\n")
print(f"numbers == numbers3:{numbers == numbers3}  {numbers}-{hex(id(numbers))}  {numbers3}-{hex(id(numbers3))}\n")
print(f"hex(id(numbers)) == hex(id(numbers3)):{ {hex(id(numbers))} == {hex(id(numbers3))}}\n")
if numbers==numbers2:
    print("numbers==numbers2\n")
elif numbers==numbers3:
    print("numbers==numbers3\n")
else:
    print("numbers!=numbers2 , numbers!=numbers3\n")

emptyList = []
if emptyList:
    print(f"emptyList:{emptyList} is not empty\n")
else:
     print(f"emptyList:{emptyList} is empty\n")    
# Python 中没有三目运算符，替代方案: x = 值1 if 条件 else 值2
score = int(random()*100)
rate = "A" if score >= 90 else "B" if score >= 80 else "C" # 从左往右判断
fixScore = (90 if score >= 90 else 80 if score >= 80 else score) + 10 # 优先级低于算术运算符
print(f"score:{score}, rate:{rate}, fixScore:{fixScore}\n")

# 推导式
squars2 = [value**3 for value in range(1,9) if value < 5] # 过滤
print(f"推导式:{squars2}\n")

# 推导式
filterSquars = [x if x > 36 else int(math.sqrt(x)) for x in squars]
print(f"推导式:{filterSquars}\n")

# match case
match score%4:
    case 0:
        print(f"整除 4 \n")
    case 1:
        print(f"整除 4  余 1\n")
    case 2:
        print(f"整除 4  余 1\n")
    case N: # 兜底 ，
        print(f"兜底,整除 4  余 {N}\n")

# 字典 obj[key] 如果 key 不存在则会报错，推荐使用 get(key, default) 方法
obj = {'from':"China",'age':20,'name':'张三','hobbies':['读书','游泳'],'detail':{'height':175,'weight':70}} 
print(f"{obj}\n") # 输出结果会将双引号变为单引号
print(f"from:{obj['from']}\n")
print(f"detail:{obj['detail']}\n")
print(f"height:{obj['detail']['height']}\n")
print(f"hobbies:{obj['hobbies']}\n")
print(f"hobbies[0]:{obj['hobbies'][0]}\n")
## print(f"unknown:{obj['unknown']}\n") # KeyError: 'unknown
print(f"unknown:{obj.get('unknown',"不存在该字段")}\n") # KeyError: 'unknown
obj["age"] = 25 # 已经存在则改变数据
print(f"改变数据：{obj}\n") 
obj["other"] = 'Other' # 不存在则新增字段
print(f"新增字段：{obj}\n") 
del obj['other']
print(f"删除字段：{obj}\n") 
print(f"keys:{obj.keys()}\n")
print(f"values:{obj.values()}\n")
keys = obj.keys()
print(f"type(obj.keys()):{type(keys)}\n")
keyList = list(keys)
print(f"type(keyList):{type(keyList)}\n")
print(f"keyList:{keyList}\n")
for k,v in obj.items(): # 元组取值
    print(f"{k} {v}\n")
print(f"\n")
