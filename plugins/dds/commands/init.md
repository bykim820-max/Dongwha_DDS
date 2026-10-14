---
description: 이 프로젝트에 DDS 토큰을 버전 고정으로 처음 가져온다
argument-hint: "[버전 — 예: 2.5.0, 생략하면 최신]"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

이 프로젝트에 Dongwha Design System(DDS) 토큰을 **버전을 고정해서** 처음 가져온다.

```
REPO = https://github.com/bykim820-max/Dongwha_DDS.git
RAW  = https://raw.githubusercontent.com/bykim820-max/Dongwha_DDS
```

## 1. 이미 가져왔는지 확인

```bash
find . \( -name DDS_VERSION -o -name tokens.css \) -not -path "*/node_modules/*" 2>/dev/null
```

- `DDS_VERSION`이 있으면 **중단**한다. 이미 설정된 프로젝트다 — `/dds:check`를 안내한다.
- `DDS_VERSION`은 없고 헤더에 `DDS v`가 있는 `tokens.css`가 있으면 **레거시 파일**이다 (v2.4.0 이전 파일은 헤더가 전부 `v2.0`). 최신 태그(`git ls-remote --tags --refs https://github.com/bykim820-max/Dongwha_DDS.git`의 가장 높은 `vX.Y.Z`)의 `CHANGELOG.md` "먼저 읽어주세요" 판별표로 실제 버전을 추정해 보고하고, 새 버전으로 교체할지 **사용자에게 묻는다.** 교체하기로 하면 `/dds:check`의 ⚠️ 확인 필요 점검을 먼저 하도록 안내한다.

## 2. 버전 정하기

- 인자가 있으면 그 버전: `$ARGUMENTS`
- 없으면 최신 태그:

```bash
git ls-remote --tags --refs https://github.com/bykim820-max/Dongwha_DDS.git
```

`refs/tags/vX.Y.Z` 형식 중 가장 높은 버전을 고른다. `dds--v*`는 플러그인 자체의 태그이므로 무시한다.

## 3. 둘 위치 정하기

프로젝트의 스타일 폴더를 찾아 제안한다 (`src/styles/`, `src/assets/styles/`, `assets/css/`, `styles/` 등). 없으면 `src/styles/dds/`를 기본으로 제안한다. **사용자 확인 후** 진행한다.

## 4. 받기

```bash
curl -fsSL "$RAW/v<버전>/dist/tokens.css" -o <위치>/tokens.css
head -3 <위치>/tokens.css     # 헤더에 DDS v<버전>이 찍혀 있어야 한다
```

- Tailwind 설정 파일(`tailwind.config.*`)이 있으면 `dist/tokens.tailwind.js`도 받는다.
- 문서(`*.md`)는 **받지 않는다.** 복사본은 반드시 낡는다. 필요할 때 태그에서 읽는다.

## 5. 버전 기록

```bash
echo "<버전>" > <위치>/DDS_VERSION
```

## 6. 연결 제안 — 수정은 승인 후

1. **전역 CSS 진입점에 import** — 프레임워크에 맞게 찾아 제안한다 (Nuxt `nuxt.config`의 `css`, Vite `main.*`, Next `app/layout.*` 등).
2. **프로젝트의 `CLAUDE.md`(없으면 `AGENTS.md`)에 DDS 절 추가** — 플러그인이 없는 팀원도 규칙을 찾을 수 있게:

```markdown
## DDS
이 프로젝트의 UI는 Dongwha Design System(DDS)을 따른다.
- 토큰: <위치>/tokens.css — 버전 고정 복사본, 직접 수정 금지
- 버전: <위치>/DDS_VERSION
- UI 작업 전 규칙: https://github.com/bykim820-max/Dongwha_DDS/blob/v<버전>/AGENTS.md
- Claude Code dds 플러그인이 있으면 dds:ui 스킬이 이 규칙을 적용한다. 새 버전 확인은 /dds:check
```

## 7. 보고

받은 버전 · 파일 위치 · 수정한 파일 · 남은 할 일(import 등)을 표로 보고한다.
**커밋하지 않는다** — 사용자가 요청할 때만.
