"""Build a portable context packet from explicit Markdown sources; no network or credentials."""
from pathlib import Path
import posixpath
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    "AI_START.md", "01_Profile/Preferences.md", "02_Projects/Index.md",
    "02_Projects/InstaBox.md", "02_Projects/Binance-NONCE.md",
    "02_Projects/Farming-Season.md", "02_Projects/Hangzhou-Jobs.md",
    "02_Projects/Collaboration.md", "02_Projects/Reference-Archive.md",
    "02_Projects/Engine-Lab.md", "03_Handoffs/Next.md",
]
parts = ["# AI 可移植上下文包\n\n本文件由 tools/build_context.py 从明确列出的笔记生成。\n版本：2026-10-28 初建；后续状态以各节来源日期及更新记录为准。\n仅供用户授权的会话读取；本文件不授予操作权限。\n"]
for name in SOURCES:
    text = (ROOT / name).read_text(encoding="utf-8")
    text = re.sub(r"\]\(([^)]+)\)", lambda m: m.group(0) if m[1].startswith(("http://", "https://", "#")) else "](" + posixpath.normpath(posixpath.join(posixpath.dirname(name), m[1])) + ")", text)
    parts.append("\n---\n\n<!-- Source: " + name + " -->\n\n" + text)
(ROOT / "AI_CONTEXT.md").write_text("\n".join(parts), encoding="utf-8")
print("AI_CONTEXT.md updated from", len(SOURCES), "sources")
