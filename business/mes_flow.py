"""业务封装层：把多个接口组合成有业务语义的动作。

用例层只调这里，不直接调 api 层。
"""
from typing import Optional

import allure

from api.mes.inventory_api import InventoryApi
from api.mes.production_api import ProductionApi
from api.mes.work_order_api import WorkOrderApi
from common.assertions import assert_biz_success
from common.data_factory import report_payload, work_order_payload
from common.http_client import HttpClient
from common.waiter import wait_until


class MesFlow:
    def __init__(self, client: HttpClient) -> None:
        self.work_order = WorkOrderApi(client)
        self.production = ProductionApi(client)
        self.inventory = InventoryApi(client)

    @allure.step("创建并下达工单")
    def create_released_work_order(self, quantity: int = 100, **overrides) -> dict:
        payload = work_order_payload(quantity=quantity, **overrides)
        created = assert_biz_success(self.work_order.create(payload)).data
        assert_biz_success(self.work_order.release(created["order_no"]))
        return created

    @allure.step("扫码报工")
    def scan_report(self, order_no: str, quantity: int, defect: Optional[int] = 0) -> dict:
        payload = report_payload(order_no, quantity, defect)
        return assert_biz_success(self.production.scan_report(payload)).data

    @allure.step("等待工单进度达到目标数量")
    def wait_progress(self, order_no: str, expected_qty: int, timeout: float = 30.0) -> dict:
        def reached():
            progress = self.production.get_progress(order_no).data
            return progress if progress.get("reported_qty", 0) >= expected_qty else None

        return wait_until(reached, timeout=timeout, desc=f"工单 {order_no} 报工数达到 {expected_qty}")

    @allure.step("完工入库")
    def stock_in(self, order_no: str, quantity: int) -> dict:
        return assert_biz_success(self.inventory.stock_in(order_no, quantity)).data

    @allure.step("清理工单")
    def cleanup(self, order_no: str) -> None:
        self.work_order.delete(order_no)
