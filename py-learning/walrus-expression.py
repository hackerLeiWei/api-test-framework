"""海象表达式
    海象表达式 (walrus operator) := 是 Python 3.8 引入的一个新操作符，它的作用是“赋值表达式”（assignment expression）。
    它允许在表达式内部进行赋值操作，通常用于在 if 语句或循环中对变量进行赋值，同时使用该变量的值。
""" 
while (inputText := input("请输入内容 (输入quit退出): ")):
    if inputText == 'quit':
        print(f"\n")
        print(f"\n")
        break
    print(f"你输入了: {inputText}")

#导包方式 1: import random # 引用 random.randint(1,100)
from random import randint # 导包方式 2; 引用：randint(1, 100)


randomNumber =  f"当时值:{score}" if (score := randint(1, 100)) > 60 else f"随机数太小了:{score}"
print(f"海象表达式替代传统三目运算符, randomNumber: {randomNumber}")



"""推导式""" 
# 列表推导式
# 字典推导式
# 集合推导式
# 生成器表达式

list1 = [x for x in (1,2,3,4)]
print(f"list1: {list1}")

list2 = [x if x < 5 else ex**2 for x in range(1, 10) ]    
print(f"list2: {list2}")

