"""全局 fixture：环境切换、客户端、登录态、测试数据自造自清。"""
import allure
import pytest

from business.mes_flow import MesFlow
from common.assertions import assert_biz_success
from common.config import load_config
from common.http_client import HttpClient
from api.erp.order_api import ErpOrderApi
from api.mes.auth_api import AuthApi


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--env", action="store", default="sit", help="测试环境: dev / sit / uat"
    )


@pytest.fixture(scope="session")
def config(request: pytest.FixtureRequest):
    cfg = load_config(request.config.getoption("--env"))
    allure.dynamic.parameter("env", cfg.env_name)
    return cfg


@pytest.fixture(scope="session")
def mes_client(config):
    """带登录态的 MES 客户端。登录失败直接让整个会话失败，避免几百条用例报同一个错。"""
    client = HttpClient(config, "mes")
    auth = config.auth()
    resp = AuthApi(client).login(auth["username"], auth["password"])
    assert resp.status_code == 200, f"MES 登录失败，环境不可用: {resp.raw.text[:300]}"
    client.set_token(assert_biz_success(resp).data["token"])
    yield client
    client.close()


@pytest.fixture(scope="session")
def erp_client(config):
    client = HttpClient(config, "erp")
    yield client
    client.close()


@pytest.fixture
def mes(mes_client) -> MesFlow:
    return MesFlow(mes_client)


@pytest.fixture
def erp_order(erp_client) -> ErpOrderApi:
    return ErpOrderApi(erp_client)


@pytest.fixture
def work_order(mes: MesFlow):
    """自造自清的工单数据。用例结束后一定回收，保证可重复执行。"""
    created = mes.create_released_work_order(quantity=100)
    yield created
    mes.cleanup(created["order_no"])


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """失败时把用例标记与环境写进报告，方便排查。"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        allure.attach(
            f"markers: {[m.name for m in item.iter_markers()]}",
            name="用例上下文",
            attachment_type=allure.attachment_type.TEXT,
        )
