# •应使用两个空行分开不同的函数块（书中代码限于版面限制未全做到）
# •所有的 import 语句都应放在文件开头，唯一的例外是，你要在文件开头使用注释来描述整个程序。


# 函数编写指南函数编写指南
# •要给函数和模块一个描述性名称，且只使用小写字母和下划线。
# •每个函数都应包含简要阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串的格式。
# •给形参指定默认值和调用函数传入实参时，等号两边不要有空格：
def example(p0, p2='default value'):
    """... """


example('value0', p2='value1')


# 当代码过长时，为了能让别人在编辑器窗口易于查看整行代码：
# •应该在函数定义中，输入左括号后按回车键，然后按两次制表符键（八个空格）
# •如果形参或实参的代码很长，应在合适的形参及其逗号后做同样的操作
# •大多数的编辑器会自动进行对齐，如果有则无需按两次制表符键。
def example2(parameter_0, parameter_1, parameter_2, parameter_3, parameter_4,
             parameter_5, parameter_6, parameter_7):
    """..."""


def printHello():
    """文档字符串（docstring）的注释：输出内容"""
    print("Hello")


printHello()


def printHello(username):
    """username:形参 parameter，即函数完成工作所需的信息"""
    print(f"Hello {username}")


printHello("张三")  # 张三:实参 argument，即在调用函数时传递的信息

# 函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参，Python 会将每个实参关联到函数定义中的一个形参上去。
# •传递位置实参：实参的顺序与形参的顺序相同；
# •传递关键字实参：其中每个实参数都以“变量名=值”形式传入；


def reduce(a, b):
    """a-b"""
    print(f"reduce {a}-{b} = {a-b}")


reduce(8, 3)
reduce(a=9, b=4)


def power(a, b=1):
    """a^b, 指定默认值,另外要注意，关键词实参必须在位置实参之后（申明、调用都如此）"""
    print(f"reduce {a}**{b} = {a**b}")


power(5, 3)
power(a=9)


def plus(a, b):
    """函数返回值,不指定类型,动态返回数据类型"""
    ab = a + b
    print(f"reduce {a}+{b} = {ab}")
    return ab if ab > 10 else "小卡拉米"


plus81 = plus(8, 1)
plus88 = plus(8, 8)
print(f"plus81: {plus81}  plus88:{plus88}")


def plus2(a, b) -> int:
    """函数返回值"""
    print(f"reduce {a} + {b} = {a + b}")
    return a + b


pl56 = plus2(5, 6)
print(f"pl56: {pl56}")

users = ['Tom', 'Jerry']


def greet(users: list):
    for u in users:
        print(f"Hello {u.title()}")
    users.append("Alice")  # 会修改传入的参数
    print(f"greet inner users:{users}")


greet(users)
print(f"outer users: {users}")
# 可以通过切片操作 [:] 将复制的列表副本传递给函数，以防止原列表被修改
greet(users[:])
print(f"outer users: {users}")


def printProfile1(*user):
    """任意数量的位置实参,打印用户信息"""
    print(user)  # ('张三', 18, '男')


def printProfile2(**user):
    """任意数量的关键字实参,打印用户信息。
    我们有时候需要接受任意数量的实参，但不知道信息是什么样的，例如用户会希望使用一些自定义信息来创建账户。
    双星号 ** 让 Python 创建一个名为 user_info 的字典，其中包含函数收到的所有（余下的）关键字实参。"""
    print(user)


printProfile1("张三", 18, '男')
printProfile2(name="张三", age=18,
              sex="男")  # {'name': '张三', 'age': 18, 'sex': '男'}


def buildProfile(first, last, **user):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user['firstName'] = first
    user['lastName'] = last
    return user


userZS = buildProfile(first='三', last='张', age=18, sex="男")
print(
    f"userZS buildProfile: {userZS}")  # {'name': '张三', 'age': 18, 'sex': '男'}

# 形参:
# • 仅限位置形参（Positional-Only Parameters）—— 用 / 标记
# • 仅限关键字形参（Keyword-Only Parameters）—— 用 * 标记， *用于隔挡， *跟参数名称时表示同时还接收剩余位置参数，如：*args
# 这两个是 Python 函数定义中用于控制传参方式的语法标记。
# 它们决定了调用函数时，参数是必须按位置传、必须按关键字传，还是两者皆可。

# 在函数定义的参数列表中：
# / 左边的所有参数 → 仅限位置（Positional-Only）
# * 右边的所有参数 → 仅限关键字（Keyword-Only）。 一旦使用了“关键字=值”的写法，它后面的所有参数也必须使用关键字形式，直到遇到 **kwargs 的捕获范围。
# 如果参数既不在 / 左边，也不在 * 右边，则既可按位置，也可按关键字（普通参数）。
# 一个函数可以同时使用 / 和 *，夹在中间的就是普通参数：

# 函数参数定义的唯一正确排列顺序如下（从左到右）：
# [仅限位置参数] → / → [位置或关键字参数]（即普通参数） → * 或 *args → [仅限关键字参数] → **kwargs
# 为了让你再也忘不掉，我画个“参数过安检”的流程图：
# 第一道门（/ 左边）：必须按顺序排队进，不能喊名字（仅限位置）。
# 第二道门（/ 和 * 之间）：既可以排队进，也可以喊名字进（普通参数）。
# 第三道门（* 右边）：必须喊名字才能进，不能插队（仅限关键字）。
# 最后的麻袋（**kwargs）：专门用来装所有喊了名字但前面没人认领的参数。

# 关键记忆点：
# 在参数列表中，/ 必须在 * 的前面（如果有的话）。
# 顺序永远是：[位置参数] → / → [普通参数] → *[分隔，可选参数名收集剩余位置参数] → [仅限关键字参数] → **kwargs[剩余关键字参数]。

# def 函数名(
#     仅限位置参数1,仅限位置参数n, /,
#     普通参数1, 普通参数n,
#     *args,           # args 捕获多余的位置参数， 或者孤零零的 *
#     仅限关键字参数1, 仅限关键字参数n,
#     **kwargs # 捕获多余的关键字参数
# ):


def normal(a, b):
    """普通形参，位置和关键字都可以"""
    return a + b


print(f"位置传入或者关键字传入：{normal(1, b=2)}")


def position(a, b, /):
    """位置形参，所有参数都是按顺序传入，不能通过关键字传入"""
    return a + b


# TypeError: position() got some positional-only arguments passed as keyword arguments: 'b
# # print(f"只能通过位置传入：{position(1, b=2)}")
print(f"只能通过位置传入：{position(1, 2)}")


def key(*, a, b):
    """参数只能通过关键字传入"""
    return a + b


# TypeError: key() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given
# # print(f"只能通过关键字传入：{key(1, b=2)}")
print(f"只能通过关键字传入：{key(a=1, b=2)}")


def func(a, b, /, c, d, *, e, f, **kwargs):
    # a, b: 仅限位置 (Positional-Only)
    # c, d: 位置或关键字 (Positional-or-Keyword) 即普通参数
    # e, f: 仅限关键字 (Keyword-Only)
    # kwargs: 捕获额外的关键字参数
    """..."""


def demo(pos1, pos2, /, normal1, normal2, *args, kw1, kw2, **kwargs):
    """
    参数拆解：
    - pos1, pos2：在 / 左边 → 仅限位置
    - normal1, normal2：在 / 和 * 之间 → 普通（位置或关键字皆可）
    - args：捕获多余的位置参数
    - kw1, kw2：在 * 右边 → 仅限关键字
    - kwargs：捕获多余的关键字参数
    """
    print(f"仅限位置: {pos1}, {pos2}")
    print(f"普通参数: {normal1}, {normal2}")
    print(f"多余位置: {args}")
    print(f"仅限关键字: {kw1}, {kw2}")
    print(f"多余关键字: {kwargs}")


# ---------- 正确的调用方式 ----------
demo(
    1, 2,  # pos1, pos2 必须按位置
    3, 4,  # normal1, normal2 可以按位置
    5, 6, 7,  # 被 *args 吃掉 (5,6,7)
    kw1=8,
    kw2=9,  # 必须用关键字
    extra='a')  # 被 **kwargs 吃掉

# 输出验证：
# 仅限位置: 1, 2
# 普通参数: 3, 4
# 多余位置: (5, 6, 7)
# 仅限关键字: 8, 9
# 多余关键字: {'extra': 'a'}

# 在 Python 的调用规则中，一旦使用了“关键字=值”的写法，它后面的所有参数也必须使用关键字形式，直到遇到 **kwargs 的捕获范围。因为 normal2=4 后面的 5,6,7 是纯位置参数，违背了这个规则。
# 这其实呼应了你之前学的“仅限关键字参数”：虽然 normal1 和 normal2 本身是灵活的，但调用时的顺序依然要遵循“所有位置参数必须排在所有关键字参数之前”的铁律。
# 以下写法不支持
# demo(1, 2, normal1=3, normal2=4, 5，6，7,kw1=8, kw2=9) 



# ----------------------作用域>>>>>>>>>>>>>>>只有 def（函数）、class（类）、lambda（表达式）会创建新的作用域。
# Python 查找变量时，遵循 LEGB 原则，从内到外一层层找，找不到就报 NameError：
# 层级	全称	说明	举例
# Local	局部作用域	函数内部定义的变量。	def foo(): x = 1 中的 x
# Enclosing	嵌套外层作用域	外层嵌套函数的局部作用域（闭包环境）。	def outer(): y=2; def inner(): ... 中的 y
# Global	全局作用域	当前模块（.py文件）顶层**定义的变量。	文件顶部的 x = 100
# Built-in	内置作用域	Python 内置的函数和异常名。	print()、len()、ValueError

x = 100  # 全局变量
print(f"x:{x}")


def test1():
    """在 Python 中，只要你在函数体内对某个变量进行了赋值（=），
    Python 就默认把它当作该函数的局部变量，除非你特意用关键字声明。
    看这个经典翻车案例"""
    print(x)  # ⚠️ 这里会报错吗？
    x = 200  # 这里对 x 赋值了
    # 调用 test1() 会抛出 UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
    # 原因：
    # 因为函数内有 x = 200，Python 在编译时就把 x 标记为“局部变量”。
    # 当执行 print(x) 时，局部变量 x 还没被赋值（赋值在后面），所以报错，它压根不会去看全局的 x=100。


def test2():
    """
    global 关键字（跳出函数，修改全局）
    在函数内部修改全局变量，必须先用 global 声明。
    """
    global x  # 声明：我要动的是全局的 x
    print(f"test2:{x}")  # 100
    x = 200  # 修改全局变量


test2()
print(f"after test2 x:{x}")  # 200 （全局被改了！）


def test3():
    """
    4. nonlocal 关键字（跳出局部，修改嵌套外层）
    nonlocal 是 global 的“近亲”，但它只用于嵌套函数中，用来修改外层嵌套函数（Enclosing）里的变量。
    """
    x = 10  # 这是外层局部变量
    print(f"test3 init x:{x}")

    def inner():
        """
        要改的是外层变量，
        nonlocal 不能用于全局变量，也不能用于内层函数中不存在的变量
        """
        nonlocal x  # 声明：我要改的是外层 outer 里的 x，不是全局的
        x += 1  # 修改外层变量
        print(f"test3 inner x:{x}")  # 11

    inner()
    print(f"test3 after inner x:{x}")  # 11 （外层确实被改了）


test3()
print(f"after test3 x:{x}")  # 200 （全局被改了！）


#
def test4():
    """
    if、for、while、with、try-except 不会创建新的作用域。在它们内部赋值的变量，在外部依然能访问。
    只有执行成功的赋值语句才会创建变量。所以，对于在 try 里赋值的变量，一定要在 except 或 else 或 try 之前给它一个“确定性”的归宿。
    """
    def testRaise():
        try:
            n1 = int('a') # ValueError: invalid literal for int() with base 10: 'a'
            return n1
        except:  # 捕获所有异常
            raise  # 重新抛出当前正在捕获的异常，向外抛出
            # raise NewError("msg") from e # 抛出一个新异常，并链式附加原始异常 e
            # raise ValueError("msg")
    try:
        n1 = testRaise()
    except ValueError as e:
        print(f"执行 testRaise 出错 {e}")
        # print(f"执行 testRaise 出错 {repr(e)}")
    else:
        print(f"执行 testRaise 成功,n1:{n1}")
    try:
         nFi = testRaise()
    except ValueError as e:
        # print(f"执行 testRaise 出错 {e}")
        print(f"执行 testRaise 出错 {repr(e)}")
        nFi = None
    finally:
        print(f"执行 testRaise finally, nFi:{nFi}")
        # UnboundLocalError: cannot access local variable 'nFi' where it is not associated with a value
    try:
        n2 = int('a')
    except ValueError:  # 捕获指定异常
        print(f"吃掉异常，不抛出")
        pass  # 吃掉异常
    # UnboundLocalError: cannot access local variable 'num' where it is not associated with a value
    # print(f"n2:{n2 if n2 else '输入内容不是数字'}")

    try:
        n3 = int(input('输入数字 n3:'))
    except ValueError:
        print(f"输入内容不是数字")
        pass
    else:
        print(f"输入内容是数字 n3:{n3}")

    try:
        n4 = int(input('输入数字 n4:'))
    except ValueError:
        n4 = None
        pass
    print(f"{'输入内容是数字' if n4 else "输入内容不是数字"} n4:{n4}")
    # 删除变量
    del n4 
    try:
        print(f"删除 n4,继续使用 :${n4}")
    except:
        print(f"继续使用删除了的变量 n4 出现异常")
    finally:
         print(f"继续使用删除了的变量 n4,finally")

test4()
