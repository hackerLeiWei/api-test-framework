"""轮询等待，替代 time.sleep。"""
import time
from typing import Callable, Optional, TypeVar

T = TypeVar("T")


def wait_until(
    condition: Callable[[], Optional[T]],
    timeout: float = 30.0,
    interval: float = 1.0,
    desc: str = "条件满足",
) -> T:
    """轮询直到 condition 返回真值，超时抛 AssertionError。

    用于异步链路：报工写库、MQ 消费、ERP 同步等。
    """
    deadline = time.monotonic() + timeout
    last_error: Optional[Exception] = None
    while time.monotonic() < deadline:
        try:
            result = condition()
            if result:
                return result
        except Exception as exc:  # noqa: BLE001 - 轮询期间的瞬时异常允许重试
            last_error = exc
        time.sleep(interval)
    raise AssertionError(f"等待「{desc}」超时（{timeout}s）" + (f"，最后一次异常: {last_error}" if last_error else ""))
