"""端到端业务链路：工单 → 下达 → 报工 → 入库 → ERP 同步对账。

这类用例数量少但价值最高，制造业的缺陷绝大多数出在系统间。
"""
import allure
import pytest

from common.assertions import assert_biz_success, assert_equal, assert_reconciled
from common.waiter import wait_until

pytestmark = [pytest.mark.e2e, pytest.mark.p0]


@allure.feature("生产主干链路")
@allure.story("工单全流程并与 ERP 对账")
class TestWorkOrderChain:
    def test_full_chain(self, mes, erp_order, work_order):
        order_no = work_order["order_no"]
        quantity = 100

        with allure.step("分批扫码报工至满数"):
            for _ in range(2):
                mes.scan_report(order_no, quantity=50)
            progress = mes.wait_progress(order_no, expected_qty=quantity)
            assert_equal(progress["reported_qty"], quantity, "累计报工数")

        with allure.step("完工入库"):
            stock = mes.stock_in(order_no, quantity)
            assert_equal(stock["quantity"], quantity, "入库数量")

        with allure.step("等待 ERP 异步同步"):
            erp_data = wait_until(
                lambda: erp_order.sync_status(order_no).data or None,
                timeout=30,
                desc=f"ERP 收到工单 {order_no}",
            )

        with allure.step("MES 与 ERP 数据对账"):
            mes_data = assert_biz_success(mes.work_order.get(order_no)).data
            assert_reconciled(
                mes_data, erp_data, keys=["order_no", "quantity"], desc="MES 与 ERP 工单"
            )

    @pytest.mark.reconcile
    def test_defect_quantity_reconciled(self, mes, work_order):
        """次品数应计入报工但不计入合格品，历史上这里出过错账。"""
        order_no = work_order["order_no"]
        mes.scan_report(order_no, quantity=50, defect=5)
        progress = mes.wait_progress(order_no, expected_qty=45)
        assert_equal(progress["qualified_qty"], 45, "合格品数量")
        assert_equal(progress["defect_qty"], 5, "次品数量")
