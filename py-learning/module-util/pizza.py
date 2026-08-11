
# 将函数存储在模块中
# 使用函数的优点之一是可将代码块与主程序分离，通过给函数指定描述性名称（并提供文档字符串），能让程序容易理解得多。
# 你还可以更进一步，将函数存储在称为模块（module）的独立文件中，再将模块导入（import）主程序。
# import 语句可让你在当前运行的程序文件中使用模块中的代码。

def mkPizza(size, *topics):
    """概述要制作的披萨"""
    print(f"\n- Making a {size}-inch pizza with the following toppings:")
    for topic in topics:
        print(f"- {topic}")


def sayPizza():
    print(f"Hello Pizza")
