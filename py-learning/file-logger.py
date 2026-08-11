import logging
import traceback

"""
实战：写一个“带异常日志”的文件上下文管理器
结合你学的 logging 和 traceback，这里展示 __exit__ 如何优雅地记录异常：
"""
class LoggedFile:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        
        if exc_type is not None:
            # 结合你学的获取异常信息（traceback.format_exc）
            logging.error(f"操作文件 {self.filename} 时发生异常：\n{traceback.format_exc()}")
            # 返回 False，让异常继续往上抛，不吞掉
            return False

# 使用
try:
    with LoggedFile("__init__and__exit__.py", 'r') as f:
        content = f.read()
        print(f"content:{content}")
except FileNotFoundError:
    print("外层业务处理：文件找不到，请检查路径")