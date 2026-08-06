from typing import Optional

from api.base_api import BaseApi
from common.http_client import ApiResponse


class WorkOrderApi(BaseApi):
    def create(self, payload: dict) -> ApiResponse:
        return self.client.post("/work-orders", json=payload)

    def get(self, order_no: str) -> ApiResponse:
        return self.client.get(f"/work-orders/{order_no}")

    def list_by_date(self, planned_date: str, line_code: Optional[str] = None) -> ApiResponse:
        return self.client.get(
            "/work-orders", params={"planned_date": planned_date, "line_code": line_code}
        )

    def release(self, order_no: str) -> ApiResponse:
        return self.client.post(f"/work-orders/{order_no}/release")

    def delete(self, order_no: str) -> ApiResponse:
        return self.client.delete(f"/work-orders/{order_no}")
