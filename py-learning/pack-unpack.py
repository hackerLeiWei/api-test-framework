"""
打包（Packing）和解包（Unpacking），在 Python 中指的是将多个值“聚合”为一个复合数据，以及将复合数据“拆分”并分配给多个变量的过程。
在你之前深究的 *args 和 **kwargs 中，其实你已经见过它们了：*args 就是把多余的位置参数打包成元组，而调用函数时 *list 则是把列表解包成位置参数。
为了让你彻底分清，我们把它们拆解为 4 个核心场景：
"""

# 赋值时的解包（最常用）

a, b = 1, 2  # <==> a=1,b=2
print(f"a:{a} b:{b}")
# 带星号 * 的贪婪解包（收集剩余项）
first, second, *others, last = [1, 2, 3, 4, 5, 6, 7]
print(f"first:{first} second:{second} others:{others} last:{last}")
print(f"others:{others}")
# 结合你学的“仅限位置参数”，这个特性在拆分固定长度数据时极好用
head, *other, tail = "Hello Python"
print(f"head:{head} other:{other} tail:{tail}")

# 函数定义时的打包（*args 和 **kwargs）


def pack(a, b, c, /, p1, p2, p3, *pack, key1, key2, **keyPack):
    """
    当你在定义函数时，在形参前加 * 或 **，就是在告诉 Python:“请把调用时传进来的多余参数，打包成一个整体给我”。
    关键记忆点（针对你之前的疑惑）：函数定义这里的 *args 就是打包操作符，它把 6,6,6 收进口袋里。而之前我们讨论的孤零零的 *（分隔符）不打包任何数据，只是划了一条线。
    a、b、c: 位置形参
    pack: 其他位置形参
    normal1、normal2: 位置形参 Or 关键字形参
    keyPack:关键字形参
    在 Python 的调用规则中，一旦使用了“关键字=值”的写法，它后面的所有参数也必须使用关键字形式，直到遇到 **kwargs 的捕获范围。
    """
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p3: {p3}")
    print(f"打包的位置参数 pack: {pack}")
    print(f"key1: {key1}")
    print(f"key2: {key2}")
    print(f"打包的关键字参数 keyPack: {keyPack}")


pack(1, 2, 3, 'P1', 'p2', 'p3', 6, 6, 6, key1='N2', key2='N1', x=9, y=8, z=7)
# 不支持
# pack(1, 2, 3,p1='P1',p2='p2',p3='p3', 6, 6, 6, key2='N2', key1='N1', x=9, y=8, z=7)

# 函数调用时的解包（反向操作）


def unpackAdd(a, b, c):
    """
    当你在调用函数时，在实参（可迭代对象/字典）前加 * 或 **，就是在告诉 Python:“请把这个容器里的元素拆开，一个一个地传给函数”。
    """
    return a + b + c


num = [2, 5, 8]
sunNum = unpackAdd(*num)
print(f"sunNum:{sunNum}")
# 不可新增其他参数 ,'d':20，TypeError: unpackAdd() got an unexpected keyword argument 'd'
data = {'a': 3, 'b': 6, 'c': 9}
sunData = unpackAdd(**data)
print(f"sunData:{sunData}")

# list 的合并
list1 = [1, 2]
list2 = [3, 4]
list3 = [*list1, *list2, 55]
print(f"list3: {list3}")  # [1, 2, 3, 4, 55]

# 字典的合并（解包展开）⚠️ 注意：如果键重复，后面的会覆盖前面的
d1 = {'a': 1, 'b': 2}
d2 = {'a': 'd2-a', 'c': 2}
d3 = d1 | d2  # {'a': 'd2-a', 'b': 2, 'c': 2}
print(f"d1: {d1}  d2: {d2}  d3: {d3}")
d4 = {**d1, **d2}  # {'a': 'd2-a', 'b': 2, 'c': 2}
print(f"d1: {d1}  d2: {d2}  d4: {d4}")


def plusABC(a, b, *, c):
    """
    场景 1/2: 孤零零的 *（分隔符） ———— 不打包，不解包，只是划界线(位置参数和关键字参数)
    a: 必须按位置参数
    c: 必须为关键字参数
    """
    return a + b + c


def plusFirstSecondLast(*args):
    """
    场景 2/2: 带*的参数 ———— 打包成元组，搬运数据
    a: 必须按位置参数
    c: 必须为关键字参数
    """
    print(f"plusFirstSecondLast args:{args}")
    # if (len(args) < 3):
    #     raise ValueError("args 至少需要3个元素")
    (a, b, *_, c) = args  # 解包成元组,优先保证 a、b 和 c 的赋值
    try:
        plus = args[0] + args[1] + args[-1]
    except ValueError:
        # 捕获底层异常，记录日志，再抛出自定义异常（异常链）
        raise RuntimeError() from e
    print(f"a:{a} b:{b} c:{c} plus:{plus}")
    return a + b + c


print(f"plusABC: {plusFirstSecondLast(*[3,5,6,7,8,2])}")  # 解包成元组
print(f"plusABC: {plusFirstSecondLast(*[3,5,6])}")  # 解包成元组
try:
    plus35 = plusFirstSecondLast(None)
    print(f"plusABC: {plus35}")  # 解包成元组
except ValueError as e:
    print(f"ValueError: {repr(e)}")
