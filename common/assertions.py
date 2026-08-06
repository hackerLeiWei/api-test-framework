"""断言封装：失败信息要能直接定位问题，不要只有 assert False。"""
from typing import Any, Iterable

import allure

from common.http_client import ApiResponse


def assert_status(resp: ApiResponse, expected: int = 200) -> ApiResponse:
    with allure.step(f"断言 HTTP 状态码 == {expected}"):
        assert resp.status_code == expected, (
            f"期望 HTTP {expected}，实际 {resp.status_code}，响应体: {resp.raw.text[:500]}"
        )
    return resp


def assert_biz_success(resp: ApiResponse, success_code: Any = 0) -> ApiResponse:
    assert_status(resp, 200)
    with allure.step(f"断言业务码 == {success_code}"):
        actual = resp.biz_code
        assert actual == success_code, (
            f"期望业务码 {success_code}，实际 {actual}，响应体: {resp.raw.text[:500]}"
        )
    return resp


def assert_fields(payload: dict, required: Iterable[str]) -> dict:
    missing = [f for f in required if f not in payload]
    with allure.step(f"断言响应包含字段 {list(required)}"):
        assert not missing, f"响应缺少字段 {missing}，实际字段 {sorted(payload)}"
    return payload


def assert_equal(actual: Any, expected: Any, desc: str) -> None:
    with allure.step(f"断言 {desc}"):
        assert actual == expected, f"{desc} 不符：期望 {expected!r}，实际 {actual!r}"


def assert_reconciled(left: dict, right: dict, keys: Iterable[str], desc: str) -> None:
    """跨系统对账断言：逐字段比对两个系统的同一业务对象。"""
    diffs = {k: (left.get(k), right.get(k)) for k in keys if left.get(k) != right.get(k)}
    with allure.step(f"对账断言 {desc}"):
        assert not diffs, f"{desc} 存在不一致（字段: (左, 右)）: {diffs}"
