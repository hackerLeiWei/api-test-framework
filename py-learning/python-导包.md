在 Python 中，不同文件之间引用方法（函数/类）的核心机制是 **模块（Module）** 和 **包（Package）** 的导入。所有导入都依赖于 Python 的搜索路径（`sys.path`）。

下面按最常见的文件组织结构，分 4 种场景详细讲解，并附上安全避坑指南。

### 场景一：同一目录下（平级文件）

这是最简单的情况。假设目录结构如下：

```
project/
├── a.py          # 被引用的文件
└── b.py          # 执行引用的文件
```

- **a.py** 内容：
  ```python
  def hello():
      print("Hello from A")
  ```

- **b.py** 引用方式（两种任选）：
  ```python
  # 方式 1：导入整个模块，调用时需加前缀
  import a
  a.hello()

  # 方式 2：直接导入具体方法，调用时无需前缀（推荐，更简洁）
  from a import hello
  hello()
  ```

> **注意**：运行 `b.py` 时，必须直接在 `project` 目录下执行（`python b.py`），不要跑到上一级目录去执行，否则会报 `ModuleNotFoundError`。

---

### 场景二：不同目录（子文件夹引用）

如果文件在子包（文件夹）里，需要在该文件夹下**包含 `__init__.py`** 文件（Python 3.3+ 即使可为空，也建议保留，以便明确标识为包）。

目录结构：
```
project/
├── main.py
└── utils/                # 子包
    ├── __init__.py       # 空文件即可
    └── tool.py           # 包含目标方法
```

- **tool.py** 内容：
  ```python
  def calculate(x):
      return x * 2
  ```

- **main.py** 引用方式：
  ```python
  # 导入子包中的模块
  from utils.tool import calculate
  print(calculate(10))

  # 或者
  import utils.tool
  print(utils.tool.calculate(10))
  ```
> **关键前提**：必须确保 `project` 目录在 Python 的搜索路径中。当你在 `project` 目录下执行 `python main.py` 时，该目录会自动加入路径，所以上述代码能正常工作。

---

### 场景三：引用父级目录或跨上级目录（相对导入）

当你需要在**包内部**的文件之间引用，且不希望写死绝对路径时，使用 **相对导入**（仅限在包内使用，不能作为顶层脚本直接运行）。

目录结构：
```
project/
├── main.py
└── libs/
    ├── __init__.py
    ├── mod_a.py
    └── sub/
        ├── __init__.py
        └── mod_b.py
```

假设 `mod_b.py` 想引用同级的 `mod_a.py` 或父级的 `mod_a.py`：

- **在 `mod_b.py` 中引用同包（同级）模块**：
  ```python
  from . import mod_a        # 一个点代表当前目录
  mod_a.func()
  ```

- **在 `mod_b.py` 中引用父级（上级）模块**：
  ```python
  from .. import mod_a       # 两个点代表上一级目录
  mod_a.func()
  ```

**⚠️ 致命陷阱**：**含有相对导入（`.` 或 `..`）的文件不能直接用 `python mod_b.py` 运行**，会报 `ImportError: attempted relative import with no known parent package`。必须将上级目录视为根包，用 `-m` 参数运行：
```bash
# 在 project 目录下执行
python -m libs.sub.mod_b
```

---

### 场景四：任意路径的引用（临时解决方案）

如果被引用的文件不在当前项目根目录下，或者在系统的 `PYTHONPATH` 之外，可以在代码中**动态添加路径**（仅应急使用，生产代码不推荐）。

```python
import sys
import os

# 将目标文件的父目录添加到搜索路径
target_path = os.path.join(os.path.dirname(__file__), '../other_folder')
if target_path not in sys.path:
    sys.path.append(target_path)

import some_module  # 现在可以正常导入了
```

---

### 避坑指南（必看）

| 常见错误 | 解决方案 |
| :--- | :--- |
| **ModuleNotFoundError: No module named 'xxx'** | 检查你是否在正确的目录下执行脚本；或者将项目根目录通过 `sys.path.append` 添加进去。 |
| **循环引用（A引用B，B引用A）** | 不要写在文件顶部。将其中一个引用**放在函数内部**（延迟导入），或者重构代码，把公共逻辑抽到第三个文件 `C.py` 中。 |
| **IDE 提示红色波浪线但运行正常** | 这是 IDE 的根目录识别问题。在 VS Code / PyCharm 中，将项目根目录标记为 **Sources Root**（右键 -> Mark Directory as）即可消除。 |
| **`__init__.py` 的作用** | 它不仅仅是标识包，还可以在该文件里写入 `__all__ = ['tool']`，来控制 `from utils import *` 时导入哪些模块。 |

### 总结一句话
- **平级**直接 `import 文件名`；
- **子目录**用 `from 文件夹.文件名 import 方法`；
- **包内跨级**用相对导入（`.` 和 `..`）但需用 `-m` 运行；
- **找不到**就用 `sys.path.append` 临时救急。

如果你能告诉我你的具体目录结构（文件在哪个文件夹，你在哪里执行命令），我可以针对你的情况直接写出精确的导入代码。😊