# 检查 python 文件类型定义是否正确： 
# 1.安装类型检查器能 mypy: pip install mypy
# 2.检查文件：python -m mypy py-learning/type-hints-demo.py

# 特别提示：如果你用的是 Python 3.9+，list、dict 等可以直接用小写泛型（如 list[int]），无需从 typing 导入 List；但 DefaultDict 仍需从 collections 或 typing 导入。
from collections import defaultdict, Counter
from typing import List, Dict, DefaultDict

# 1. 普通列表推导式的类型注解
numbers: List[int] = [1, 2, 3, 4]
n1: List[int] = [x**2 for x in numbers]

# 2. defaultdict 的类型注解（需要指明 key 和 value 的类型）
# 示例：键为 str，值为包含 int 的列表
d: DefaultDict[str, List[int]] = defaultdict(list)
d['group'].append(10)  # 新增一个 int 数据，以后新增数据，类型检查器能正确推断，类型错误则报错
d['group'].append(5)
d['group'].append(1)
d['group'].append(8)
print(f"d:{d}\n")
print(f"d.items:{d.items()}\n")
itemList: List[tuple[str, List[int]]] = list(d.items())
print(f"itemList:{itemList}\n")

tuple0: tuple[str, list[int]] = itemList[0]
print(f"tuple0:{tuple0}\n")

sortedItems: list[int] = sorted(tuple0[1], key=lambda kv: kv, reverse=True)
print(f"sortedItems:{sortedItems}\n")

countInitEmpty: Counter = Counter()
countInitStr: Counter[str] = Counter("Hello Python!")
print(f"countInitStr:{countInitStr}\n")