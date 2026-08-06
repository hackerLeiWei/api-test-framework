# 接口自动化测试框架骨架

pytest + requests + Allure，分层设计。面向集团制造业场景（MES / ERP / WMS / 外贸），
示例以 MES 工单链路为主，可直接替换为你们真实接口。

## 分层结构

```
用例层  testcases/     只写业务语义，读起来像需求文档
   ↓
业务层  business/      多接口组合成业务动作，如 create_work_order()
   ↓
接口层  api/           单个 API 的封装，接口变更只改这一层
   ↓
基础层  common/        HTTP 客户端、鉴权、日志、断言、数据工厂
```

**核心原则**：接口一变，只改 `api/`，上层用例不动。这决定了框架能不能活过两年。

## 目录

| 路径 | 说明 |
|---|---|
| `config/` | 多环境配置（dev / sit / uat），通过 `--env` 切换 |
| `common/` | HTTP 客户端、配置加载、日志、断言封装、数据工厂 |
| `api/` | 接口层，按系统分包（mes / erp） |
| `business/` | 业务封装层 |
| `testcases/smoke/` | 冒烟用例（P0，每次构建必跑，<5 分钟） |
| `testcases/e2e/` | 端到端业务链路用例 |
| `data/` | 测试数据（yaml，参数化驱动） |
| `mock/` | 外部依赖挡板服务（海关 / 设备采集） |
| `ci/` | GitLab CI 与 Jenkins 配置 |

## 快速开始

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 启动 Mock 服务（示例用例默认打到 Mock，可直接跑通）
python mock/mock_server.py &

# 跑冒烟
pytest -m smoke --env=sit

# 跑端到端链路
pytest -m e2e --env=sit

# 生成 Allure 报告
allure serve reports/allure-results
```

## 用例标记

| 标记 | 含义 | 触发时机 |
|---|---|---|
| `@pytest.mark.smoke` | 冒烟，版本准入门禁 | 每次代码合并 |
| `@pytest.mark.e2e` | 端到端业务链路 | 每晚全量回归 |
| `@pytest.mark.p0` | 故障代价最高 | 发版前必跑 |
| `@pytest.mark.reconcile` | 跨系统数据对账 | 定时跑，含生产只读 |

## 规约（写用例前必读）

1. **用例必须独立**：能单独跑、能乱序跑、能并发跑。禁止用例间依赖执行顺序。
2. **数据自造自清**：用例自己建数据，`yield` 后自己删。禁止依赖"环境里本来就有的那条数据"。
3. **禁止 `time.sleep`**：用 `common.waiter.wait_until` 轮询等待。
4. **外部依赖一律 Mock**：海关、银行、第三方物流、产线设备。
5. **红了当天处理**：容忍长期失败的用例，整套自动化就死了。
6. **脚本按代码管**：进 Git、走 Code Review。

## 落地节奏建议

- 第 1 个月：框架 + 10 条接口冒烟，接进 CI 每日跑
- 第 3 个月：核心业务链路覆盖
- 第 6 个月：接入合并门禁，回归耗时从人天降到分钟

衡量指标看**回归耗时下降**和**自动化拦截缺陷数**，不要看脚本条数。




新增：
windows 当前命令窗口启动： Start-Process python -ArgumentList "mock/mock_server.py" -NoNewWindow
windows 启动新窗口打开：Start-Process python -ArgumentList "mock/mock_server.py"
启动成功展示： Running on http://127.0.0.1:9527

powershell中停止进程：
方式一：
Get-Process python | Where-Object {$_.MainWindowTitle -eq ""} | Stop-Process
方式二 （simply find the process ID and kill it:）：
taskkill /F /IM python.exe


windows 运行 test(增加 python -m ):
Future Usage
For future runs, you'll need to:

Activate the virtual environment first: .venv\Scripts\Activate.ps1
Run tests with: python -m pytest -m smoke --env=sit
