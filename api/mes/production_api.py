from api.base_api import BaseApi
from common.http_client import ApiResponse


class ProductionApi(BaseApi):
    def scan_report(self, payload: dict) -> ApiResponse:
        """条码枪扫码报工。"""
        return self.client.post("/production/reports", json=payload)

    def get_progress(self, order_no: str) -> ApiResponse:
        return self.client.get(f"/production/progress/{order_no}")

    def loom_metrics(self, line_code: str) -> ApiResponse:
        """织机数据采集。"""
        return self.client.get("/production/loom-metrics", params={"line_code": line_code})
