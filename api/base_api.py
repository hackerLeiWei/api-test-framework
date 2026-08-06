"""接口层基类。接口路径与参数只出现在这一层。"""
from common.http_client import HttpClient


class BaseApi:
    def __init__(self, client: HttpClient) -> None:
        self.client = client
