"""HTTP 基础客户端：统一鉴权、超时、重试、日志、Allure 附件。

所有接口层都通过它发请求，不要在用例里直接 import requests。
"""
from typing import Any, Optional

import allure
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from common.config import Config
from common.logger import get_logger

logger = get_logger(__name__)

_RETRY_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})


class ApiResponse:
    """薄封装，避免用例层直接依赖 requests。"""

    def __init__(self, raw: requests.Response) -> None:
        self.raw = raw

    @property
    def status_code(self) -> int:
        return self.raw.status_code

    @property
    def ok(self) -> bool:
        return self.raw.ok

    def json(self) -> Any:
        try:
            return self.raw.json()
        except ValueError as exc:
            raise AssertionError(
                f"响应不是合法 JSON: {self.raw.status_code} {self.raw.text[:500]}"
            ) from exc

    @property
    def data(self) -> Any:
        """约定业务响应体为 {code, message, data}。"""
        body = self.json()
        if isinstance(body, dict) and "data" in body:
            return body["data"]
        return body

    @property
    def biz_code(self) -> Any:
        body = self.json()
        return body.get("code") if isinstance(body, dict) else None


class HttpClient:
    def __init__(self, config: Config, service: str) -> None:
        self._config = config
        self._service = service
        self._base_url = config.base_url(service)
        self._session = requests.Session()
        retry = Retry(
            total=config.retry,
            backoff_factor=0.5,
            status_forcelist=(502, 503, 504),
            allowed_methods=_RETRY_METHODS,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)

    def set_token(self, token: str) -> None:
        self._session.headers["Authorization"] = f"Bearer {token}"

    def request(self, method: str, path: str, **kwargs: Any) -> ApiResponse:
        url = f"{self._base_url}/{path.lstrip('/')}"
        kwargs.setdefault("timeout", self._config.timeout)
        logger.info("%s %s payload=%s", method, url, kwargs.get("json") or kwargs.get("params"))
        raw = self._session.request(method, url, **kwargs)
        self._attach(method, url, kwargs, raw)
        return ApiResponse(raw)

    def get(self, path: str, params: Optional[dict] = None, **kw: Any) -> ApiResponse:
        return self.request("GET", path, params=params, **kw)

    def post(self, path: str, json: Optional[dict] = None, **kw: Any) -> ApiResponse:
        return self.request("POST", path, json=json, **kw)

    def put(self, path: str, json: Optional[dict] = None, **kw: Any) -> ApiResponse:
        return self.request("PUT", path, json=json, **kw)

    def delete(self, path: str, **kw: Any) -> ApiResponse:
        return self.request("DELETE", path, **kw)

    def close(self) -> None:
        self._session.close()

    def _attach(self, method: str, url: str, kwargs: dict, raw: requests.Response) -> None:
        body = kwargs.get("json") or kwargs.get("params") or {}
        allure.attach(
            f"{method} {url}\n\nrequest:\n{body}\n\n"
            f"status: {raw.status_code}\nresponse:\n{raw.text[:4000]}",
            name=f"{self._service} {method} {url}",
            attachment_type=allure.attachment_type.TEXT,
        )
