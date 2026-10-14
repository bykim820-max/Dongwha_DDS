---
description: 이 프로젝트의 DDS 버전과 최신 버전을 비교하고, 올리면 무엇을 해야 하는지 보고한다 (읽기 전용)
allowed-tools: Bash, Read, Glob, Grep
---

이 프로젝트의 DDS 버전을 확인하고, 최신 버전과 비교해 **올릴 때 무엇을 해야 하는지** 보고한다.
**파일을 수정하지 않는다.**

```
REPO = https://github.com/bykim820-max/Dongwha_DDS.git
RAW  = https://raw.githubusercontent.com/bykim820-max/Dongwha_DDS
```

## 1. 현재 버전

```bash
find . \( -name DDS_VERSION -o -name tokens.css \) -not -path "*/node_modules/*" 2>/dev/null
```

- `DDS_VERSION`의 내용이 현재 버전이다.
- 없는데 `tokens.css` 헤더가 `DDS v2.0`이면 **레거시 파일**이다. 최신 태그(2번)의 `CHANGELOG.md` "먼저 읽어주세요" 판별표로 실제 버전을 추정한다 — 프로젝트 tokens.css에서 `--topbar-h` 유무와 `--color-text-warning` 값을 확인한다. 추정한 버전과 근거를 보고에 적는다.
- 둘 다 없으면 `/dds:init`을 안내하고 끝낸다.

## 2. 최신 버전

```bash
git ls-remote --tags --refs https://github.com/bykim820-max/Dongwha_DDS.git
```

`refs/tags/vX.Y.Z` 중 가장 높은 것. `dds--v*`는 무시한다.
같으면 **"최신 버전(vX.Y.Z)을 쓰고 있습니다."** 로 끝낸다.

## 3. 사이에 무엇이 바뀌었나

```bash
curl -fsSL "$RAW/v<최신>/CHANGELOG.md"
curl -fsSL "$RAW/v<최신>/MIGRATION.md"
```

**`main` 브랜치는 읽지 않는다.** `main`은 작업 중인 내용이고, 태그가 붙은 것만 공개된 버전이다.

CHANGELOG에서 **현재 버전 초과 ~ 최신 버전 이하**의 절만 읽는다. 버전마다 추가 · 변경 · ⚠️ 확인 필요를 정리한다.

## 4. 이 프로젝트에 실제로 해당하는지 확인

- **⚠️ 확인 필요** 항목마다 MIGRATION.md §4의 대응 절을 찾아, 그 절의 **"찾기" 명령을 이 프로젝트에서 실행**한다. 걸린 파일·줄을 보고한다. 걸렸어도 대응 절이 "올바른 사용"이라고 하는 경우(예: 페이지 배경에 면 토큰)는 구분해서 적는다.
- **변경**(토큰 값) 항목 — 바뀐 토큰을 쓰는 파일 수를 센다. 그 화면은 받은 뒤 눈으로 확인해야 한다.
- **사라질 토큰** — 이 프로젝트가 쓰는 `var(--*)` 중 최신 `tokens.css`에 없는 것:

```bash
curl -fsSL "$RAW/v<최신>/dist/tokens.css" | grep -o -- "--[a-z0-9-]*:" | tr -d ':' | sort -u > /tmp/dds-new.txt
grep -rhoE "var\(--[a-z0-9-]+" --include="*.css" --include="*.scss" --include="*.vue" --include="*.tsx" --include="*.jsx" --include="*.ts" . 2>/dev/null | grep -v node_modules | sed 's/var(//' | sort -u > /tmp/dds-used.txt
comm -23 /tmp/dds-used.txt /tmp/dds-new.txt
```

결과에는 DDS가 아닌 프로젝트 자체 변수도 섞여 있다. DDS 토큰 접두어(`--color-` · `--space-` · `--radius-` · `--font-` · `--motion-` · `--shadow-` · `--elevation-` 등)만 골라 보고한다.

## 5. 보고

```
현재 v<현재>  →  최신 v<최신>

| 구분 | 내용 | 이 프로젝트 |
|---|---|---|
| ⚠️ 확인 필요 | ... | N곳 해당 (파일:줄) / 해당 없음 |
| 변경 (값) | ... | N개 파일이 사용 — 화면 확인 필요 |
| 추가 | ... | 영향 없음 |
| 사라지는 토큰 | ... | N개 사용 중 |

결론: 받기만 하면 됨 / 코드 수정 N곳 필요
→ 올리려면 /dds:upgrade
```
