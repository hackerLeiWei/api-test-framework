class Resource:
    def __enter__(self):
        print("打开资源")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        __exit__:上下文管理器的“清理工”（资源释放）
        __exit__ 必须和 __enter__ 成对出现，定义在上下文管理器类中，专门配合 with 语句使用。
        它最强大的地方在于：它可以决定“是否吞掉” with 代码块里发生的异常！ 这正是结合你学的异常处理（try-except）的关键进阶点。
        exc_type: 异常类型（如 ValueError）
        exc_val: 异常实例（如 ValueError("msg")）
        exc_tb: 异常追踪信息（Traceback）
        """
        print("关闭资源（无论是否异常，都会执行）") # 这里相当于 try-finally 的 finally
        # 返回 False（或什么都不返回，默认就是 None），异常会继续往上抛
        # 如果 __exit__ 返回 True，则异常被彻底压制，外层 try-except 捕获不到这个异常。
        return False


# 调用
try:
    with Resource() as r:
        print("执行中...")
        raise ValueError("哎呀出错了")  # 故意报错
except ValueError as e:
    print(f"外层捕获到：{e}")

# 输出顺序：
# 打开资源
# 执行中...
# 关闭资源（无论是否异常，都会执行）  <-- 这里相当于 try-finally 的 finally
# 外层捕获到：哎呀出错了


print(f"\n")

class Suppressor:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"在上下文内部偷偷处理了异常：{exc_val}")
        return True  # 返回 True，表示“我已经搞定了，别往外抛了”

# 调用
try:
    with Suppressor() as s:
        raise RuntimeError("这是个严重错误")
    print("这行居然能执行？")  # 因为异常被吞了，所以能执行！
except RuntimeError as e:
    print("外层捕获不到任何东西！")  # 永远不会执行

# 输出：
# 在上下文内部偷偷处理了异常：这是个严重错误
# 这行居然能执行？