"""外部依赖挡板服务。

用途：
1. 让框架开箱即跑通，不依赖真实 MES/ERP；
2. 真实项目中替换为对海关、银行、第三方物流、产线设备（PLC/条码枪/织机）的挡板。

启动: python mock/mock_server.py
"""
from __future__ import annotations

import threading
import time
from typing import Any, Dict

from flask import Flask, jsonify, request

app = Flask(__name__)
_LOCK = threading.Lock()
_ORDERS: Dict[str, dict] = {}
_PROGRESS: Dict[str, dict] = {}
_ERP: Dict[str, dict] = {}
_TOKEN = "mock-token"

ERP_SYNC_DELAY_SECONDS = 2.0


def ok(data: Any = None):
    return jsonify({"code": 0, "message": "success", "data": data})


def err(code: int, message: str, http_status: int = 200):
    return jsonify({"code": code, "message": message, "data": None}), http_status


@app.post("/mes/auth/login")
def login():
    body = request.get_json(silent=True) or {}
    if not body.get("username") or not body.get("password"):
        return err(40100, "用户名或密码为空")
    return ok({"token": _TOKEN, "username": body["username"]})


@app.get("/mes/auth/me")
def me():
    return ok({"username": "qa_bot", "workshops": ["WS-KNIT-01", "WS-GARMENT-02"]})


@app.post("/mes/work-orders")
def create_order():
    body = request.get_json(silent=True) or {}
    quantity = body.get("quantity", 0)
    if not isinstance(quantity, int) or quantity <= 0:
        return err(40001, "工单数量必须为正整数")
    if body.get("line_code") not in {"LINE-01", "LINE-02"}:
        return err(40404, "产线不存在")
    order = {**body, "status": "CREATED"}
    with _LOCK:
        _ORDERS[body["order_no"]] = order
        _PROGRESS[body["order_no"]] = {"reported_qty": 0, "qualified_qty": 0, "defect_qty": 0}
    return ok(order)


@app.get("/mes/work-orders")
def list_orders():
    planned_date = request.args.get("planned_date")
    line_code = request.args.get("line_code")
    with _LOCK:
        result = [
            o
            for o in _ORDERS.values()
            if (not planned_date or o.get("planned_date") == planned_date)
            and (not line_code or o.get("line_code") == line_code)
        ]
    return ok(result)


@app.get("/mes/work-orders/<order_no>")
def get_order(order_no: str):
    with _LOCK:
        order = _ORDERS.get(order_no)
    return ok(order) if order else err(40404, "工单不存在")


@app.post("/mes/work-orders/<order_no>/release")
def release_order(order_no: str):
    with _LOCK:
        order = _ORDERS.get(order_no)
        if not order:
            return err(40404, "工单不存在")
        order["status"] = "RELEASED"
    return ok(order)


@app.delete("/mes/work-orders/<order_no>")
def delete_order(order_no: str):
    with _LOCK:
        _ORDERS.pop(order_no, None)
        _PROGRESS.pop(order_no, None)
        _ERP.pop(order_no, None)
    return ok({"order_no": order_no})


@app.post("/mes/production/reports")
def scan_report():
    body = request.get_json(silent=True) or {}
    order_no = body.get("order_no")
    with _LOCK:
        progress = _PROGRESS.get(order_no)
        if progress is None:
            return err(40404, "工单不存在")
        qualified = body.get("qualified_qty", 0)
        defect = body.get("defect_qty", 0)
        progress["qualified_qty"] += qualified
        progress["defect_qty"] += defect
        progress["reported_qty"] += qualified + defect
    return ok({"report_id": f"RPT-{int(time.time() * 1000)}", "order_no": order_no})


@app.get("/mes/production/progress/<order_no>")
def progress(order_no: str):
    with _LOCK:
        data = _PROGRESS.get(order_no)
    return ok(data) if data is not None else err(40404, "工单不存在")


@app.get("/mes/production/loom-metrics")
def loom_metrics():
    line_code = request.args.get("line_code", "LINE-01")
    return ok(
        [
            {"line_code": line_code, "loom_id": "LM-001", "rpm": 620, "efficiency": 0.94},
            {"line_code": line_code, "loom_id": "LM-002", "rpm": 598, "efficiency": 0.91},
        ]
    )


@app.post("/mes/inventory/stock-in")
def stock_in():
    body = request.get_json(silent=True) or {}
    order_no = body.get("order_no")
    quantity = body.get("quantity", 0)
    with _LOCK:
        order = _ORDERS.get(order_no)
        if not order:
            return err(40404, "工单不存在")
        order["status"] = "FINISHED"
    # 模拟 ERP 异步同步延迟，用例必须用轮询等待而不是 sleep
    threading.Timer(
        ERP_SYNC_DELAY_SECONDS,
        _sync_to_erp,
        args=(order_no, quantity),
    ).start()
    return ok({"order_no": order_no, "quantity": quantity})


def _sync_to_erp(order_no: str, quantity: int) -> None:
    with _LOCK:
        _ERP[order_no] = {"order_no": order_no, "quantity": quantity, "source": "MES"}


@app.get("/mes/inventory")
def inventory_query():
    return ok([{"material_code": request.args.get("material_code"), "on_hand": 0}])


@app.get("/erp/health")
def erp_health():
    return ok({"status": "UP"})


@app.get("/erp/orders/<order_no>")
def erp_order(order_no: str):
    with _LOCK:
        data = _ERP.get(order_no)
    return ok(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9527, threaded=True)
