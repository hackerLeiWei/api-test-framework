import math
from random import random
from operator import itemgetter
from collections import defaultdict, Counter

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
del fruit[0] # 有则删除，无则报错 IndexError
print(f"有则删除，无则报错 IndexError, del fruit[0]，删除后 {fruit}\n")
element = fruit.pop(2) # 删除并返回指定索引的元素，默认最后一个
print(f"删除 pop（2）: {element} 删除后{fruit}\n")
fruit.remove(fruit[0])
print(f"remove(0) 删除后：{fruit}\n")

numbers = [1,4,7,2,5,8,3,6,9]
print(f"numbers: {numbers}\n")
numbers.sort()
print(f"numbers.sort(), numbers2:{numbers}\n")

numbers2 = [1,4,7,2,5,8,3,6,9]
print(f"numbers2: {numbers2}\n")
#  sorted  接受任意可迭代对象，返回新的 list，原对象不变。
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

print(f"numbers:{numbers}\n")
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
squars2 = [value**2 for value in range(1,9) if value < 5] # 过滤
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
obj = {'from':"China",'age':20,'name':'张三','hobbies':['Swimming','Reading',"Listen to music","Play games"],'detail':{'height':175,'weight':70}} 
print(f"{obj}\n") # 输出结果会将双引号变为单引号
print(f"from:{obj['from']}\n")
print(f"detail:{obj['detail']}\n")
print(f"height:{obj['detail']['height']}\n")
print(f"hobbies:{obj['hobbies']} len:{len(obj['hobbies'])}\n")
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
print(f"keys:{keys}")
print(f"type(keys):{type(keys)}")
print(f"list(keys):{list(keys)}")
print(f"type(list(keys)):{type(list(keys))}\n")
for k,v in obj.items(): # 元组取值
    print(f"key:{k} value:{v}")
print(f"\n")

obj2 = {'from':"America",'age':15,'name':'Si Li','hobbies':['Swimming','Reading',"Listen to music","Play basketboll"],'detail':{'height':185,'weight':80}} 
obj_fromKeys1 = obj2.fromkeys(['from','age','name'])
obj_fromKeys2 = dict.fromkeys(['from','age','name'])
print(f"obj_fromKeys1:{obj_fromKeys1}\n")
print(f"obj_fromKeys2:{obj_fromKeys2}\n")
# dict.fromKeys , fromkeys 是 dict 的类方法（classmethod），跟 obj2 里的数据毫无关系。写成 dict.fromkeys([...]) 效果完全一样，
# 用实例来调只是语法上允许，容易误导人。而且它返回新字典，obj2 本身不变。
# 第二个参数是默认值，大坑：默认值是同一个对象被所有键共享，可变类型会互相影响：
objFromKeys = dict.fromkeys(['from','age','name'], [])
print(f"objFromKeys:{objFromKeys}")
objFromKeys['from'].append('China')
print(f"from key append China, objFromKeys:{objFromKeys}\n")
# 如果需要每个键对应自己独立的对象，可以使用字典推导式：
objFromKeysSelf= {key:[] for key in ['from','age','name']}
objFromKeysSelf['from'].append('China')
objFromKeysSelf['from'].append('America')
print(f"from key append China and America, objFromKeysSelf:{objFromKeysSelf}\n")
# 拷贝对象所有字段的数据
objChild1 = {k:obj2[k] for k in obj2.keys()}
print(f"objChild1 of obj2:{objChild1}\n")
# 取对象部分字段的数据
objChild2 = {k: obj2.get(k) for k in ['from','age','name']}
print(f"objChild2 of obj2:{objChild2}\n")

obj2Copy = obj2.copy()
print(f"obj2Copy:{obj2Copy}\n")
obj2Copy.clear()
print(f"clear obj2Copy:{obj2Copy}\n")

dictObj = {k:obj2.get(k, ['Swimming','Reading','Coding']) for k in ['from','age','name','hobbiesFix']}
print(f"dictObj:{dictObj}\n")
# get(k,default) 有键则返回该字段的值；无键则返回 default 且不会写入， 不会跟 [k] 一样报错
hobbies = dictObj.get('hobbies',['Unset'])
hobbiesFix = dictObj.get('hobbiesFix',['Unset'])
print(f"hobbies:{hobbies}\n")
print(f"hobbiesFix:{hobbiesFix}\n")
# set(k,default) 有键则返回该字段的值，不写入；无键则写入 default 并返回
setAge = dictObj.setdefault('age',30) # 有键则返回该字段的值，不写入
print(f"setAge:{setAge}\n")
setDetailHeight = dictObj.setdefault('detail',{'height':177}) # 无键则写入 default 并返回
print(f"setDetailHeight:{setDetailHeight}\n")

dict2 = {'k1':'v1','k2':'v2'}
print  (f"dict2:{dict2}")
dict2.pop('k1')
print  (f"dict2 after pop:'k1':{dict2}")
## dict2.pop('k3') # 第二个参数是默认值，如果键不存在，返回默认值且不报错，不存在则报错：KeyError: 'k3'
popK3 = dict2.pop('k3','default') # 第二个参数是默认值，如果键不存在，返回默认值且不报错
print  (f"dict2 after pop:'k3':{dict2}  popK3:{popK3}\n")
popItem = dict2.popitem() #删并返回最后插入的 (k,v)，空字典报错
print  (f"dict2 after popitem():{dict2}  popItem:{popItem}\n")
dict2.update(dictObj) # 合并另一个 dict 或 [(k,v),...]，同键覆盖
print(f"dict2 update dictObj, dict2:{dict2}\n")
dict2.clear()
print(f"clear dict2:{dict2}\n")
dict2.update([('k1','v1'),('k2','v2')])
print(f"有则更新，无则新增[('k1','v1'),('k2','v2')], dict2:{dict2}\n")
dict2.update(k1 = 'v1 single') # 有则更新，无则新增
print(f"有则更新，无则新增(k1 = 'v1 single'), dict2:{dict2}\n")
dict2.update(k3 = 'v3 single') # 有则更新，无则新增
print(f"有则更新，无则新增 (k3 = 'v3 single'), dict2:{dict2}\n")

## dict2.update(from = '关键字，不能这样更新')
dict2.update(**{'from': 'America'})    # 可以，from 是关键字但这样绕过去了,没有则新增
print(f"更新 Python 关键字 from 的值为 'America',有则更新，无则新增 dict2:{dict2}\n")
dict2.update([('from','America 2')]) # 有则更新，无则新增
print(f"有则更新，无则新增[('from','America 2')], dic2:{dict2}\n")


del dict2['k1'] # 有则删除，无则报错 KeyError
print(f"有则删除，无则报错 KeyError['k1'], dict2:{dict2}\n")
dict2['k1'] = 'k1 new' # 有则更新，无则新增
dict2['k2'] = 'k2 new' # 有则更新，无则新增
print(f"有则更新，无则新增['k1']='k1 new', 有则更新，无则新增['k2']='k2 new', dict2:{dict2}\n")


dictA = {'name':'dictA','attrA':'A'}
dictB = {'name':'dictB','attrB':'B'}
dictC = dictA | dictB
print(f"dictA:{dictA}")
print(f"dictB:{dictB}")
print(f"dictA | dictB 合并，相同字段后者覆盖前者， dictC:{dictC}\n")
print(f"idA:{hex(id(dictA))},idB:{hex(id(dictB))},idC:{hex(id(dictC))}\n")
dictA |= dictB
print(f"dictA |= dictB,等价于update, dictA:{dictA}\n")

dictNum = {k : k**2 for k in range(1,6)}
print(f"dictNum:{dictNum}\n")
dictNum2 = {k : k**2 for k in (1,6,4,5,3,2)}
print(f"dictNum2:{dictNum2}\n")

print(f"\n")
print(f"\n")
print(f"\n")

# 返回元组的第二个元素（即字典的值）
def lambdaReplace(item):
    return item[1]
#  sorted(iterable, *, key=None, reverse=False)   
# iterable：接受任意可迭代对象，返回新的 list，原对象不变。
# key：一个函数，对每个元素算出「用来比较的值」，只调用一次（不是两两比较），只是取值。
sorted_dictNum2 = sorted(dictNum2.items(), key=lambda kv: kv[1], reverse=True)  # 按值排序， key=lambda kv: kv[1] 返回元组的第二个元素（即字典的值）
print(f"sorted_dictNum2:{sorted_dictNum2}\n")
sorted_dictNum3 = sorted(dictNum2.items(), key=lambdaReplace, reverse=False)  # 按值排序， key=lambda kv: kv[1] 返回元组的第二个元素（即字典的值）
print(f"sorted_dictNum3:{sorted_dictNum3}\n")
sorted_dictNum4 = sorted(dictNum2.items(), key=itemgetter(1), reverse=False)  # 按值排序， key=lambda kv: kv[1] 返回元组的第二个元素（即字典的值）
print(f"sorted_dictNum4:{sorted_dictNum4}\n")
{v: k for k, v in dictNum2.items()} # 键值反转
max(dictNum2, key=dictNum2.get) # 值最大的键
{k: v for k, v in dictNum2.items() if v} # 过滤

print("for k ,v in  dictA.items()\n")
for k ,v in  dictA.items():
    print(f"k:{k} v:{v}")
print("\n")
sortedTupleAcb = sorted(('a','c','b'))
print(f"sortedTupleAcb:{sortedTupleAcb}\n")
sortedTuple312 = sorted((3,1,2))
print(f"sortedTuple312:{sortedTuple312}\n")
sortedList312 = sorted([3,1,2])
print(f"sortedList312:{sortedList312}\n")
dictAcb = {'a':'AA','c':'CC','b':99}
sortedDictAcb = sorted(dictAcb) # 字典只排键，忽略值，返回 list 键
print(f"dictAcb:{dictAcb}  sortedDictAcb:{sortedDictAcb}\n")


# defaultdict  自动建默认值，比 setdefault 干净。
# defaultdict 是 collections 模块提供的一个字典子类，它会在访问不存在的键时自动调用一个“工厂函数”来生成默认值，从而避免 KeyError
# defaultdict 的第一个参数必须是 可调用对象（callable），例如：
# list、int、dict 等内置类型（它们都是可调用的）
# 自定义函数或 lambda 表达式
# 或者 None（此时与普通字典行为相同）
initDictNone = defaultdict(None)
initDictNone['a'] =  {'from':'America','age':15,'name':"Si Li"}
initDictNone['c'] = 'C'
print(f"initDictNone:{initDictNone}\n")

initDictInt = defaultdict(int)
initDictInt['a'] +=1 # initDictInt['a'] 默认值为 0 
print(f"initDictInt:{initDictInt}\n")

initDictDict = defaultdict(dict)
initDictDict['user']['from'] = 'China'
initDictDict['user']['age'] = '20'
initDictDict['user']['name'] = 'San Zhang'
initDictDict['other'] = {'from1':'America','age1':15,'name1':"Si Li"}
print(f"initDictDict:{initDictDict}\n")

initDictList = defaultdict(list)
initDictList[0].append({'from':'America','age':15,'name':"Si Li"})
initDictList[1].append(20)
initDictList[2].append(30)
print(f"initDictList:{initDictList}\n")
set2 = initDictList.setdefault(2,{'San'})
print(f"set2:{set2}\n")  # 有键则返回该字段的值，不写入
initDictList.setdefault(3,{'Zhang'})
print(f"initDictList:{initDictList}\n")

numbers1 = [1,2,2,3,3,3,5,5,5,5,5,8,8,8,8,8,8]
numberCount1 = Counter(numbers1)
print(f"numbers1:{numbers1}\n")
print(f"numberCount1:{numberCount1}\n")

# 方式1：从列表统计
numbers2 = [1,2,3,4,6]
numberCount2 = Counter(numbers2)
print(f"numbers2:{numbers2}\n")
print(f"numberCount2:{numberCount2}\n")

# Counter 支持 +、-、&（交集，取较小值）、|（并集，取较大值）
plusCount = numberCount1 + numberCount2
print(f"numberCount1 + numberCount2 plusCount:{plusCount}\n")
reduceCount = numberCount1 - numberCount2
print(f"numberCount1 - numberCount2 reduceCount:{reduceCount}\n")
print(f"reduceCount.elements:{reduceCount.most_common(4)}\n") # 获取出现次数最多的前 n 个（返回元组列表）
print(f"reduceCount.elements:{reduceCount.elements()}\n")

abCount1 = Counter(a=1, b=2)
abCount2 = Counter(a=3, b=4)
print(f"abCount1:{abCount1}\n")
print(f"abCount2:{abCount2}\n")
print(f"abCount1+abCount2:{abCount1 + abCount2}\n")
print(f"abCount1-abCount2:{abCount1 - abCount2}\n")

# 方式2：从字符串统计字符
sNumber = '1223388888'
sNumberCount = Counter(sNumber)
print(f"sNumber:{sNumber}\n")
print(f"sNumberCount:{sNumberCount}\n")
# 方式3：手动更新
countInitEmpty = Counter()
countInitEmpty['apple'] += 1   # 即使 'apple' 不存在，也不会报错，默认从 0 开始
print(f"countInitEmpty['apple'] += 1， countInitEmpty:{countInitEmpty}\n") #Counter({'apple': 1})
countInitEmpty.update(['banana', 'orange']) # 累加
print(f"countInitEmpty.update(['banana', 'orange'])， countInitEmpty:{countInitEmpty}\n") #Counter({'apple': 1, 'banana': 1, 'orange': 1})
countInitEmpty.subtract(['banana']) # 递减
print(f"countInitEmpty.subtract(['banana'])， countInitEmpty:{countInitEmpty}\n") #Counter({'apple': 1, 'banana': 0, 'orange': 1})
print(f"total:{countInitEmpty.total()}\n")



# userA = {'name':'未知','age':'未知','from':'未知'}
# print(f"userA: {userA}\n")
# userA['name'] = input('请输入名称：')
# userA['age'] = input('请输入年龄：')
# userA['from'] = input('请输入来自地方：')
# print(f"userA: {userA}\n")

# # 猜数字
# answerCount = 1
# while True:
#     n = int(input(f"请猜分数{score}:"))
#     if score == n:
#         print(f"猜对了\n")
#         break
#     else :
#         if score > n:
#             print(f"偏小，请继续，还有{8 - answerCount}次机会\n")
#         else:
#             print(f"偏大，请继续，还有{8 - answerCount}次机会\n")
#         answerCount += 1
#         if answerCount > 8:
#             print(f"你已经没有机会了\n")
#             break

# # 海象运算符（表达式）：赋值 + 返回值
# 海象运算符赋值的变量，遵循 LEGB 作用域规则。在 if、while、推导式等子句中，变量会被提升到所在函数或全局作用域。
# while (n := input(f"请输入海象运算符:")) != '海象运算符':
#     print(f"你输入的是: {n}")

# while (s := input(f"请输入,退出(quit):")) != 'quit':
#     print(f"你输入的是: {s}")
print(f"numbers:{numbers}\n")
n1 = [x**2 for x in numbers] # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(f"n1:{n1}\n")
n2 = [y for x in numbers if (y := x**2) > 10] # y= 16 , 后续的 y 会共享此 y, [16, 25, 36, 49, 64, 81]
print(f"n2:{n2}\n")

# Python 解析列表推导式的顺序是：先判断 if，再计算左侧表达式。
# x=1：判断 if y > 10，此时全局 y=16，条件为 True。执行 y := 1**2，将 y 重新赋值为 1，并将 1 加入 n2。
# x=2：判断 if y > 10，此时全局 y 已被改为 1，条件为 False。跳过，不执行赋值。
# x=3：判断 if 1 > 10，为 False，跳过。
# x=4：判断 if 1 > 10，为 False，跳过。
# 正确的海象用法永远是 n3 这种：把 := 放在条件 if 的括号里，确保“赋值”发生在“判断”之前，且不依赖任何外部状态。
n3 = [y := x**2 for x in numbers if y > 10]
print(f"n3:{n3}\n") # [1]
# 
# 
#  假设要将列表中的数字取平方，但只保留结果 > 10 的：
data = (xxx:=3)
print(f"data:{data}\n")

if (xxx:=3):
    print("(xxx:=3)\n")
yyy = 44 if (xxx:=4) else 55
print(f"(yyy:{yyy}\n")
yyy2 = xx2 if (xx2:=4) else 55
print(f"(yyy2:{yyy2}\n")
operators = ['+=','-=','*=','/=','continue','**=','//=','%=','break','other']
idx = 0
while idx < len(operators):
    match operators[idx]:
        case 'continue':
            print(f"do continue")
            idx += 1
            continue
        case 'break':
            print(f"do break")
            break
        case _:
            print(f"operators[{idx}]: {operators[idx]}")
            idx += 1

if 1:
    print(f"AAAAAAAAA 1\n")

if 0:
    print(f"AAAAAAAAA 0\n")
else:
     print(f"AAAAAAAAA !0\n")

if '':
    print(f"BBBBBBBBB 空字符串\n")
else:
    print(f"BBBBBBBBB ! 空字符串\n")

if  1 > 0:
    print(f"CCCCCCCC 1 > 0\n")



print(f"\n")
print(f"\n")
print(f"\n")
print(f"\n")
print(f"\n")
print(f"\n")    