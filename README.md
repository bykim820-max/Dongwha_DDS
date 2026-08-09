# Dongwha Design System (DDS) v2.0

> 동화의 통합 디자인시스템. **AI 에이전트와 디자이너·개발자 모두가 한 곳에서** 토큰과 컴포넌트 사양을 확인할 수 있도록 정리한 문서 저장소.

![status](https://img.shields.io/badge/status-active-22c55e) ![version](https://img.shields.io/badge/version-2.0-2563eb) ![mode](https://img.shields.io/badge/mode-light%20%2B%20dark-6366f1) ![font](https://img.shields.io/badge/font-Pretendard-111827)

---

## 🧭 무엇이 들어있나요

| 분야 | 위치 | 한 줄 요약 |
|------|------|-----------|
| 📘 **개요 · 철학** | [design.md](./design.md) | 3-레이어 토큰 아키텍처, 코드 매핑 규칙, LLM 변환 워크플로우 |
| 🎨 **Foundations** | [foundations/](./foundations/) | Colors · Typography · Spacing · Radius · State · Motion · Layout · Elevation |
| 🧩 **Components** | [components/](./components/) | Button · Input · Switch · Checkbox · Tooltip · Table 등 |
| ✍️ **UX Writing** | [foundations/writing.md](./foundations/writing.md) | 보이스·톤, 버튼·오류·안내 문구 규칙, 용어 사전 |
| 🌐 **다국어(i18n)** | [foundations/i18n.md](./foundations/i18n.md) | 문자열 키, 확장률, ICU 복수형, 날짜·숫자·통화, 한↔영 대응 |
| 🧪 **라이팅 샘플** | [examples/writing.html](./examples/writing.html) | 거래처 관리 화면 5가지 상황 — 규칙 위반 ↔ DDS 적용 비교 (한/영 토글) |

---

## ⚡ 빠른 시작

### 디자이너
1. [design.md](./design.md) 의 "디자인 철학" 섹션부터 읽기
2. [foundations/colors.md](./foundations/colors.md) 의 Semantic 토큰 매트릭스 숙지
3. Figma 작업 시 `Semantic` 토큰만 사용 (Primitive 직접 사용 금지)
4. 새 컴포넌트는 [components/README.md](./components/README.md) 의 문서 템플릿을 따라 정리

### 개발자
1. [design.md](./design.md) 의 "코드 매핑 핵심 규칙" 7가지 확인
2. **[dist/tokens.css](./dist/) 를 import** — 값이 실제 hex/px로 해석된 드롭인 토큰 (Tailwind는 `dist/tokens.tailwind.js` preset)
3. 컴포넌트 구현 시 [components/](./components/) 의 props·states 시그니처 참고
4. 모든 인터랙션에 [foundations/motion.md](./foundations/motion.md) 의 Duration·Easing 토큰 적용

### AI 에이전트 (LLM)
이 저장소는 raw URL로 직접 읽도록 설계되어 있습니다.

```
https://raw.githubusercontent.com/<owner>/dds-design-system/main/design.md
```

변환 워크플로우:
1. Figma `get_metadata` → 페이지 구조 파악
2. `search_design_system` → 토큰·컴포넌트 인덱스
3. `get_variable_defs` → 변수 값 추출
4. `get_design_context` → 코드 생성 컨텍스트
5. 이 저장소 문서 참조하여 **Semantic 토큰만 출력**

자세한 규칙: [design.md § LLM 에이전트 워크플로우](./design.md#-llm-에이전트-변환-워크플로우)

---

## 📂 폴더 구조

```
Dongwha_DDS/
├── README.md                ← 지금 보는 파일
├── design.md                ← 인덱스 (단일 진실 소스)
├── foundations/             ← 디자인 토큰·규범 (문서 10 + W3C 토큰 JSON 3)
│   ├── colors.md            (+ accent · chart · subtle · 다크 모드)
│   ├── typography.md        (+ 굵기 weight 축)
│   ├── spacing.md · radius.md · state.md · motion.md
│   ├── layout.md            ← Container · Grid · Breakpoint · SNB
│   ├── elevation.md         ← 의미 깊이 레벨
│   ├── writing.md           ← UX 라이팅 (버튼·오류·안내 문구 · 용어 사전)
│   ├── i18n.md              ← 다국어 (키 · 복수형 · 날짜/숫자 · 한↔영 대응)
│   ├── DDS_tokens_w3c.json       ← SSOT (primitive→semantic)
│   ├── DDS_tokens_extended.json  ← accent · chart · 굵기 토큰
│   └── DDS_tokens_dark.json      ← 다크 semantic 오버라이드
├── components/              ← 컴포넌트 (문서 12 + 카탈로그)
│   ├── README.md            ← 컴포넌트 카탈로그 · componentKey
│   ├── button.md · input.md · switch.md · checkbox.md · option-group.md
│   ├── table.md · page-header.md · icons.md · tooltip.md
│   ├── skeleton.md          ← 로딩 자리표시
│   ├── feedback.md          ← Toast · Alert · Spinner · Progress · Empty
│   └── overlay.md           ← Modal · Sheet · Drawer · Popover · Menu
├── scripts/build_tokens.py  ← 토큰 빌드 (JSON → dist, 경량 Style Dictionary)
├── dist/                    ← 생성물: tokens.css · tokens.resolved.json · tokens.tailwind.js
└── examples/                ← 데모 (dashboard · layout · feedback · overlay · dark · writing)
```

> `dist/`·`examples/`는 직접 수정 금지. 토큰은 JSON 수정 후 `python3 scripts/build_tokens.py`로 재생성.

---

## 🎨 토큰 한눈에

| 카테고리 | 토큰 패턴 | 예시 |
|----------|-----------|------|
| 컬러 (Semantic) | `--color-<role>-<intent>` | `--color-bg-primary`, `--color-text-danger` |
| 컬러 (Accent·Chart) | `--color-accent-<hue>`, `--color-chart-<n>` | `--color-accent-violet`, `--color-chart-1` |
| 틴트 면 | `--color-bg-<intent>-subtle` | `--color-bg-success-subtle` |
| 간격 | `--space-<n>` | `--space-16` (= 16px) |
| 라디우스 | `--radius-<size>` | `--radius-md` (= 4px) |
| 타이포 | `--heading-<sz>-*` · `--body-<sz>-*` | `--heading-lg-font-size` |
| 굵기 | `--font-weight-<name>` | `--font-weight-medium` (= 500) |
| 레이아웃 | `--container-*` · `--grid-*` · `--snb-width` | `--container-dashboard` (1680), `--snb-width` (270) |
| 깊이 | `--elevation-<level>` | `--elevation-raised`, `--elevation-modal` |
| 모션 | `--motion-duration-*` · `--motion-easing-*` | `--motion-duration-base` (= 240ms) |

→ 실제 값이 채워진 토큰: **[dist/tokens.css](./dist/)** · 자세한 표·매핑: [foundations/](./foundations/)

---

## 🧩 컴포넌트 한눈에

```
Actions          ▸ Button · Icon Button · Button Stack
Form Inputs      ▸ Input · Switch · Checkbox · Option Group
Feedback         ▸ Tooltip · Skeleton · Toast · Inline Alert · Spinner · Progress · Empty State
Overlay          ▸ Modal · Bottom Sheet · Drawer · Popover · Dropdown Menu
Data Display     ▸ Table
Layout           ▸ Page Header
Foundation       ▸ Icon System
```

→ 자세한 변형·상태·코드: [components/README.md](./components/README.md)

---

## 🔗 소스

- **Figma 파일**: [`2026_DDS_v2_배포용`](https://www.figma.com/design/tDGeNJRNR2vCZu5bVdmoNc/2026_DDS_v2_%EB%B0%B0%ED%8F%AC%EC%9A%A9)
- **폰트**: Pretendard
- **모드**: Light · Dark (`[data-theme="dark"]` / OS 자동)

---

## 🛠 기여 방법

1. 새 컴포넌트 추가 시 [components/README.md](./components/README.md) 하단의 **10-섹션 템플릿** 준수
2. 토큰 추가/변경은 Figma 라이브러리 갱신 → 본 저장소 PR
3. 임의 hex/px 값 인라인 금지. **Semantic 토큰만 사용**
4. 모든 컴포넌트는 `prefers-reduced-motion` 미디어쿼리 포함
5. **이모지 아이콘 금지 · 라인 SVG 아이콘만 사용**, **AI스러운 그라데이션 띠/배너·맹목적 고밀도 지양** → [design.md § 디자인 금지 규칙](./design.md#-디자인-금지-규칙-anti-patterns)
6. **UI 문자열 하드코딩 금지** — i18n 키로 작성하고 문안은 [writing.md](./foundations/writing.md) 패턴 준수

---

## 📅 로드맵

- ✅ **토큰 빌드 파이프라인** — `build_tokens.py` → `dist/` (경량 Style Dictionary)
- ✅ **다크 모드** — semantic 다크 토큰 + `[data-theme]` / OS 자동
- ✅ **레이아웃·Elevation·피드백·오버레이** 추가
- ✅ **UX 라이팅 가이드** — [writing.md](./foundations/writing.md) + 한/영 다국어 [i18n.md](./foundations/i18n.md)
- 🔜 **내비게이션 컴포넌트** — Tabs · Segmented · Breadcrumb
- 🔜 **거버넌스** — stylelint(hex·px·이모지 차단) + 빌드 검증 CI + i18n 키 검증
- 🔜 **Code Connect** — Figma ↔ React/Vue 1:1 매핑

---

## 📝 변경 이력 (요약)

| 버전 | 변경 |
|------|------|
| 2.2 | **UX 라이팅 가이드**(보이스·톤, 버튼/오류/안내 문구 규칙, 용어 사전), **다국어(i18n)** 규범(문자열 키·확장률·ICU 복수형·`Intl` 포맷·한↔영 용어 대응) |
| 2.1 | 토큰 빌드 파이프라인(`dist/`), Accent·Chart·Subtle 컬러, 타이포 굵기 축(body 400), Layout·Elevation 파운데이션, SNB(270·좌측), Skeleton·Feedback·Overlay 컴포넌트, **다크 모드**, 디자인 금지 규칙(이모지·그라데이션 띠·고밀도) |
| 2.0 | 3-레이어 토큰, W3C 토큰 export, 오타 정정(neutral 등), 기본 컴포넌트 카탈로그 |

> 상세 이력은 git 커밋 로그 참조.

---

*동화 스마트워크팀 김부영 · 2026*
