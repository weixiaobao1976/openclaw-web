# 🌐 OpenClaw Web 管理界面

> FastAPI + Web 仪表盘 / 配置管理 / 监控面板

## 📋 分支规划

| 分支 | 内容 |
|------|------|
| `main` | 总览 + 架构说明 |
| `backend` | FastAPI 后端（API + 认证 + 数据服务）|
| `frontend` | 前端面板（仪表盘 / 配置管理 / 日志查看）|
| `dashboard` | 实时监控面板（Gateway状态/系统指标/模型状态）|
| `config-manager` | 配置编辑器（openclaw.json 可视化编辑）|
| `log-viewer` | 日志查看器（gateway日志/维护日志）|

## 🏗️ 架构

```
┌─────────────────────────────────────────┐
│            Web Browser                  │
├─────────────────────────────────────────┤
│         FastAPI (uvicorn)              │
│  ┌──────────┐  ┌──────────────────┐   │
│  │ REST API │  │ WebSocket (实时)  │   │
│  └────┬─────┘  └────────┬─────────┘   │
├───────┴──────────────────┴─────────────┤
│          Gateway API (127.0.0.1:18789) │
├─────────────────────────────────────────┤
│   openclaw CLI / gh CLI / systemctl    │
└─────────────────────────────────────────┘
```

## 🚀 开发计划

### Phase 1 — 基础框架
- FastAPI 应用 + CORS
- Gateway 连通性检测
- 基础仪表盘

### Phase 2 — 监控面板
- 实时 Gateway 状态
- 系统资源（CPU/内存/磁盘）
- 日志查看

### Phase 3 — 配置管理
- JSON 配置可视化编辑
- 配置差异对比
- 备份/恢复

### Phase 4 — 技能管理
- 技能列表/启用/禁用
- 模型管理界面

## 🛠 技术栈

| 组件 | 技术 |
|------|------|
| 后端 | FastAPI + uvicorn |
| 前端 | HTML/CSS/JS (htmx + alpine.js) |
| 实时 | WebSocket |
| 认证 | session-based |
| 部署 | systemd user service |

## 🔗 相关项目

- [openclaw-tools](https://github.com/weixiaobao1976/openclaw-tools) — 运维工具集
- [openclaw-agentics](https://github.com/weixiaobao1976/openclaw-agentics) — 技能/自动化
- [openclaw-techniques](https://github.com/weixiaobao1976/openclaw-techniques) — 技术实战文档库

---

**建设中...** 🐺
