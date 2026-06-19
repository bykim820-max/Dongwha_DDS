#!/usr/bin/env python3
"""
DDS 토큰 빌드 스크립트 (경량 Style Dictionary)
================================================
입력: foundations/DDS_tokens_w3c.json  (W3C Design Tokens, primitive→semantic 참조)
      foundations/motion.md           (모션/섀도 값은 JSON에 없어 문서 기준 상수로 보유)

출력: dist/tokens.css            — :root CSS 변수 (semantic 값이 hex/px로 해석됨, 드롭인)
      dist/tokens.resolved.json  — 평탄화된 토큰 → 최종값 맵 (기계 판독)
      dist/tokens.tailwind.js    — Tailwind preset (CSS 변수 참조)

사용: python3 scripts/build_tokens.py
JSON만 갱신하면 이 스크립트로 산출물을 재생성한다. dist/* 는 직접 수정 금지.
"""
import json, re, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "foundations" / "DDS_tokens_w3c.json"
EXT = ROOT / "foundations" / "DDS_tokens_extended.json"
DARK = ROOT / "foundations" / "DDS_tokens_dark.json"
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

data = json.load(open(SRC, encoding="utf-8"))

# 확장 토큰(accent·subtle·chart) 병합 — 원본 primitive를 참조만 함
def deep_merge(base, extra):
    for k, v in extra.items():
        if k.startswith("_"):
            continue
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            deep_merge(base[k], v)
        else:
            base[k] = v
if EXT.exists():
    deep_merge(data, json.load(open(EXT, encoding="utf-8")))

# ── 1. 평탄화 + 참조 해석 ────────────────────────────────────────────────
flat = {}          # "a.b.c" -> raw $value
types = {}         # "a.b.c" -> $type
def walk(node, path):
    if isinstance(node, dict):
        if "$value" in node:
            flat[".".join(path)] = node["$value"]
            types[".".join(path)] = node.get("$type")
        else:
            for k, v in node.items():
                walk(v, path + [k])
walk(data, [])

REF = re.compile(r"^\{(.+)\}$")
def resolve(val, depth=0):
    if depth > 20:
        raise RuntimeError("순환 참조: " + str(val))
    m = REF.match(str(val).strip())
    if not m:
        return val
    target = m.group(1)
    if target not in flat:
        raise KeyError(f"끊긴 참조: {{{target}}}")
    return resolve(flat[target], depth + 1)

def num(v):
    """소수 부동소수점 정리 (-0.4000000059 -> -0.4)"""
    try:
        f = float(v)
        return str(int(f)) if f == int(f) else str(round(f, 4))
    except (TypeError, ValueError):
        return v

# semantic 토큰만 (path 가 'color.semantic.*', 'dimension.semantic.*', 'typography.semantic.*')
def semantic(prefix):
    out = {}
    for k, v in flat.items():
        if k.startswith(prefix):
            leaf = k.split(".")[-1]
            out[leaf] = resolve(v)
    return out

colors = semantic("color.semantic.")
dims = semantic("dimension.semantic.")
typo = semantic("typography.semantic.")
primitives = {k.split(".")[-1]: v for k, v in flat.items() if k.startswith("color.primitive.")}

# 다크 테마: light(colors) 위에 dark 오버라이드만 덮어 해석 (primitive 공유)
dark_colors = dict(colors)
if DARK.exists():
    dark_sem = json.load(open(DARK, encoding="utf-8")).get("color", {}).get("semantic", {})
    for leaf, node in dark_sem.items():
        dark_colors[leaf] = resolve(node["$value"])

# ── 2. 토큰명 → CSS 변수명 매핑 (문서 컨벤션과 1:1) ───────────────────────
def color_var(leaf):                       # color_bg_interactive_primary-hover -> --color-bg-interactive-primary-hover
    return "--" + leaf.replace("_", "-")

def dim_var(leaf):
    if leaf.startswith("spacing_"):        # spacing_16 -> --space-16
        return "--space-" + leaf.split("_", 1)[1]
    if leaf.startswith("border_radius_"):  # border_radius_md -> --radius-md
        return "--radius-" + leaf.split("border_radius_", 1)[1]
    if leaf.startswith("border_width_"):   # border_width_md -> --border-width-md
        return "--" + leaf.replace("_", "-")
    return None                            # effect_shadow_* 는 별도 합성

def typo_var(leaf):
    if leaf == "heading_font_family":  return "--font-heading"
    if leaf == "body_font_family":     return "--font-body"
    return "--" + leaf.replace("_", "-")   # heading_md_font_size -> --heading-md-font-size

# ── 3. 모션 / 섀도 (JSON 미수록 → motion.md 기준 상수) ────────────────────
MOTION = {
    "--motion-duration-instant": "80ms",
    "--motion-duration-quick": "160ms",
    "--motion-duration-base": "240ms",
    "--motion-duration-moderate": "320ms",
    "--motion-duration-slow": "480ms",
    "--motion-duration-deliberate": "640ms",
    "--motion-easing-standard": "cubic-bezier(0.4, 0, 0.2, 1)",
    "--motion-easing-decelerate": "cubic-bezier(0, 0, 0.2, 1)",
    "--motion-easing-accelerate": "cubic-bezier(0.4, 0, 1, 1)",
    "--motion-easing-emphasized": "cubic-bezier(0.2, 0, 0, 1)",
    "--motion-easing-spring-soft": "cubic-bezier(0.32, 0.72, 0, 1)",
    "--motion-easing-spring-snappy": "cubic-bezier(0.5, 1.25, 0.5, 1)",
}
# 섀도: JSON effect_shadow_<n> (cast/core y·blur) + 그림자 색(transparent) 합성
_cast = resolve(flat["color.semantic.color_effect_shadow_cast"])   # #00000029
_core = resolve(flat["color.semantic.color_effect_shadow_core"])   # #0000001f
def shadow(n):
    g = lambda part: resolve(flat[f"dimension.semantic.effect_shadow_{n}_{part}"])
    return f"0 {g('cast-y')} {g('cast-blur')} {_cast}, 0 {g('core-y')} {g('core-blur')} {_core}"
SHADOW = {
    "--shadow-sm": shadow("2"),
    "--shadow-md": shadow("4"),
    "--shadow-lg": shadow("8"),
    "--shadow-xl": shadow("16"),
}

# 미세 간격 보강 (JSON 8pt 그리드 사이 스텝) + 섹션 리듬용 대형 스텝
EXTRA_SPACE = {"--space-6": "6px", "--space-10": "10px", "--space-20": "20px", "--space-80": "80px"}

# 레이아웃 (container 최대폭·grid·섹션 리듬) — source: foundations/layout.md
LAYOUT = {
    "--container-sm": "640px", "--container-md": "768px", "--container-lg": "1024px",
    "--container-xl": "1200px", "--container-2xl": "1680px", "--container-prose": "680px",
    "--container-dashboard": "1680px",   # 대시보드 기본 — 이 폭까지 가득 채우고 가운데 고정
    "--grid-columns": "12", "--grid-gutter": "var(--space-24)", "--grid-margin": "var(--space-24)",
    "--snb-width": "270px",   # SNB(사이드 내비) — 좌측 배치, 권장 폭
    "--snb-width-collapsed": "72px",
    "--layout-section-gap": "var(--space-64)",   # 섹션 사이
    "--layout-block-gap": "var(--space-24)",      # 블록(카드) 사이
    "--layout-stack-gap": "var(--space-12)",      # 한 덩어리 내부
}
# 반응형 분기 (CSS @media는 var 미지원 → JS·문서 참조용)
BREAKPOINT = {"--breakpoint-sm": "640px", "--breakpoint-md": "768px",
              "--breakpoint-lg": "1024px", "--breakpoint-xl": "1280px"}

# Elevation: 의미 레벨 ↔ shadow 매핑 ("선 대신 깊이") — source: foundations/elevation.md
ELEVATION = {
    "--elevation-flat": "none",                 # 평면 (배경 분리만)
    "--elevation-raised": "var(--shadow-sm)",   # 카드 기본
    "--elevation-overlay": "var(--shadow-md)",  # 팝오버·드롭다운·hover lift
    "--elevation-sticky": "var(--shadow-md)",   # sticky 헤더/바
    "--elevation-modal": "var(--shadow-lg)",    # 모달·바텀시트
    "--elevation-top": "var(--shadow-xl)",      # 풀스크린 오버레이
}

# 주: 그라데이션 띠/배너·고밀도(density) 모드 토큰은 디자인 금지 규칙(design.md §Anti-patterns)에 따라 제공하지 않음.

# ── 4. tokens.css ────────────────────────────────────────────────────────
def css_value(leaf, val, kind):
    """타이포 number 류는 단위 보정"""
    if kind == "typo":
        if leaf.endswith("_font_size") or leaf.endswith("_line_height"):
            return num(val) + "px"
        if leaf.endswith("_letter_spacing"):
            return num(val) + "px"
        if leaf.endswith("_font_weight"):
            return num(val)
    return val

lines = []
lines.append("/* ============================================================")
lines.append("   DDS v2.0 · Design Tokens (생성 파일 — 직접 수정 금지)")
lines.append("   source: foundations/DDS_tokens_w3c.json + foundations/motion.md")
lines.append("   regenerate: python3 scripts/build_tokens.py")
lines.append("   ============================================================ */")
lines.append(":root {")

lines.append("\n  /* ── Color · Semantic (UI는 이 토큰만 사용) ── */")
for leaf in colors:
    if leaf.startswith("color_effect_"):   # 섀도 합성에 쓰이므로 별도 노출 생략
        continue
    lines.append(f"  {color_var(leaf)}: {colors[leaf]};")

lines.append("\n  /* ── Spacing (8pt 그리드) ── */")
for leaf in dims:
    if leaf.startswith("spacing_"):
        lines.append(f"  {dim_var(leaf)}: {dims[leaf]};")

lines.append("\n  /* ── Radius ── */")
for leaf in dims:
    if leaf.startswith("border_radius_"):
        lines.append(f"  {dim_var(leaf)}: {dims[leaf]};")

lines.append("\n  /* ── Border Width ── */")
for leaf in dims:
    if leaf.startswith("border_width_"):
        lines.append(f"  {dim_var(leaf)}: {dims[leaf]};")

lines.append("\n  /* ── Typography ── */")
for leaf in typo:
    v = css_value(leaf, typo[leaf], "typo")
    lines.append(f"  {typo_var(leaf)}: {v};")

lines.append("\n  /* ── Motion (source: motion.md) ── */")
for k, v in MOTION.items():
    lines.append(f"  {k}: {v};")

lines.append("\n  /* ── Shadow (effect_shadow 합성) ── */")
for k, v in SHADOW.items():
    lines.append(f"  {k}: {v};")

lines.append("\n  /* ── Spacing (미세·대형 스텝) ── */")
for k, v in EXTRA_SPACE.items():
    lines.append(f"  {k}: {v};")

lines.append("\n  /* ── Layout (container · grid · 섹션 리듬) ── */")
for k, v in LAYOUT.items():
    lines.append(f"  {k}: {v};")

lines.append("\n  /* ── Breakpoint (JS·문서 참조용) ── */")
for k, v in BREAKPOINT.items():
    lines.append(f"  {k}: {v};")

lines.append("\n  /* ── Elevation (선 대신 깊이) ── */")
for k, v in ELEVATION.items():
    lines.append(f"  {k}: {v};")

lines.append("\n  /* ── Color · Primitive (참고용 — 직접 사용 금지) ── */")
for leaf, v in primitives.items():
    lines.append(f"  --p-{leaf.replace('_', '-')}: {resolve(v)};")

lines.append("}")

# ── 다크 테마: 색상 토큰만 오버라이드 ──
def dark_rules(indent):
    out = []
    for leaf in colors:
        if leaf.startswith("color_effect_"):
            continue
        out.append(f"{indent}{color_var(leaf)}: {dark_colors[leaf]};")
    return out

lines.append('\n/* ── Dark theme (수동: [data-theme="dark"]) ── */')
lines.append('[data-theme="dark"] {')
lines += dark_rules("  ")
lines.append("}")

lines.append('\n/* ── Dark theme (자동: OS 설정 — light 명시 시 제외) ── */')
lines.append("@media (prefers-color-scheme: dark) {")
lines.append('  :root:not([data-theme="light"]) {')
lines += dark_rules("    ")
lines.append("  }")
lines.append("}")

(DIST / "tokens.css").write_text("\n".join(lines) + "\n", encoding="utf-8")

# ── 5. tokens.resolved.json (평탄 맵) ────────────────────────────────────
resolved = {}
for k, v in flat.items():
    try:
        rv = resolve(v)
        resolved[k] = num(rv) if types.get(k) == "number" else rv
    except KeyError as e:
        resolved[k] = f"<UNRESOLVED {e}>"
(DIST / "tokens.resolved.json").write_text(
    json.dumps(resolved, ensure_ascii=False, indent=2), encoding="utf-8")

# ── 6. tokens.tailwind.js (preset) ───────────────────────────────────────
def split_color(leaf):                     # color_bg_interactive_primary-hover -> ('bg','interactive-primary-hover')
    body = leaf[len("color_"):]
    role, _, rest = body.partition("_")
    return role, rest.replace("_", "-")

tw_colors = {}
for leaf in colors:
    if leaf.startswith("color_effect_"):
        continue
    role, rest = split_color(leaf)
    tw_colors.setdefault(role, {})[rest or "DEFAULT"] = f"var({color_var(leaf)})"

tw_spacing = {leaf.split("_", 1)[1]: f"var({dim_var(leaf)})"
              for leaf in dims if leaf.startswith("spacing_")}
tw_radius = {leaf.split("border_radius_", 1)[1]: f"var({dim_var(leaf)})"
             for leaf in dims if leaf.startswith("border_radius_")}

tw = {
    "theme": {
        "extend": {
            "colors": tw_colors,
            "spacing": tw_spacing,
            "borderRadius": tw_radius,
            "boxShadow": {k.replace("--shadow-", ""): f"var({k})" for k in SHADOW},
            "transitionTimingFunction": {
                k.replace("--motion-easing-", ""): f"var({k})"
                for k in MOTION if "easing" in k
            },
            "transitionDuration": {
                k.replace("--motion-duration-", ""): f"var({k})"
                for k in MOTION if "duration" in k
            },
        }
    }
}
js = ("// DDS v2.0 Tailwind preset (생성 파일 — 직접 수정 금지)\n"
      "// regenerate: python3 scripts/build_tokens.py\n"
      "// 사용: presets: [require('./dist/tokens.tailwind.js')] + dist/tokens.css import\n"
      "module.exports = " + json.dumps(tw, ensure_ascii=False, indent=2) + ";\n")
(DIST / "tokens.tailwind.js").write_text(js, encoding="utf-8")

# ── 요약 ─────────────────────────────────────────────────────────────────
unresolved = [k for k, v in resolved.items() if str(v).startswith("<UNRESOLVED")]
print(f"✓ dist/tokens.css            ({len(colors)-2} color + {len(dims)} dim + {len(typo)} typo + motion/shadow)")
print(f"✓ dist/tokens.resolved.json  ({len(resolved)} tokens)")
print(f"✓ dist/tokens.tailwind.js")
if unresolved:
    print(f"⚠ 미해석 참조 {len(unresolved)}개: {unresolved}")
else:
    print("✓ 끊긴 참조 없음")
# 플레이스홀더 경고
ph = [k for k, v in resolved.items() if v == "String value"]
if ph:
    print(f"⚠ 플레이스홀더('String value') {len(ph)}개: {ph}  (Figma에서 실제 값 입력 필요)")
