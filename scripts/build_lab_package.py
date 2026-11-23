#!/usr/bin/env python3
"""동화Lab 업로드 묶음 만들기 — 정본을 동화Lab으로 옮길 때 올릴 최종 파일만 모은다.

    python3 scripts/build_lab_package.py

결과: dongwhalab/ 폴더 (매번 지우고 새로 만든다). 구성은 START.md 참조.

  - 문서(md) · 토큰(dist/) · 토큰 원본 JSON · 재개용 스크립트를 폴더 구조 그대로 복사한다
  - HTML은 <link href=".../dist/tokens.css">를 파일 안의 <style>로 바꿔 넣는다.
    동화Lab에서 HTML 하나만 열어도 토큰이 적용되게 하기 위해서다
  - 올리지 않는 것: plugins/ · mcp/ · .github/ · metrics/ · 커밋되지 않은 예시 HTML
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dongwhalab"

DOCS = [
    "START.md", "README.md", "HANDOVER.md", "design.md", "AGENTS.md",
    "CHANGELOG.md", "MIGRATION.md", "VERSION",
]
GLOBS = [
    "foundations/*.md", "foundations/*.json",
    "components/*.md",
    "guides/*.md",
    "dist/*",
    "scripts/build_tokens.py", "scripts/check_hardcoding.py",
]
HTML = ["index.html", "guides/index.html"]

TOKENS_LINK = re.compile(r'<link rel="stylesheet" href="(?:\./|\.\./)dist/tokens\.css"\s*/>')


def tracked(path: str) -> bool:
    """git이 추적하는 파일만 올린다 — 작업 중인 예시가 섞이지 않게."""
    r = subprocess.run(["git", "ls-files", "--error-unmatch", path], cwd=ROOT,
                       capture_output=True)
    return r.returncode == 0


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)

    files = [ROOT / p for p in DOCS]
    for g in GLOBS:
        files += sorted(ROOT.glob(g))
    for f in files:
        dest = OUT / f.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)

    tokens = (ROOT / "dist" / "tokens.css").read_text(encoding="utf-8")
    inline = "<style>/* DDS 토큰 — dist/tokens.css 를 그대로 넣음 (동화Lab 단독 열기용) */\n" + tokens + "\n</style>"
    pages = HTML + [str(p.relative_to(ROOT)) for p in sorted((ROOT / "examples").glob("*.html"))
                    if tracked(str(p.relative_to(ROOT)))]
    for rel in pages:
        src = (ROOT / rel).read_text(encoding="utf-8")
        html, n = TOKENS_LINK.subn(lambda _: inline, src, count=1)
        if n != 1:
            print(f"✗ {rel}: tokens.css 링크를 찾지 못함")
            return 1
        dest = OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")

    count = sum(1 for p in OUT.rglob("*") if p.is_file())
    print(f"✓ dongwhalab/ — 파일 {count}개 (HTML {len(pages)}개는 토큰 내장)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
