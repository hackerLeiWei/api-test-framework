from api.base_api import BaseApi
from common.http_client import ApiResponse


class ErpOrderApi(BaseApi):
    def sync_status(self, order_no: str) -> ApiResponse:
        """查询 MES 工单同步到 ERP 的结果，用于跨系统对账。"""
        return self.client.get(f"/orders/{order_no}")

    def health(self) -> ApiResponse:
        return self.client.get("/health")
