# Layout

> 화면 구성의 규율. **여백·그리드·리듬**으로 정렬을 잡는다.
> 절제된 구성의 핵심은 색이 아니라 **일관된 레이아웃 규칙**이다.

[← design.md](../design.md)

> **기본 형식 = 대시보드(와이드)**. 콘텐츠는 `--container-dashboard`(1680px)까지 가득 채우고 가운데 고정한다.
> 모바일 레이아웃(단일 컬럼·접힘)은 **모바일 breakpoint 이하에서만** 적용한다. → [§5](#5-breakpoint-반응형)

---

## 1. 원칙

| 원칙 | 의미 |
|------|------|
| **여백은 도구** | 박스·구분선보다 **여백으로 그룹핑**. 관련 있으면 가깝게, 다르면 멀게 |
| **수직 리듬** | 섹션/블록/스택 3단계 간격 토큰으로 일관된 흐름 |
| **그리드 정렬** | 모든 요소는 8pt 그리드 + 12컬럼 위에. 임의 위치 금지 |
| **하나의 초점** | 화면당 primary 액션 1개. 복잡하면 단계·시트로 분할 |
| **컨텐츠 최대폭** | 본문은 너무 넓지 않게(가독 폭 유지), 데이터는 넓게 |

---

## 2. 간격 리듬 (3단계)

레이아웃 간격은 **의미 토큰 3개**로 통일한다. 임의 px·산발적 spacing 금지.

| 토큰 | 값 | 용도 |
|------|----|------|
| `--layout-section-gap` | `--space-64` (64) | **섹션 사이** (페이지 내 큰 묶음) |
| `--layout-block-gap` | `--space-24` (24) | **블록(카드) 사이** |
| `--layout-stack-gap` | `--space-12` (12) | **한 덩어리 내부** (라벨↔값, 아이콘↔텍스트) |

```css
.page    { display: flex; flex-direction: column; gap: var(--layout-section-gap); }
.section { display: flex; flex-direction: column; gap: var(--layout-block-gap); }
.stack   { display: flex; flex-direction: column; gap: var(--layout-stack-gap); }
```

> 비결: **섹션 간격을 과감히 크게(64+)**, 내부는 촘촘히. 큰 여백 ↔ 작은 여백의 대비가 위계를 만든다.

---

## 3. Container (최대폭)

콘텐츠는 **container 최대폭** 안에서 가운데 고정 정렬.

| 토큰 | px | 용도 |
|------|----|------|
| `--container-dashboard` | **1680** | **대시보드 기본** — 이 폭까지 가득 채우고 고정 |
| `--container-2xl` | 1680 | 와이드 (= dashboard) |
| `--container-xl` | 1200 | 좁은 콘텐츠 페이지 |
| `--container-lg` | 1024 | 일반 콘텐츠 |
| `--container-md` | 768 | 단일 컬럼 |
| `--container-prose` | 680 | 읽기 본문·폼 (한 줄 가독 폭) |
| `--container-sm` | 640 | 좁은 폼·모달 |

```css
/* 대시보드: 1680까지 가득 + 가운데 고정 */
.container { max-width: var(--container-dashboard); margin-inline: auto; padding-inline: var(--grid-margin); }
```

> 대시보드 화면은 1680px까지 폭을 **가득 채워** 데이터 밀도를 살리고, 그 이상 넓은 모니터에서는 가운데 고정한다.

---

## 3.1 Topbar (앱 상단 헤더)

화면 최상단에 고정되는 전역 헤더. 레거시 용어로는 **GNB**에 해당한다.
(페이지 안쪽 제목 영역은 Topbar가 아니라 → [Page Header](../components/page-header.md))

| 항목 | 데스크톱 (≥ md) | 모바일 (< md) |
|------|----------------|---------------|
| **높이** | `--topbar-h` = **56px** | **40px** (`--topbar-h-mobile`, 자동 전환) |
| **축약형** | `--topbar-h-compact` = 46px — 메뉴를 아이콘 하나로 접었을 때 | — |
| **좌우 패딩** | `--grid-margin` (`spacing/24`) | `spacing/16` |
| **아이콘** | `lg`(24) | `md`(20) |
| **폭** | 뷰포트 full-width. 내부 콘텐츠만 `--container-dashboard`로 제한 | full-width |
| **깊이** | 스크롤 시 `--elevation-sticky` | 동일 |

```css
:root { /* dist/tokens.css 제공 */ }

.topbar {
  position: sticky; top: 0; z-index: 100;
  height: var(--topbar-h);                    /* md 미만에서 40px로 자동 전환 */
  padding-inline: var(--grid-margin);
  background: var(--color-bg-primary);        /* 반투명 금지 */
  border-bottom: 1px solid var(--color-border-secondary);
}
.topbar[data-scrolled="true"] { box-shadow: var(--elevation-sticky); }

@media (max-width: 767px) {
  .topbar { padding-inline: var(--space-16); }
}
```

> **`--topbar-h`는 단일 참조점이다.** SNB·드로어·스티키 요소는 헤더 높이를 직접 쓰지 말고
> 항상 `var(--topbar-h)`를 참조한다. 값은 브레이크포인트에서 자동으로 바뀐다.

값의 출처는 레거시 `동화디자인시스템_배포용`의 헤더 규격(PC 56 / 축약 46 / 모바일 40)이다.
좌우 패딩만 레거시 30px → DDS **8pt 그리드에 맞춰 24px**로 정규화했다.

---

## 3.2 App Shell · SNB (사이드 내비게이션)

대시보드형 화면의 기본 골격은 **좌측 SNB + 콘텐츠** 2분할이다.

| 항목 | 규칙 |
|------|------|
| **위치** | SNB는 **항상 뷰포트 맨 좌측에 고정**(`left:0`, flush-left). 앱 셸은 전체 폭으로 펴서 SNB 칼럼이 화면 왼쪽 끝에 붙게 한다 |
| **폭** | `--snb-width` = **270px (권장)**. 접힘 상태는 `--snb-width-collapsed`(72px, 아이콘만) |
| **콘텐츠** | SNB 우측 영역(`1fr`) 안에서 컨테이너를 `--container-dashboard`(1680)까지 두고 **가운데 정렬**. 1680 초과분은 좌우 여백 |
| **모바일** | `md`(768) 미만에서 SNB **숨김** → 햄버거/드로어로 전환 |

```css
/* 셸은 전체 폭 → SNB 칼럼이 항상 left:0 */
.app-shell { display: grid; grid-template-columns: var(--snb-width) 1fr; }
.app-shell > .snb { position: sticky; top: var(--topbar-h); align-self: start; }  /* 좌측 0 고정 */
/* 콘텐츠는 SNB 우측 영역 안에서 가운데 정렬 */
.app-shell > .content { max-width: var(--container-dashboard); margin-inline: auto; }

@media (max-width: 767px) {
  .app-shell { grid-template-columns: 1fr; }   /* SNB 숨김, 드로어로 */
  .app-shell > .snb { display: none; }
}
```

> Top Nav만 쓰는 단순 화면은 SNB 없이 container만으로 구성. SNB가 있으면 **반드시 좌측 270px**.

---

## 4. Grid (12컬럼)

| 토큰 | 값 |
|------|----|
| `--grid-columns` | 12 |
| `--grid-gutter` | `--space-24` (컬럼 사이) |
| `--grid-margin` | `--space-24` (좌우 여백) |

```css
.grid { display: grid; grid-template-columns: repeat(var(--grid-columns), 1fr); gap: var(--grid-gutter); }
.col-6 { grid-column: span 6; }   /* 1/2 */
.col-4 { grid-column: span 4; }   /* 1/3 */
.col-3 { grid-column: span 3; }   /* 1/4 */
```

> 카드 그리드는 `repeat(auto-fill, minmax(280px, 1fr))` + `gap: var(--grid-gutter)` 패턴 권장 (반응형 모듈).

---

## 5. Breakpoint (반응형)

| 토큰 | px | 기준 |
|------|----|------|
| `--breakpoint-sm` | 640 | 큰 모바일 |
| `--breakpoint-md` | 768 | 태블릿 |
| `--breakpoint-lg` | 1024 | 데스크톱 |
| `--breakpoint-xl` | 1280 | 와이드 |

> CSS `@media`는 `var()`를 못 쓰므로 값 자체를 사용하되, **이 토큰 값과 일치**시킨다. JS·문서에서는 `--breakpoint-*` 참조.

**원칙: 대시보드(와이드)가 기본, 모바일 레이아웃은 모바일 breakpoint 이하에서만.**
데스크톱에서는 1680px까지 가득 찬 멀티컬럼 대시보드를, `md`(768px) **미만**에서만 단일 컬럼·접힘(사이드바 숨김 등) 모바일 형식으로 전환한다.

```css
/* 기본 = 와이드 대시보드 */
.container { max-width: var(--container-dashboard); margin-inline: auto; }
.dash { display: grid; grid-template-columns: 240px 1fr; gap: var(--grid-gutter); }  /* 사이드바 + 콘텐츠 */
.kpis { display: grid; grid-template-columns: repeat(6, 1fr); gap: var(--grid-gutter); }

/* 모바일에서만 단일 컬럼으로 접힘 */
@media (max-width: 767px) {
  .dash { grid-template-columns: 1fr; }
  .dash > .sidebar { display: none; }
  .kpis { grid-template-columns: repeat(2, 1fr); }
}
```

---

## 6. 터치 타깃 · 정렬

- 모든 인터랙티브 요소 최소 **44×44px** 히트 영역 (작은 아이콘도 패딩으로 확보)
- 시각 정렬은 **광학 정렬** 우선 (아이콘·숫자는 보이는 중심 기준)
- 같은 위계의 요소는 같은 정렬선 공유

---

## 7. Do / Don't

✅ **DO**
- 섹션/블록/스택 3단계 간격 토큰만 사용
- container로 최대폭 제한 + 가운데 정렬
- 큰 여백 ↔ 작은 여백 대비로 위계 표현
- 모바일 우선 반응형

❌ **DON'T**
- 화면 가장자리에 콘텐츠 꽉 채우기 (여백 0)
- 임의 margin/padding 산발적 사용
- 한 화면에 primary 액션 여러 개
- 박스·구분선 남발 (여백으로 충분한데 선으로 가둠)

---

## 8. Tokens 요약

| 영역 | 토큰 |
|------|------|
| 간격 리듬 | `--layout-{section,block,stack}-gap` |
| 최대폭 | `--container-dashboard`(1680, 기본) · `--container-{2xl,xl,lg,md,prose,sm}` |
| 그리드 | `--grid-{columns,gutter,margin}` |
| Topbar(상단 헤더) | `--topbar-h`(56 → md 미만 40 자동) · `--topbar-h-compact`(46) · `--topbar-h-mobile`(40) |
| SNB(사이드 내비) | `--snb-width`(270, 좌측) · `--snb-width-collapsed`(72) |
| 반응형 | `--breakpoint-{sm,md,lg,xl}` |
| 깊이 | → [elevation.md](./elevation.md) |
