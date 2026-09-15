# DDS 에이전트 지침

> 이 저장소는 Dongwha Design System(DDS) v2.0의 단일 진실 소스(SSOT)다. 산출물은 **문서와 토큰**이다.
> 사람용 안내는 [README.md](./README.md), 설계 원칙은 [design.md](./design.md).
> 이 파일은 **에이전트가 작업 전에 읽는 규칙**이다. 이 저장소에서 문서를 편집할 때도, 다른 저장소에서 DDS로 화면을 만들 때도 적용된다.

---

## 1. 읽는 순서 — 작업 전 필수

| 순서 | 문서 | 왜 |
|---|---|---|
| 1 | [design.md § 제품 문맥](./design.md#-제품-문맥--이-시스템은-무엇을-위한-것인가) | 무엇을 위한 시스템인지. **문서에 없는 판단은 여기서 추론한다** |
| 2 | [design.md § 디자인 금지 규칙](./design.md#-디자인-금지-규칙-anti-patterns) | 이모지 아이콘 · 장식 그라데이션 · 맹목적 고밀도 · 채도 남발 — 예외 없음 |
| 3 | 작업 대상 컴포넌트의 **§0 선택 기준** (예: [button.md §0](./components/button.md)) | 그 컴포넌트가 맞는지 먼저 판단. 없으면 [components/README.md](./components/README.md) 카탈로그에서 찾는다 |
| 4 | 해당 [foundations/](./foundations/) 토큰 문서 | 값이 아니라 **토큰 이름**으로 쓴다 |
| 5 | [writing.md §4](./foundations/writing.md) · [i18n.md](./foundations/i18n.md) | 문구 · 다국어 |

---

## 2. 절대 규칙

1. **색 · 간격 · radius · 타이포는 토큰만.** hex · rgb · 임의 px 인라인 금지. `dist/tokens.css`의 `var(--*)`로 쓴다.
2. **토큰 이름은 `dist/tokens.css`에 있는 것만.** 없는 이름을 만들지 않는다. 필요한 토큰이 없으면 `[미확인: 토큰 부재 — <용도>]`로 표시하고 가장 가까운 것을 쓴다.
3. **`primary`는 세 가지 뜻이다 — 섞지 않는다.**
   - 버튼 위계 `primary` → 배경은 `Color/bg/interactive/primary` (브랜드 green)
   - `Color/bg/primary` → **페이지 표면** (흰색). 버튼에 쓰지 않는다
   - `Color/text/primary` → 본문 텍스트
   - 면 `bg/*` vs 누르는 것 `bg/interactive/*` 구분 → [colors.md §5](./foundations/colors.md)
4. **컴포넌트는 있는 것을 쓴다.** 비슷한 것을 새로 만들지 않는다. 카탈로그에 없으면 `[미확인: 컴포넌트 부재 — <이름>]`로 표시하고 가장 가까운 것을 쓴다.
5. **한 화면에 primary 버튼 1개.** 예외는 [button.md §3.2](./components/button.md)의 표에 있는 경우만.
6. **UI 문자열은 i18n 키.** 하드코딩 금지. 문안은 [writing.md](./foundations/writing.md) 패턴 — "확인 / 예 / OK" 금지, 오류 문구에는 "다음에 할 일" 포함.
7. **아이콘은 라인 SVG 한 세트**(`stroke="currentColor"`) → [icons.md](./components/icons.md). 이모지 · 유니코드 기호 금지.
8. **`<div onClick>` 금지.** 실행은 `<button>`, 이동은 `<a>` → [button.md §0](./components/button.md).
9. **문서에 규칙이 없으면 추론으로 채우지 않는다.** `[미확인: <무엇이 불명확한지>]`로 표시하고 질문한다. 추론한 것을 규칙처럼 쓰지 않는다.
10. **모션은 `prefers-reduced-motion` 포함**, 대비는 **WCAG AA** → [motion.md](./foundations/motion.md) · [colors.md §2.2.1](./foundations/colors.md).

---

## 3. 작업 유형별 절차

### 3.1 화면 · 컴포넌트 코드 생성 (DDS를 소비하는 저장소에서)

1. `dist/tokens.css` import (또는 `dist/tokens.tailwind.js` preset)
2. [design.md § LLM 에이전트 변환 워크플로우](./design.md#-llm-에이전트-변환-워크플로우) 8단계를 따른다
3. 화면 유형(목록 · 상세 · 폼 · 대시보드)에 맞게 [button.md §12 배치](./components/button.md) 표를 지킨다
4. 완료 전 자가 보고: 하드코딩 값 0건 · 하드코딩 문자열 0건 · primary 버튼 개수 · 이모지 0건 · `[미확인]` 목록

### 3.2 이 저장소의 문서 편집

- 컴포넌트 문서는 [components/README.md 템플릿](./components/README.md)을 따른다. **사양(무엇인가) + 문법(§0 선택 기준 · 배치 · 원칙의 예외)** 둘 다 — 기준선은 [navigation.md](./components/navigation.md) · [button.md](./components/button.md)
- **기존 `##` 절 번호를 바꾸지 않는다.** 다른 문서가 `§3` · `#8-icon-button` 같은 앵커로 참조한다. 새 절은 뒤에 붙이거나 `§0` · 하위 절로 넣는다
- 규칙은 **표 · 판별 질문 · Do/Don't**로 쓴다. 산문으로 늘어놓지 않는다
- 토큰 변경: `foundations/DDS_tokens_*.json` 수정 → `python3 scripts/build_tokens.py` → `dist/` 재생성. **`dist/`를 직접 편집하지 않는다**
- 완료한 것은 [design.md 로드맵 · 알려진 이슈](./design.md#-로드맵)를 같이 갱신한다. 완료됐는데 "예정"으로 남는 항목을 만들지 않는다
- 기존 문서와 모순되는 규칙을 발견하면 **둘 다 고치거나 알려진 이슈에 적는다.** 한쪽만 고쳐 두지 않는다

### 3.3 검증 — 커밋 전

```bash
python3 scripts/check_hardcoding.py                        # *.html 하드코딩 검사 — CI와 동일
python3 scripts/build_tokens.py && git diff --stat dist/   # 토큰을 바꿨다면 — diff가 비어야 한다
```

CI: [.github/workflows/validate.yml](./.github/workflows/validate.yml)

---

## 4. 하지 않는 것

- `metrics/` — 로컬 전용(`.gitignore`). 커밋 · 참조 · 내용 인용 금지
- Figma `componentKey`를 임의로 만들지 않는다. 미발급은 "미발급"으로 둔다 ([navigation.md §0](./components/navigation.md))
- `dist/` 직접 편집
- 사용자가 요청하지 않은 커밋 · 푸시

---

## 5. 다른 저장소에서 DDS를 쓰게 하기

DDS를 소비하는 저장소(예: ITSM)의 `AGENTS.md` 또는 `CLAUDE.md`에 아래를 넣는다. 경로는 그 환경의 절대 경로.

```markdown
# DDS 적용
이 프로젝트의 UI는 Dongwha Design System(DDS)을 따른다.
작업 전 /절대경로/Dongwha_DDS/AGENTS.md 를 읽고 그 규칙을 적용한다.
토큰: /절대경로/Dongwha_DDS/dist/tokens.css
```

---

*`AGENTS.md`는 벤더 중립 진입점이다. `CLAUDE.md`는 이 파일을 임포트한다.*
