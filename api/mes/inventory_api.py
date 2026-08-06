from api.base_api import BaseApi
from common.http_client import ApiResponse


class InventoryApi(BaseApi):
    def stock_in(self, order_no: str, quantity: int) -> ApiResponse:
        return self.client.post("/inventory/stock-in", json={"order_no": order_no, "quantity": quantity})

    def query(self, material_code: str) -> ApiResponse:
        return self.client.get("/inventory", params={"material_code": material_code})
