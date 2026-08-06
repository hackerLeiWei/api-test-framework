"""MES 冒烟用例：版本准入门禁。

要求：整体 5 分钟内跑完，任一条失败则版本退回，不启动回归。
条数控制在 10-20 条，不要膨胀。
"""
import time

import allure
import pytest

from common.assertions import assert_biz_success, assert_fields, assert_status

pytestmark = [pytest.mark.smoke, pytest.mark.mes, pytest.mark.p0]


@allure.feature("MES 冒烟")
class TestMesSmoke:
    @allure.story("登录态可用")
    def test_current_user(self, mes_client):
        from api.mes.auth_api import AuthApi

        data = assert_biz_success(AuthApi(mes_client).current_user()).data
        assert_fields(data, ["username", "workshops"])
        assert data["workshops"], "登录用户未加载到任何车间权限"

    @allure.story("能查询今日排产计划")
    def test_query_today_plan(self, mes):
        today = time.strftime("%Y-%m-%d")
        data = assert_biz_success(mes.work_order.list_by_date(today)).data
        assert isinstance(data, list), f"排产计划应返回列表，实际 {type(data)}"

    @allure.story("能新建工单")
    def test_create_work_order(self, work_order):
        assert_fields(work_order, ["order_no", "status"])

    @allure.story("条码枪扫码报工能写库")
    def test_scan_report(self, mes, work_order):
        result = mes.scan_report(work_order["order_no"], quantity=10)
        assert_fields(result, ["report_id"])
        progress = mes.wait_progress(work_order["order_no"], expected_qty=10, timeout=15)
        assert progress["reported_qty"] >= 10

    @allure.story("织机数据采集接口有数据")
    def test_loom_metrics(self, mes):
        data = assert_biz_success(mes.production.loom_metrics("LINE-01")).data
        assert data, "织机采集接口未返回任何数据点，可能采集链路中断"

    @allure.story("库存查询能出数")
    def test_inventory_query(self, mes, work_order):
        material = work_order["material"]["material_code"]
        assert_status(mes.inventory.query(material))

    @allure.story("与 ERP 的同步接口连通")
    def test_erp_reachable(self, erp_order):
        assert_status(erp_order.health())
