"""Build a concise, agent-neutral packet; history and full projects stay on demand."""
from pathlib import Path
import posixpath
import re
ROOT=Path(__file__).resolve().parents[1]
SOURCES=["START_HERE.md","01_Profile/Preferences.md","02_Projects/Index.md","03_Handoffs/Next.md"]
parts=["# 多 Agent 精简上下文包\n\n生成自知识库常读层；项目细节与历史按需另取。\n"]
for name in SOURCES:
    text=(ROOT/name).read_text(encoding="utf-8")
    text=re.sub(r"\]\(([^)]+)\)",lambda m:m.group(0) if m[1].startswith(("http://","https://","#")) else "]("+posixpath.normpath(posixpath.join(posixpath.dirname(name),m[1]))+")",text)
    parts.append("\n---\n\n<!-- Source: "+name+" -->\n\n"+text)
packet="\n".join(parts)
if len(packet)>14000:
    raise SystemExit("Context exceeds 14000-character budget; condense source notes first")
(ROOT/"AI_CONTEXT.md").write_text(packet,encoding="utf-8")
print("AI_CONTEXT.md:",len(packet),"characters;",len(SOURCES),"sources; no history loaded")
