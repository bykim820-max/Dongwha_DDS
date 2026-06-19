# Dongwha Design System (DDS) v2.0

> 동화의 통합 디자인시스템. **AI 에이전트와 디자이너·개발자 모두가 한 곳에서** 토큰과 컴포넌트 사양을 확인할 수 있도록 정리한 문서 저장소.

![status](https://img.shields.io/badge/status-active-22c55e) ![version](https://img.shields.io/badge/version-2.0-2563eb) ![mode](https://img.shields.io/badge/mode-light-e5e7eb) ![font](https://img.shields.io/badge/font-Pretendard-111827)

---

## 🧭 무엇이 들어있나요

| 분야 | 위치 | 한 줄 요약 |
|------|------|-----------|
| 📘 **개요 · 철학** | [design.md](./design.md) | 3-레이어 토큰 아키텍처, 코드 매핑 규칙, LLM 변환 워크플로우 |
| 🎨 **Foundations** | [foundations/](./foundations/) | Colors · Typography · Spacing · Radius · State · Motion · Layout · Elevation |
| 🧩 **Components** | [components/](./components/) | Button · Input · Switch · Checkbox · Tooltip · Table 등 |

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
dds-design-system/
├── README.md                ← 지금 보는 파일
├── design.md                ← 인덱스 (단일 진실 소스)
├── foundations/             ← 디자인 토큰 (6 파일)
│   ├── colors.md
│   ├── typography.md
│   ├── spacing.md
│   ├── radius.md
│   ├── state.md
│   └── motion.md
└── components/              ← 컴포넌트 (10 파일)
    ├── README.md            ← 컴포넌트 카탈로그
    ├── button.md
    ├── input.md
    ├── switch.md
    ├── checkbox.md
    ├── option-group.md
    ├── tooltip.md
    ├── table.md
    ├── page-header.md
    └── icons.md
```

---

## 🎨 토큰 한눈에

| 카테고리 | 토큰 패턴 | 예시 |
|----------|-----------|------|
| 컬러 (Semantic) | `Color/<role>/<intent>` | `Color/bg/primary`, `Color/text/danger` |
| 간격 | `spacing/<n>` | `spacing/16` (= 16px) |
| 라디우스 | `border/radius/<size>` | `border/radius/md` (= 8px) |
| 타이포 (Heading) | `Heading/<size>` | `Heading/lg` |
| 타이포 (Body) | `body/<size>/<weight>` | `body/md/regular` |
| 모션 시간 | `motion/duration/<name>` | `motion/duration/base` (= 240ms) |
| 모션 이징 | `motion/easing/<name>` | `motion/easing/spring/soft` |

→ 자세한 표·CSS·Tailwind 매핑: [foundations/](./foundations/)

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
- **현재 모드**: Light (Dark는 Phase 2)

---

## 🛠 기여 방법

1. 새 컴포넌트 추가 시 [components/README.md](./components/README.md) 하단의 **10-섹션 템플릿** 준수
2. 토큰 추가/변경은 Figma 라이브러리 갱신 → 본 저장소 PR
3. 임의 hex/px 값 인라인 금지. **Semantic 토큰만 사용**
4. 모든 컴포넌트는 `prefers-reduced-motion` 미디어쿼리 포함
5. **이모지 아이콘 금지 · 라인 SVG 아이콘만 사용**, **AI스러운 그라데이션 띠/배너·맹목적 고밀도 지양** → [design.md § 디자인 금지 규칙](./design.md#-디자인-금지-규칙-anti-patterns)

---

## 📅 로드맵

- 🔜 **다크 모드** — 2026 Q3
- 🔜 **UX 라이팅 가이드** (한/영 다국어) — 2026 Q3–Q4
- 🔜 **JSON 토큰 연동** (Style Dictionary) — 2026 Q4
- 🔜 **Code Connect** — Figma ↔ React/Vue 1:1 매핑

---

*동화 디자인시스템 팀 · Pretendard 기반 · 2026*
