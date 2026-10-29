---
type: project
recorded: 2026-10-29
source_date: 2026-10-29
status: completed-proof-submission-reported
---
# ComputeRoll / CROLL 计算与提交

来源：聊天01a183ad-0dce-73c2-84cd-34d41a62d15f的用户请求及助手最终答复。本轮记忆维护没有重新查链。
本机：D:\GPT\Binance\research\computeroll-20261029。

## 关键结果

用户使用账号二试验CPU/GPU算题；RTX3060Ti的历史实测约708MH/s，后来约696–855MH/s。
用户规定2026-10-29上午10:00停止，找到证明或异常提前停。80°C保护、RPC短暂失败最多重试3次为当时程序设置；当前进程未核验，不重启或延长运行。
找到1个有效候选后，前期因本机BAW连接缺失未能提交；“仍未提交/余额0”已被同日较新成功记录取代。
原会话10:26答复报告提交mine成功：账号二获得10,000 CROLL，原生币value=0、无代币授权，gas为0.000009714219902478 BNB。
交易：https://bscscan.com/tx/0x9704a420d16c06428f174907fc6669d8f3d36c7d9ba07fe599e644de03ef4675
报告称receipt及Mined/ProofAccepted/Transfer事件匹配。没有已卖出CROLL的证据；余额和市场条件须重新查询。

## 接手入口

- 候选：overnight-20261029/gpu-candidate-verified.json。
- 交易准备：submission-preview.json；提交前用最新globalMines重新核验，不把旧proof当永久有效。
- 算法：Keccak-256的84字节challenge/address/nonce，不能替换为NIST SHA3。
- BAW连接修复入口：D:\GPT\Binance\work\binance-agentic-wallet-cli\baw-with-system-proxy.ps1。原会话报告只在命令期间沿用既有系统代理，没有修改系统代理、Vortex或PATH。
- 本机面板历史入口http://127.0.0.1:8876；当前监听状态未核验。

计算候选、链上mint到账、卖出代币是三个独立结果。一次提交授权不扩展为以后自动计算、交易或卖出许可；不上传钱包凭据。
