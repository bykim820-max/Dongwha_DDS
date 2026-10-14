---
name: ui
description: Dongwha Design System(DDS) 규칙으로 UI를 만들거나 고칠 때 사용한다. 프로젝트에 DDS_VERSION 파일이나 "DDS v" 헤더가 있는 tokens.css가 있을 때, 또는 사용자가 DDS·동화 디자인시스템·디자인 토큰을 언급할 때, 화면·컴포넌트·스타일·UI 문구를 만들거나 수정하기 전에 반드시 먼저 사용한다. Use before building or editing UI screens, components, styles, or UI copy in a project that uses DDS.
---

# DDS로 UI 만들기

이 프로젝트에 **고정된 DDS 버전**의 규칙과 토큰으로 작업한다. 최신 버전의 문서가 아니다.
프로젝트는 v2.5.0을 쓰는데 v2.6.0 문서를 보고 코드를 쓰면, v2.6.0에만 있는 토큰을 써서 화면이 깨진다.

```
REPO = https://github.com/bykim820-max/Dongwha_DDS.git
RAW  = https://raw.githubusercontent.com/bykim820-max/Dongwha_DDS
```

## 1. 고정 버전 확인 — 작업마다 첫 단계

**DDS 저장소 자체**(루트에 `VERSION`과 `plugins/dds/`가 있음)에서는 이 스킬을 적용하지 않는다. 그 저장소의 `AGENTS.md`를 직접 따른다.

```bash
find . -name DDS_VERSION -not -path "*/node_modules/*" 2>/dev/null
```

- 있으면 그 내용이 버전이다 (`2.5.0` → 태그 `v2.5.0`). 같은 폴더의 `tokens.css`가 이 프로젝트의 토큰이다.
- 없는데 `tokens.css` 헤더에 `DDS v`가 있으면:
  - `DDS v2.5.0` 이상 → 그 버전을 쓴다.
  - `DDS v2.0` → **레거시 파일.** v2.4.0 이전 파일은 내용과 무관하게 전부 v2.0으로 찍혀 있었다. 실제 버전을 모르므로 사용자에게 알리고 `/dds:check`를 권한다. 작업은 4번 규칙(프로젝트 tokens.css의 이름만)으로 계속한다.
- 둘 다 없으면 이 프로젝트는 아직 DDS를 가져오지 않았다. `/dds:init`을 권하고, 사용자가 원하지 않으면 이 스킬을 적용하지 않는다.

## 2. 그 버전의 규칙을 읽는다

```bash
curl -fsSL "$RAW/v<버전>/AGENTS.md"
```

AGENTS.md의 **§1 읽는 순서 · §2 절대 규칙 · §3.1 코드 생성 절차**를 따른다. §1이 가리키는 문서(제품 문맥 · 금지 규칙 · 컴포넌트 §0)도 같은 태그에서 받는다.

- 404이면 v2.5.0 이전 버전이라 AGENTS.md가 없다. 최신 태그(`git ls-remote --tags --refs https://github.com/bykim820-max/Dongwha_DDS.git`의 가장 높은 `vX.Y.Z`)의 `AGENTS.md`를 읽되, **토큰 이름은 반드시 4번 규칙**을 따르고, 사용자에게 `/dds:upgrade`를 권한다.
- 문서를 받지 못했으면 규칙을 **지어내지 않는다.** 사용자에게 알리고 4번 규칙만 지키며 진행한다.

## 3. 컴포넌트는 그 버전 문서의 §0 선택 기준부터

```bash
curl -fsSL "$RAW/v<버전>/components/README.md"        # 카탈로그
curl -fsSL "$RAW/v<버전>/components/<이름>.md"         # 예: button.md
```

§0 선택 기준이 있으면 그것부터 — 이 컴포넌트가 맞는지 먼저 판단한다. 카탈로그에 없는 컴포넌트를 새로 만들지 않는다.

## 4. 토큰 이름은 프로젝트의 tokens.css에 있는 것만

**문서에 나온 토큰이라도 이 프로젝트의 `tokens.css`에 없으면 쓰지 않는다.** 더 새 버전에서 추가된 토큰이다.

```bash
grep -o -- "--[a-z0-9-]*:" <프로젝트 tokens.css 경로> | sort -u
```

필요한 토큰이 없으면 `[미확인: 토큰 부재 — <용도>]`로 표시하고 가장 가까운 것을 쓴다.

## 5. 끝나면 자가 보고

| 항목 | 기준 |
|---|---|
| 사용한 DDS 버전 | 1번에서 확인한 것 |
| 하드코딩 값 (hex · rgb · 임의 px) | 0건 |
| 하드코딩 UI 문자열 | 0건 (i18n 키 사용) |
| primary 버튼 개수 | 화면당 1개 — 예외면 근거 |
| 이모지 아이콘 | 0건 |
| `[미확인]` 목록 | 있으면 전부 나열 |

`[미확인]`이 있으면 사용자에게 이렇게 덧붙인다 — **"이 목록은 DDS 문서에 답이 없는 항목입니다. DDS 담당자(스마트워크팀)에게 전달하면 문서가 보완됩니다."**
