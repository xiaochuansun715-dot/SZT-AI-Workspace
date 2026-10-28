---
type: project
recorded: 2026-10-28
source_date: 2026-10-27
status: historical-needs-recheck
---
# Binance / NONCE

来源：历史摘要，关联聊天 01a17e0f-37f3-7910-b5f0-156502dc2f6a、01a17da3-8daa-72c2-9647-5b98897418ee。
本机项目：D:\GPT\Binance。

## 接手要点

账号二由 Codex 负责；资金相关动作需逐次明确确认。不得把一次签名或登录复用于后续操作授权。
历史 NONCE #6104 已有成交与转出记录，不能沿用更早“仍挂单未售”的描述；当前持仓需重新查链。
2026-10-27 的最新实时尝试停在 MCP 初始化 429，未取得新题或提交答案，没有新的成功 mint 证据。
历史 moat.fun claim 曾在明确确认 EIP-712 签名后完成；不授权以后签名。

## 代码路线

- research/nonce-live-20261028/solve_current.py：本地求解与 MCP 客户端入口。
- research/nonce-offline-20261028/BEST-OFFLINE.json 与 benchmark-report.json：过期 balanced-1536 实验记录；没有满足赋值或提交成功。
- 历史经验：先分类；balanced-1536 可优先 CScoreSAT/DCCASat 多种子 CPU 冷启动；旧实验的停止条件仅作参考，每次任务以当前预算为准。
- watch_nonce.py 为只读通知程序，历史 PID 和运行状态不可信，需核验。

## 下一步

先检查当前服务、额度与题目；离线解题结果必须完整验证。
纯解题协作不等于允许开启钱包操作或反复自动申请新挑战。
