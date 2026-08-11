


list1 = [ x for x in range(6)]
print(f"列表推导式 list1: list1\n")
dict1 = {x: x**2 for x in range(6)}
print(f"字典推导式 dict1: dict1\n")
collection1 = {x**3 for x in range(6)}
print(f"集合推导式（自动去重）collection1: collection1\n")
generatorExpression = (x for x in range(6))
print(f"生成器表达式，生成器对象（惰性计算，省内存）: {generatorExpression}\n")

tuple1 = tuple(x for x in range(6))
print(f"元组推导式 tuple1: {tuple1}\n")

if 0:
    print(f"if 0, run\n")
else:
    print(f"if !0, run\n")
# 过滤条件， if 置于末尾，用于筛选，保留满足条件的
list2 = [x for x in range(6) if x % 2 == 0]
print(f"列表推导式 range(6) if x % 2 == 0, list2 : {list2}\n")
list3 = [x for x in range(6) if x % 2 == 1]
print(f"列表推导式 range(6) if x % 2 == 1, list3 : {list3}\n")
# 过滤条件， if 置于前面，用于对数据分类
list4 = [x**2 if x % 2 == 0 else x**3 for x in range(6)]
print(f"x**2 if x % 2 == 0 else x**3 for x in range(6),list4:{list4}")
# 嵌套循环
zip = [[1,2],[3,4]]
flat = [f for row in zip for f in row]
print(f"flat:{flat} {type(flat)}") #flat:[1, 2, 3, 4] <class 'list'>