from collections import defaultdict, Counter

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

abCount1 = Counter(a=5, b=2)
abCount2 = Counter(a=3, b=4)
print(f"abCount1:{abCount1}\n")
print(f"abCount2:{abCount2}\n")
print(f"abCount1+abCount2:{abCount1 + abCount2}\n")
print(f"abCount1-abCount2:{abCount1 - abCount2}\n") # 不会出现负数

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
print(f"countInitEmpty.subtract(['banana'])， countInitEmpty:{countInitEmpty}\n") # Counter({'apple': 1, 'banana': 0, 'orange': 1})
countInitEmpty.subtract(['banana']) # 递减， 可到负数
print(f"countInitEmpty.subtract(['banana'])， countInitEmpty 22:{countInitEmpty}\n") # Counter({'apple': 1, 'orange': 1, 'banana': -1})
print(f"total:{countInitEmpty.total()}\n")

print(f"countInitEmpty:{countInitEmpty}\n")
countDict: Counter[str] = Counter({'apple':1,'banana':3,'orange':5})
print(f"countDict:{countDict}\n")
print(f"countDict+countInitEmpty:{countDict + countInitEmpty}\n")
print(f"countDict-countInitEmpty:{countDict - countInitEmpty}\n") # 不会出现负数