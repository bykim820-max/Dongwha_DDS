# Dongwha Design System (DDS) v2.0

> 동화 디자인시스템 v2.0의 단일 진실 소스(SSOT).
> AI 에이전트와 사람이 모두 읽기 좋은 구조로 정리한 디자인 가이드.

---

## 🧭 제품 문맥 — 이 시스템은 무엇을 위한 것인가

> **모든 문서에 앞서 읽는 전제.** 토큰·컴포넌트 문서가 답하지 않는 판단은 이 문맥에서 추론한다.
> `[미확인]` 표시는 아직 답이 없는 항목이다. AB 실험(로드맵 v2.5 항목 2) 중에 채운다.

### 어떤 제품인가

| 항목 | 내용 |
|---|---|
| 제품 유형 | **사내 업무 시스템(B2B 운영 도구) 전반.** ITSM 리뉴얼을 시작으로 거래처·주문·인사 등 다른 사내 시스템의 **관리자 화면**으로 확대한다 |
| 대표 화면 유형 | 목록+필터 · 상세 · 등록/수정 폼 · 마스터 관리 · 다중 탭·폼 복합 화면 · 대시보드 |
| **아닌 것** | 마케팅 사이트 · 소비자 앱 · 랜딩 페이지 · 게임. **첫인상이 아니라 매일의 반복 사용**을 위한 시스템이다 |

### 누가, 어떻게 쓰는가

| 항목 | 내용 |
|---|---|
| 사용자 | **디지털혁신실(IT 부서) 담당자**가 주 사용자. 시스템 운영·관리 업무를 수행한다 |
| 사용 패턴 | **하루 수 시간 상주.** 같은 화면을 수십 번 연다. 대부분 숙련 사용자이며 처음 보는 사람은 소수다 |
| 기기 | **데스크톱 우선** (1280~1680 와이드). 모바일도 쓰지만 **보기·승인 수준**이며 웹만큼 깊지 않다 — `md`(768) 미만에서는 열람·승인 흐름만 축약형으로 제공하고, 등록·편집 등 깊은 작업은 데스크톱 전제로 설계한다 |
| 언어 | **다국어 필수.** 한국어·영어는 기본 지원, **베트남어**는 일부 화면·사용자에 한해 지원. 모든 UI 문자열은 i18n 키로 → [i18n.md](./foundations/i18n.md). ⚠️ 베트남어는 i18n.md에 아직 미반영 (§ 알려진 이슈) |

### 그래서 이렇게 생겼다 — 판단의 근거

위 문맥이 DDS의 규칙을 결정했다. **문서에 없는 상황도 같은 논리로 판단한다.** 링크가 있는 항목은 이미 문서화된 규칙, 없는 항목은 이 문맥에서 도출한 원칙이다.

- **상주 사용 → 절제된 채도.** 눈이 피로하지 않게. 브랜드 green은 주요 액션에만, 장식 그라데이션·배너 금지 → [§ 금지 규칙](#-디자인-금지-규칙-anti-patterns)
- **반복 사용 → 예측 가능성이 신선함보다 우선.** 같은 역할은 항상 같은 자리·같은 모양. 화면마다 새로운 시도를 하지 않는다
- **숙련 사용자 → 설명은 짧게, 경로는 빠르게.** 온보딩식 안내·환영 문구 배제. 키보드 조작·일괄 처리를 우선 고려
- **데이터 중심 → 표가 기본 표현.** 목록은 [Table](./components/table.md)로. 카드는 대시보드 요약에 한정하고 **목록을 카드로 만들지 않는다**
- **데스크톱 우선 → 와이드 멀티컬럼이 기본**, 모바일은 축약형. 모바일 우선으로 설계하지 않는다 → [layout.md §5](./foundations/layout.md)
- **업무 오류는 비용 → 파괴적 액션은 항상 확인 단계**, 오류 문구에는 항상 "다음에 할 일" → [button.md § Do/Don't](./components/button.md) · [writing.md](./foundations/writing.md)
- **읽기 쉬운 밀도 → 욱여넣지 않되, 데이터 그리드는 고밀도 허용** → [§ 금지 규칙 3](#-디자인-금지-규칙-anti-patterns)
- **장시간 응시 → 대비는 WCAG AA 이상**, 다크 모드 지원 → [colors.md](./foundations/colors.md)

### "우리 화면답다"의 기준

새 화면이 아래와 나란히 놓였을 때 **이질감이 없어야 한다.** 판단이 갈리면 이 화면들을 열어 비교한다.

| 화면 | 유형 | 기준이 되는 것 |
|---|---|---|
| [examples/writing.html](./examples/writing.html) | 목록 + 폼 (거래처 관리) | 문구 · 상태 · 빈 상태 처리 |
| [examples/dashboard.html](./examples/dashboard.html) | 대시보드 | 와이드 레이아웃 · SNB · 카드 요약 |
| [examples/layout.html](./examples/layout.html) | 레이아웃 뼈대 | 간격 리듬 · 컨테이너 · 그리드 |
| `[미확인]` ITSM 실서비스 화면 1~2개 | 실제 제품 | 문서가 아닌 **실제 결과물**의 기준. AB 실험 조건 B 화면 중에서 선정한다 |

> 예제 3종은 컴포넌트 시연용이라 "실제 제품"의 기준으로는 부족하다. **ITSM 실서비스 화면을 여기 추가하는 것이 로드맵 v2.5 항목 1의 완료 조건**이다.

### 레거시와의 관계

2024 `동화디자인시스템_배포용`(GNB·LNB·SNB 3층 내비게이션)을 DDS v2가 **계승·대체**한다. 용어 대응은 [navigation.md §7.2](./components/navigation.md). 레거시 실측값(헤더 높이 등)은 근거로 인용하되, **새 화면은 DDS v2 토큰만 쓴다.** `[미확인]` 레거시 시스템 병행 운영 여부·기간

---

## 📚 문서 구조

### Foundations (디자인 토큰)

| 문서 | 내용 |
|------|------|
| [Colors](./foundations/colors.md) | Primitive · Semantic 컬러 토큰, 32-슬롯 매트릭스 |
| [Typography](./foundations/typography.md) | Heading · Body 스케일, Pretendard, Letter Spacing |
| [Spacing](./foundations/spacing.md) | 8pt 그리드, `spacing/0` ~ `spacing/64` |
| [Radius](./foundations/radius.md) | `border/radius/sm` ~ `rounded` |
| [State](./foundations/state.md) | default · hover · focus · disabled · error · loading |
| [Motion](./foundations/motion.md) | Duration · Easing · 인터랙션 레시피 10종 |
| [Layout](./foundations/layout.md) | 간격 리듬(섹션·블록·스택) · Container · 12컬럼 Grid · Breakpoint |
| [Elevation](./foundations/elevation.md) | 의미 깊이 레벨(raised·overlay·modal…) ↔ shadow 매핑, "선 대신 깊이" |
| [UX Writing](./foundations/writing.md) | 보이스·톤, 문장 규칙, 버튼·오류·안내 문구 패턴, 용어 사전 |
| [라이팅 체크리스트](./foundations/writing-checklist.md) | 리뷰·PR용 1장 점검표. 규범서 대신 이걸로 검수한다 |
| [i18n](./foundations/i18n.md) | 다국어 — 문자열 키, 확장률, ICU 복수형, 날짜·숫자·통화, 한↔영 용어 대응 |
| [토큰 export](./foundations/DDS_tokens_w3c.json) | W3C Design Tokens 형식. Primitive 참조 구조 적용, 기계 판독용 SSOT |
| [빌드 산출물](./dist/) | JSON에서 값이 **해석된** `tokens.css`·`tokens.resolved.json`·Tailwind preset. 컬러 hex/px가 실제로 채워진 드롭인 파일 (`python3 scripts/build_tokens.py`로 재생성) |

### Components

| 카테고리 | 문서 |
|----------|------|
| Actions | [Button](./components/button.md) (Icon Button · Button Stack 포함) |
| Form Inputs | [Input](./components/input.md) · [Switch](./components/switch.md) · [Checkbox](./components/checkbox.md) · [Option Group](./components/option-group.md) |
| Feedback & Overlay | [Tooltip](./components/tooltip.md) · [Skeleton](./components/skeleton.md) · [Feedback & Status](./components/feedback.md) (Toast·Alert·Spinner·Progress·Empty) · [Overlay](./components/overlay.md) (Modal·Sheet·Drawer·Popover·Menu) |
| Navigation | [Navigation](./components/navigation.md) (Tabs · Segmented Control · Breadcrumb) |
| Data Display | [Table](./components/table.md) |
| Layout | [Page Header](./components/page-header.md) |
| Foundation | [Icon System](./components/icons.md) |

📋 전체 카탈로그 및 `componentKey` 인덱스 → [components/README.md](./components/README.md)

### Guides

| 문서 | 내용 |
|------|------|
| [비개발자 선적용 가이드](./guides/non-developer-guide.md) | 기획자·디자이너·PM용 — 컴포넌트 선택 기준 · 토큰/아이콘 규칙 · 문구 템플릿 · 자가 체크리스트 |

---

## 🎯 디자인 철학

DDS는 **3-레이어 토큰 아키텍처**를 갖는다.

```
Primitive  →  Semantic   →  Component
(원시 값)     (의미 매핑)    (변형/상태)
```

- **Primitive**: 컬러 램프(50–900), 원시 수치. **직접 참조 금지**.
- **Semantic**: 의미 기반 토큰 (`Color/bg/primary`, `spacing/16`). 모든 UI는 여기를 거친다.
- **Component**: 컴포넌트의 변형(Variant)·상태(State) 정의.

---

## 🔧 코드 매핑 핵심 규칙

1. **컬러는 hex 인라인 금지** → Semantic 토큰만 사용
2. **간격은 `spacing/*` 토큰만**, 임의 px 금지
3. **모서리는 `border/radius/*` 토큰만**
4. **타이포는 Text Style** (`Heading/lg`, `body/md/regular`)을 클래스/유틸로 매핑
5. **상태는 표준 셀렉터** (`:hover`, `:focus-visible`, `:disabled`, `[data-state]`)
6. **모션은 항상** `prefers-reduced-motion` 미디어쿼리 포함
7. **컴포넌트는 라이브러리 인스턴스 = 코드 컴포넌트 1:1**
8. **UI 문자열 하드코딩 금지** → i18n 키로 출력, 문안은 [writing.md](./foundations/writing.md) 패턴 준수

---

## 🤖 LLM 에이전트 변환 워크플로우

Figma → 코드 변환 시 다음 순서를 따른다.

```
1. 컴포넌트 식별   — 인스턴스 이름 → 컴포넌트 카탈로그 매핑
2. 변형 매핑       — Variant props → React/Vue props
3. 토큰 추출       — Figma 변수 → Semantic 토큰명
4. 상태 정의       — foundations/state.md 기준 셀렉터 작성
5. 타이포 적용     — Text Style 이름 → 클래스 매핑
6. 모션 적용       — foundations/motion.md §9 우선순위 따르기
7. 문구 작성       — foundations/writing.md §10 · i18n.md §11 우선순위 따르기
8. 검증           — 임의 px/hex·하드코딩 문자열 잔존 여부 확인
```

### Figma MCP 호출 매핑

| 작업 | MCP 도구 |
|------|----------|
| 페이지 구조 파악 | `get_metadata` |
| 변수 값 추출 | `get_variable_defs` (노드 선택 필요) |
| 토큰/컴포넌트 검색 | `search_design_system` |
| 코드 생성 컨텍스트 | `get_design_context` |

---

## 🚫 디자인 금지 규칙 (Anti-patterns)

DDS 산출물은 **절제되고 신뢰감 있는 톤**을 유지한다. 아래는 예외 없이 금지.

1. **이모지 아이콘 금지** — `₩ 🛒 👤 📦 ⏱ ✅ ⚠️ 🔔` 등 이모지·기호를 아이콘 자리에 쓰지 않는다.
   모든 아이콘은 **라인(아웃라인) SVG 한 세트**(`stroke="currentColor"`)로 통일. → [components/icons.md §0](./components/icons.md)
2. **"AI스러운" 그라데이션 띠/배너 UI 지양** — 화면 상단을 가로지르는 브랜드 그라데이션 히어로 띠, 보라↔핑크 글로우 그라데이션, 네온 테두리, 무의미한 글래스모피즘 등 **장식적 그라데이션·배너**를 남발하지 않는다.
   - 면은 기본적으로 **단색 surface**(`Color/bg/*`)와 **연한 틴트**(`*-subtle`)로 구성.
   - 그라데이션은 차트·데이터 시각화 등 **기능적 목적**이 있을 때만 제한적으로.
3. **맹목적 고밀도 지양** — 정보를 욱여넣는 초고밀도(compact) 레이아웃을 기본으로 삼지 않는다.
   여백·정렬·위계로 **읽기 쉬운 밀도**를 우선하고, 고밀도는 데이터 그리드 등 꼭 필요한 화면에 한정.
4. **컬러는 다채롭되 조화롭게** — accent·chart 팔레트로 **다양성**은 살리되, 한 화면의 강조색은 절제하고
   브랜드 green은 주요 액션 전용으로 보존한다. 채도 높은 색의 대면적 사용·무지개식 남발 금지.

---

## 📦 소스 메타

| 항목 | 값 |
|------|----|
| Figma 파일 | `2026_DDS_v2_배포용` |
| File Key | `tDGeNJRNR2vCZu5bVdmoNc` |
| 라이브러리 키 | `lk-c82741c9eb3cfc2addd0404224304df5d65a7036ad1f38eeac26f7e660286d91e1723437ace74f6d2a826e6755a0744aa5d72288b5a47a47ff789573d602ab7c` |
| 페이지 ID | `5001:88244` (DDS ver.2.0) |
| 폰트 | Pretendard |
| 모드 | Light · Dark (`[data-theme="dark"]` / OS 자동) |

🔗 [Figma 파일 열기](https://www.figma.com/design/tDGeNJRNR2vCZu5bVdmoNc/2026_DDS_v2_%EB%B0%B0%ED%8F%AC%EC%9A%A9)

---

## 🗺 로드맵

### 완료 (v2.0 ~ v2.4) — 단어장 층

- ✅ **토큰 빌드 파이프라인** — `scripts/build_tokens.py`가 JSON을 해석해 `dist/`(tokens.css·resolved.json·Tailwind preset) 생성 (경량 Style Dictionary)
- ✅ **다크 모드** — semantic 다크 토큰 + `[data-theme="dark"]`·자동(`prefers-color-scheme`) 지원 ([foundations/colors.md § 다크 모드](./foundations/colors.md#-다크-모드))
- ✅ **Foundations 확장** — Layout([layout.md](./foundations/layout.md))·Elevation([elevation.md](./foundations/elevation.md))·Accent/Chart 컬러·타이포 굵기 축
- ✅ **UX 라이팅 가이드** — 문구 규칙([writing.md](./foundations/writing.md)) + 한/영 다국어([i18n.md](./foundations/i18n.md))
- ✅ **내비게이션 컴포넌트** — [navigation.md](./components/navigation.md) (Tabs·Segmented·Breadcrumb). 사양 정의 완료, **Figma 게시 및 componentKey 발급은 대기 중**
- ✅ **거버넌스 1단계** — 하드코딩 검사 CI(hex·rgb·간격 px·이모지 — `scripts/check_hardcoding.py`) + 토큰 빌드 검증(`.github/workflows/validate.yml`). 정당한 예외는 해당 줄 `dds-allow: <이유>` 주석

### v2.5 — 문법 단계 (2026-09 ~)

> 토큰·사양("단어장")은 갖춰졌다. 이제 AI와 신규 구성원이 **"이 화면에 이걸 써도 되나"** 를 문서만으로 판단할 수 있도록
> 사용 규칙("문법")·제품 문맥·교정 기록을 채운다. 형식(JSON·MD)이나 도구를 더 얹는 일이 아니라 **빠져 있는 판단을 밖으로 꺼내 적는 일**이다.
> 기준선은 [navigation.md](./components/navigation.md) — 선택 기준 표 · 오버플로 규칙 · 배치 규칙을 갖춘 유일한 컴포넌트 문서.

| 순서 | 항목 | 내용 | 산출물 |
|---|---|---|---|
| 1 | ✅ **제품 문맥 선언** — 확정. 기준 화면(ITSM 실서비스)만 `[미확인]`, AB 실험 중 선정 | DDS가 어떤 제품(사내 B2B 운영 도구)·어떤 사용자(장시간 상주)·어떤 업무를 위한 시스템인지, "우리 화면답다"의 정의, 기준 화면 2~3개 링크 | design.md 상단 § |
| 2 | 🔜 **AI 사용 빈칸 기록** | AB 실험(`metrics/AB실험_설계서.md` §6 부산물 기록 — 로컬 전용, 저장소 미포함) 조건 B에서 AI가 DDS를 잘못 쓰거나 문서가 침묵한 지점을 화면별로 기록. **실험 중엔 기록만, 문서 반영은 4본 종료 후** | `metrics/cases/<화면>/gaps.md` |
| 3 | 🔜 **컴포넌트 문법 보강** | 선택 기준(대안 컴포넌트와의 구분) · 기본값 명시 · 라벨 글자 수·말줄임 · 로딩 시 표시 · 원칙의 예외 케이스. **Button → Input → Overlay → Table** 순 (B2B 화면 출현 빈도순) | `components/*.md` |
| 4 | 🔜 **페이지 패턴** | 목록 · 상세 · 폼(등록/수정) · 대시보드 4종. 컴포넌트 배치 · primary 위치 · 필터 위치 · 빈/로딩 상태. [examples/writing.html](./examples/writing.html)(거래처 관리)에서 목록+폼 패턴을 먼저 추출 | `patterns/` (신설) |
| 5 | 🔜 **Figma 부채 정리** | 상태색 WCAG 매핑 Figma 변수 반영 · Navigation 3종 게시 및 componentKey 발급 · `font_family` 플레이스홀더 정리 | Figma + [components/README.md](./components/README.md) |

### 이후 — 도구·형식 층

- 🔜 **거버넌스 2단계** — stylelint(에디터 단계) · i18n 키 검증
- 🔜 **Code Connect** — Figma ↔ React/Vue 1:1 매핑

> 형식·도구는 사용 규칙이 모호한 상태를 바꾸지 못한다 — 기계가 읽기 좋은 형식으로 정갈하게 모호해질 뿐이다. v2.5 문법 단계가 채워진 뒤로 미룬다.

---

## ⚠️ 알려진 이슈

- ~~`Brand/Secondary/netural`의 `netural` 오타 유지~~ → **v2.0에서 `neutral`로 정정 완료.** Figma 변수 및 토큰 JSON 모두 반영됨. 함께 `transpaernt`→`transparent`, `Interctive`→`Interactive` 오타도 정정.
- `primary_typography`의 `font_family`·`font_family_typeface` 토큰 값이 `"String value"` 플레이스홀더 상태. 실사용 토큰(`font_family_typeface_sans` 등)은 정상이므로, Figma에서 두 토큰에 실제 값을 채우거나 미사용 시 삭제 필요.
- ~~상태색 `text/*`·`icon/*`이 면과 같은 500 단계를 참조해 대비 미달(warning 1.99:1, success 2.5:1). `bg/disabled`와 `text/disabled`가 같은 값이라 비활성 글자가 안 보임~~ → **정정 완료.** 글자·아이콘은 700~800, disabled는 면/글자를 분리. → [colors.md §2.2.1](./foundations/colors.md)
  - **Figma 변수도 같은 매핑으로 갱신해야 한다.** 현재는 저장소 JSON에만 반영된 상태.
- **베트남어 지원이 [i18n.md](./foundations/i18n.md)에 미반영.** 현재 문서는 한↔영만 다룬다. 베트남어는 성조 부호(diacritics)로 글자 높이가 커지고 확장률이 영어와 다르므로 ① 확장률 표 추가 ② Pretendard의 베트남어 글리프 커버리지 확인(미지원 시 폴백 폰트 지정) ③ 용어 대응표 확장이 필요하다.
- 토큰 값은 W3C Design Tokens 형식 export 파일(`./foundations/DDS_tokens_w3c.json`)에서 확인 가능. `get_variable_defs`는 노드 선택이 필요해 MCP 경유로는 일부 토큰만 수집되므로, 전체 토큰은 export 파일을 기준으로 함.

---

*최종 갱신: 2026-08-14 · 거버넌스 1단계(하드코딩 검사 CI·토큰 빌드 검증) · 상태색 WCAG AA 대비 정정*
