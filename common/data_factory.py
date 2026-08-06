"""测试数据工厂：保证用例自造数据、互不冲突、可并发。"""
import random
import string
import time
from typing import Optional


def unique_suffix() -> str:
    """时间戳 + 随机串，保证并发执行时不撞号。"""
    rand = "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{int(time.time() * 1000)}{rand}"


def work_order_no(prefix: str = "AT") -> str:
    return f"{prefix}-WO-{unique_suffix()}"


def fabric_payload(**overrides) -> dict:
    """织物工艺参数样例，真实项目请替换为脱敏生产数据。"""
    payload = {
        "material_code": f"FAB-{unique_suffix()}",
        "color_no": "C-1802",
        "gram_weight": 185.5,
        "width_cm": 150,
        "composition": "97%Cotton/3%Spandex",
    }
    payload.update(overrides)
    return payload


def work_order_payload(quantity: int = 100, line_code: str = "LINE-01", **overrides) -> dict:
    payload = {
        "order_no": work_order_no(),
        "material": fabric_payload(),
        "quantity": quantity,
        "line_code": line_code,
        "planned_date": time.strftime("%Y-%m-%d"),
    }
    payload.update(overrides)
    return payload


def report_payload(order_no: str, quantity: int, defect: Optional[int] = 0) -> dict:
    return {
        "order_no": order_no,
        "qualified_qty": quantity - (defect or 0),
        "defect_qty": defect or 0,
        "operator": "qa_bot",
        "barcode": f"BC{unique_suffix()}",
    }
