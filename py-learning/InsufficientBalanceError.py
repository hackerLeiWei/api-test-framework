# 1. 定义自定义异常（通常只需写 pass，或重写 __init__）
class InsufficientBalanceError(Exception):
    """账户余额不足异常"""

    def __init__(self, balance, amount):
        """
        当你写 class MyClass: def __init__(self, ...): 时，__init__ 负责在实例被创建后立即初始化属性。
        __init__ 对象的“构造函数”,不负责创建对象（创建对象是 __new__ 干的），它只负责给创建好的对象“填充数据”。
        __init__ 属于面向对象（OOP），负责“对象的诞生”（初始化）
        """
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足，当前余额:{self.balance},需要支付:{self.amount}")


# 2. 在业务逻辑中抛出（结合你学的打包/解包，这里参数传递很清晰）
def withDraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance=balance, amount=amount)
    return balance - amount


# 3. 调用方捕获（结合你学的 try-except 获取异常信息）
try:
    balance = withDraw(150, 200)
    print(f"支付成功，余额：{balance}")
except InsufficientBalanceError as e:
    print(f"异常提示: {e}")
    print(f"还能自助取款吗？：{e.balance>=100}")
