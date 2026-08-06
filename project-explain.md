# 项目讲解

我来详细讲解这个API测试框架项目。首先让我探索一下项目的整体结构：

# API测试框架项目详解

这是一个面向制造业场景的企业级API自动化测试框架，采用分层设计，主要用于测试MES（制造执行系统）、ERP（企业资源计划）、WMS（仓储管理系统）等系统。

## 🏗️ 架构设计

### 分层结构（核心设计理念）
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

## 📁 目录结构详解

### 1. 基础层
- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\common\http_client.py" />** - HTTP客户端封装
  - 统一鉴权、超时、重试机制
  - 自动日志记录和Allure报告附件
  - 提供ApiResponse薄封装，避免直接依赖requests

- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\common\config.py" />** - 多环境配置加载
  - 支持环境变量占位符：`${VAR}` 和 `${VAR:-default}`
  - 支持dev/sit/uat多环境切换

- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\common\assertions.py" />** - 断言封装
  - 业务级断言：`assert_biz_success()` - 检查业务码
  - 跨系统对账：`assert_reconciled()` - MES与ERP数据对账

- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\common\data_factory.py" />** - 测试数据工厂
  - 生成唯一工单号：时间戳+随机串，保证并发不冲突
  - 提供标准测试数据模板

- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\common\waiter.py" />** - 轮询等待
  - 替代`time.sleep()`，用轮询等待异步操作完成
  - 支持超时控制和错误处理

### 2. 接口层
- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\api\base_api.py" />** - 接口基类
- **api/mes/** - MES系统接口封装（auth_api, work_order_api, production_api, inventory_api）
- **api/erp/** - ERP系统接口封装

### 3. 业务层
- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\business\mes_flow.py" />** - MES业务流程封装
  - `create_released_work_order()` - 创建并下达工单
  - `scan_report()` - 扫码报工
  - `wait_progress()` - 等待工单进度
  - `stock_in()` - 完工入库
  - `cleanup()` - 清理测试数据

### 4. 用例层
- **testcases/smoke/** - 冒烟用例（P0，每次构建必跑，<5分钟）
  - <ref_file file="D:\Code\Test\api-test-framework\api-test-framework\testcases\smoke\test_mes_smoke.py" /> - 7条MES冒烟用例

- **testcases/e2e/** - 端到端业务链路用例
  - <ref_file file="D:\Code\Test\api-test-framework\api-test-framework\testcases\e2e\test_work_order_chain.py" /> - 工单全流程测试

### 5. 配置与数据
- **config/** - 多环境配置文件（dev.yaml, sit.yaml, uat.yaml）
- **data/** - 测试数据（YAML格式，参数化驱动）

### 6. Mock服务
- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\mock\mock_server.py" />** - 外部依赖挡板服务
  - 让框架开箱即跑通，不依赖真实MES/ERP
  - 提供MES和ERP的模拟接口

### 7. CI/CD集成
- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\ci\Jenkinsfile" />** - Jenkins流水线配置
- **<ref_file file="D:\Code\Test\api-test-framework\api-test-framework\ci\.gitlab-ci.yml" />** - GitLab CI配置

## 🎯 核心特性

### 1. 用例标记体系
| 标记 | 含义 | 触发时机 |
|---|---|---|
| `@pytest.mark.smoke` | 冒烟，版本准入门禁 | 每次代码合并 |
| `@pytest.mark.e2e` | 端到端业务链路 | 每晚全量回归 |
| `@pytest.mark.p0` | 故障代价最高 | 发版前必跑 |
| `@pytest.mark.reconcile` | 跨系统数据对账 | 定时跑，含生产只读 |

### 2. 测试规约
1. **用例必须独立**：能单独跑、能乱序跑、能并发跑
2. **数据自造自清**：用例自己建数据，自己删
3. **禁止 `time.sleep`**：用 `common.waiter.wait_until` 轮询等待
4. **外部依赖一律 Mock**：海关、银行、第三方物流、产线设备
5. **红了当天处理**：容忍长期失败的用例，整套自动化就死了
6. **脚本按代码管**：进Git、走Code Review

### 3. 运行方式
```bash
# 激活虚拟环境
.venv\Scripts\Activate.ps1

# 启动Mock服务
Start-Process python -ArgumentList "mock/mock_server.py" -NoNewWindow

# 跑冒烟
python -m pytest -m smoke --env=sit

# 跑端到端链路
python -m pytest -m e2e --env=sit

# 生成Allure报告
python -m allure serve reports/allure-results
```

## 🚀 CI/CD集成

### GitLab CI（合并门禁）
- **冒烟测试**：合并请求时触发，冒烟不过不许合
- **每晚回归**：定时任务，全量回归测试
- **失败重跑**：区分真失败与环境抖动

### Jenkins
- **参数化构建**：选择环境（sit/uat/dev）和范围（smoke/e2e/all）
- **定时触发**：每晚2点全量回归
- **Allure报告**：自动生成测试报告

## 💡 项目优势

1. **分层清晰**：接口变更只改api层，影响范围可控
2. **数据隔离**：用例独立，支持并发执行
3. **生产导向**：面向制造业实际场景（MES/ERP/WMS）
4. **工程化**：完整的CI/CD集成，代码质量管理
5. **可维护性**：规约明确，易于团队协作

## 📊 落地节奏建议

- **第1个月**：框架 + 10条接口冒烟，接进CI每日跑
- **第3个月**：核心业务链路覆盖
- **第6个月**：接入合并门禁，回归耗时从人天降到分钟

**衡量指标**：看回归耗时下降和自动化拦截缺陷数，不要看脚本条数。

这个框架的设计非常成熟，特别适合制造业的复杂系统测试场景，通过分层架构和工程化实践，解决了传统测试脚本维护困难的痛点。