from api.base_api import BaseApi
from common.http_client import ApiResponse


class AuthApi(BaseApi):
    def login(self, username: str, password: str) -> ApiResponse:
        return self.client.post("/auth/login", json={"username": username, "password": password})

    def current_user(self) -> ApiResponse:
        return self.client.get("/auth/me")
