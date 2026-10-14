---
description: 이 프로젝트의 DDS를 새 버전으로 올린다 — 코드 수정이 필요한 항목부터 처리하고 토큰을 교체한다
argument-hint: "[목표 버전 — 생략하면 최신]"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

이 프로젝트의 DDS를 새 버전으로 올린다. 순서가 중요하다 — **파일만 교체하면 안 고쳐지는 항목**이 있다.

```
REPO = https://github.com/bykim820-max/Dongwha_DDS.git
RAW  = https://raw.githubusercontent.com/bykim820-max/Dongwha_DDS
```

## 1. 현재 · 목표 버전

- 현재: `DDS_VERSION`. 없으면 `/dds:check`의 1번 방법(레거시 판별)으로 추정하고, 추정이라는 사실을 사용자에게 알린다. `DDS_VERSION`도 `tokens.css`도 없으면 `/dds:init`을 안내하고 끝낸다.
- 목표: `$ARGUMENTS`, 없으면 최신 태그 (`git ls-remote --tags --refs https://github.com/bykim820-max/Dongwha_DDS.git`, `dds--v*` 무시).
- 목표가 현재보다 낮거나 같으면 중단하고 사용자에게 묻는다.

## 2. 분석

`/dds:check`의 3·4번과 같은 분석을 한다 — 구간 CHANGELOG, ⚠️ 확인 필요 해당 위치, 값 변경 토큰 사용 파일, 사라지는 토큰.
**MAJOR가 바뀌면**(예: 2.x → 3.0) 사라지는 토큰이 있을 수 있다. MIGRATION.md의 해당 버전 대응표를 반드시 읽는다.

## 3. 계획을 보여주고 승인받기

아래를 표로 보여주고 **사용자 승인 전에는 아무것도 수정하지 않는다.**

| 단계 | 대상 | 내용 |
|---|---|---|
| 코드 수정 | 파일:줄 | ⚠️ 항목 — MIGRATION.md §4 대응표 그대로 |
| 토큰 이름 교체 | 파일:줄 | 사라지는 토큰 → 대응표의 새 이름 (MAJOR일 때) |
| 파일 교체 | `tokens.css` 등 | v<현재> → v<목표> |
| 버전 기록 | `DDS_VERSION` | <현재> → <목표> |
| 확인 필요 화면 | 화면 목록 | 값이 바뀐 토큰을 쓰는 화면 — 라이트·다크 |

## 4. 코드 수정 — 파일 교체보다 먼저

- MIGRATION.md §4 대응표대로 고친다.
- **판단이 갈리는 곳은 묻는다.** 예: `--color-bg-primary`가 버튼 배경이면 고치고, 페이지·카드 배경이면 올바른 사용이라 그대로 둔다. 어느 쪽인지 코드만으로 확실하지 않으면 사용자에게 묻는다.
- 대응표에 없는 판단을 지어내지 않는다.

## 5. 파일 교체

지금 있는 파일과 **같은 위치, 같은 파일 세트**로 교체한다.

```bash
curl -fsSL "$RAW/v<목표>/dist/tokens.css" -o <위치>/tokens.css
head -3 <위치>/tokens.css        # DDS v<목표> 확인
```

`tokens.tailwind.js`가 있었으면 그것도 같은 버전으로 교체한다.

## 6. 버전 기록

```bash
echo "<목표>" > <위치>/DDS_VERSION
```

`DDS_VERSION`이 없던 레거시 프로젝트면 새로 만든다.

## 7. 검증

- 4번 "사라지는 토큰" 검사를 다시 실행해 DDS 토큰이 0개인지 확인한다.
- 프로젝트에 빌드·린트 명령이 있으면 실행한다.

## 8. 보고

수정한 파일 · 교체한 파일 · 바뀐 버전 · **눈으로 확인할 화면 목록(라이트·다크)** 을 보고한다.
**커밋하지 않는다** — 사용자가 요청할 때만. 커밋 메시지를 원하면 `chore(dds): v<현재> → v<목표>` 형식을 제안한다.
