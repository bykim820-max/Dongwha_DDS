#!/usr/bin/env python3
"""DDS 하드코딩 검사기 — hex 색상 · spacing px · 이모지 차단.

design.md § 코드 매핑 핵심 규칙 / § 디자인 금지 규칙의 자동 검증.
CI와 로컬에서 동일하게 실행한다:

    python3 scripts/check_hardcoding.py

검사 대상
  - 저장소 루트와 examples/ 의 *.html — UI로 렌더되는 파일
  - hex·px는 CSS 문맥(<style> 블록, style= 속성)만 검사한다.
    본문 텍스트의 주문번호(#10293)나 앵커(#feedback)는 색상이 아니다.
  - 이모지는 파일 전체를 검사한다 (UI 노출 금지 — icons.md §0)

검사하지 않는 것
  - dist/            : 빌드 산출물. 값이 해석된 hex/px가 있는 것이 정상
  - foundations/*.json: 토큰 SSOT. 원시 값의 원본
  - *.md             : 문서. hex 값 설명·이모지 헤딩은 UI가 아니다

예외 처리
  - #fff / #ffffff 허용 — 브랜드 배경 위 흰색은 문서화된 예외 (icons.md §3)
  - 정당한 예외는 해당 줄에 `dds-allow: <이유>` 주석을 남기면 건너뛴다.
    이유 없는 dds-allow는 리뷰에서 반려한다.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ── 검사 대상 ────────────────────────────────────────────────
def target_files() -> list[Path]:
    files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "examples").glob("*.html"))
    return [f for f in files if "dist" not in f.parts]

# ── 패턴 ────────────────────────────────────────────────────
# 3·4·6·8자리만 hex 색상. 5자리(주문번호 #10293 등)는 색상이 아니다.
HEX = re.compile(r"#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})(?![0-9a-fA-F])")
HEX_ALLOWED = {"#fff", "#ffff", "#ffffff", "#ffffffff"}  # icons.md §3

# rgb()/rgba()/hsl()/hsla() 리터럴도 색상 하드코딩이다
RGB = re.compile(r"\b(?:rgba?|hsla?)\(")

# 간격 속성에 px 리터럴 — spacing/* 토큰(var(--space-*))만 허용 (design.md 규칙 2)
SPACING_PX = re.compile(
    r"(?:^|[;{\s])"
    r"(margin(?:-[a-z]+)*|padding(?:-[a-z]+)*|gap|row-gap|column-gap|inset(?:-[a-z]+)*)"
    r"\s*:[^;}]*?\b[1-9][0-9]*px",
)

# 이모지·기호문자 (icons.md §0 금지 목록 범위)
EMOJI = re.compile(
    "["
    "\U0001F000-\U0001FAFF"  # 이모지 본 영역 (얼굴·사물·국기 등)
    "☀-➿"          # 잡기호·딩뱃 (⚠ ✅ ✨ ❌ …)
    "⬀-⯿"          # 화살표·별 (⭐ ⬅ …)
    "️"                 # 이모지 표현 선택자
    "]"
)

ALLOW = re.compile(r"dds-allow:\s*\S")

STYLE_OPEN = re.compile(r"<style[^>]*>", re.I)
STYLE_CLOSE = re.compile(r"</style>", re.I)
INLINE_STYLE = re.compile(r'style\s*=\s*"([^"]*)"|style\s*=\s*\'([^\']*)\'', re.I)


def css_contexts(line: str, in_style: bool) -> list[str]:
    """이 줄에서 CSS로 취급할 조각들을 돌려준다."""
    if in_style:
        return [line]
    return ["".join(m.groups("")) for m in INLINE_STYLE.finditer(line)]


def check_file(path: Path) -> list[str]:
    problems: list[str] = []
    in_style = False
    rel = path.relative_to(ROOT)

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        opened = bool(STYLE_OPEN.search(line))
        closed = bool(STYLE_CLOSE.search(line))
        line_is_css = in_style or opened
        if opened and not closed:
            in_style = True
        if closed:
            in_style = False

        if ALLOW.search(line):
            continue

        # hex · spacing px — CSS 문맥만
        chunks = [line] if line_is_css else css_contexts(line, False)
        for chunk in chunks:
            for m in HEX.finditer(chunk):
                if m.group(0).lower() not in HEX_ALLOWED:
                    problems.append(
                        f"{rel}:{lineno}: hex 색상 하드코딩 {m.group(0)} — "
                        f"Semantic 토큰(var(--color-*))으로 교체 (design.md 규칙 1)"
                    )
            for m in RGB.finditer(chunk):
                problems.append(
                    f"{rel}:{lineno}: {m.group(0)}…) 색상 하드코딩 — "
                    f"Semantic 토큰(var(--color-*))으로 교체 (design.md 규칙 1)"
                )
            m = SPACING_PX.search(chunk)
            if m:
                problems.append(
                    f"{rel}:{lineno}: 간격 px 하드코딩 ({m.group(1)}) — "
                    f"var(--space-*) 토큰으로 교체 (design.md 규칙 2)"
                )

        # 이모지 — 파일 전체
        m = EMOJI.search(line)
        if m:
            problems.append(
                f"{rel}:{lineno}: 이모지 {m.group(0)!r} — UI 노출 금지, "
                f"라인 SVG 아이콘으로 교체 (icons.md §0)"
            )

    return problems


def main() -> int:
    files = target_files()
    all_problems: list[str] = []
    for f in files:
        all_problems.extend(check_file(f))

    if all_problems:
        print(f"✗ 하드코딩 {len(all_problems)}건 발견\n")
        for p in all_problems:
            print("  " + p)
        print(
            "\n예외가 정당하다면 해당 줄에 `dds-allow: <이유>` 주석을 남기세요."
            "\n규칙 근거: design.md § 코드 매핑 핵심 규칙 · § 디자인 금지 규칙"
        )
        return 1

    print(f"✓ 하드코딩 없음 — {len(files)}개 파일 통과")
    return 0


if __name__ == "__main__":
    sys.exit(main())
