# Navigation

> 사용자가 **지금 어디에 있고, 어디로 갈 수 있는지**를 알려주는 컴포넌트군.
> 전역 이동(SNB)은 → [foundations/layout.md §3.2](../foundations/layout.md), 페이지 상단 조합은 → [Page Header](./page-header.md).

[← Components](./README.md) · [← design.md](../design.md)

이 문서는 **3개 내비게이션 컴포넌트**를 묶어 다룬다: Tabs · Segmented Control · Breadcrumb.
공통 규칙: **현재 위치를 색만으로 알리지 않는다** — 색 + 굵기 + `aria-current`/`aria-selected` 3중 표시.

---

## 0. Figma 게시 상태

| 컴포넌트 | 타입 | componentKey | 상태 |
|----------|------|--------------|------|
| `Tabs` | component_set | *(미발급)* | **코드 우선 정의** — Figma 미게시 |
| `Segmented Control` | component_set | *(미발급)* | **코드 우선 정의** — Figma 미게시 |
| `Breadcrumb` | component | *(미발급)* | **코드 우선 정의** — Figma 미게시 |

> 이 3종은 v2 라이브러리(`2026_DDS_v2_배포용`)에 아직 없다. 본 문서를 사양서로 Figma에 게시한 뒤
> `componentKey`를 이 표와 [components/README.md](./README.md) 인덱스에 채운다. 키를 임의로 만들지 않는다.

---

## 1. 선택 기준

| 상황 | 컴포넌트 | 시맨틱 | 개수 |
|------|----------|--------|------|
| 같은 층위의 **콘텐츠 패널을 교체** | **Tabs** | `tablist` / `tab` / `tabpanel` | 2~7개 |
| 같은 콘텐츠의 **표시 방식·범위를 전환** | **Segmented Control** | `radiogroup` / `radio` | 2~4개 |
| 현재 페이지의 **계층 경로 표시** | **Breadcrumb** | `nav` + `ol` | 3단계 이하 |
| 앱 **전역 이동** | SNB → [layout.md §3.2](../foundations/layout.md) | `nav` + `ul` | — |

**Tabs와 Segmented의 차이가 핵심이다.**

- **Tabs** = 서로 다른 내용을 담은 패널을 갈아끼운다. (프로필 / 알림 / 보안)
- **Segmented** = 내용은 그대로고 **보는 방식이나 구간만** 바꾼다. (일별 / 주별 / 월별, 카드 / 목록)

Segmented는 성격상 **폼 컨트롤(라디오 그룹)** 에 가깝다. `role="tablist"`를 쓰지 않는다.

---

## 2. Tabs

### 2.1 Anatomy

```
[Tabs]
├── [Tab List]                role="tablist"
│   ├── [Tab]                 role="tab" · aria-selected
│   │   ├── [Leading Icon]    (옵션, 라인 SVG)
│   │   ├── [Label]           (필수)
│   │   └── [Count]           (옵션, 숫자 배지)
│   ├── [Indicator]           (선택 위치 표시)
│   └── [Overflow]            (옵션, 넘칠 때)
└── [Tab Panel]               role="tabpanel"
```

### 2.2 Variants · Size

| Property | 값 | 의미 |
|----------|-----|------|
| `variant` | `underline`(기본) · `pill` | 언더라인 / 알약 배경 |
| `size` | `sm`(36px) · `md`(44px, 기본) | 탭 높이 |
| `align` | `start`(기본) · `stretch` | 좌측 정렬 / 균등 분할(모바일) |
| `overflow` | `scroll`(기본) · `menu` | 가로 스크롤 / `더 보기` 메뉴로 접기 |

- `md`(44px)가 기본 — 터치 타깃 44px을 그대로 만족한다.
- `sm`은 밀도가 높은 데이터 화면에서만. 클릭 영역은 44px로 확장한다.

### 2.3 States

| 상태 | 라벨 | 인디케이터 | 비고 |
|------|------|-----------|------|
| `default` | `Color/text/tertiary` | 없음 | — |
| `hover` | `Color/text/secondary` | 없음 | 배경 `Color/bg/tertiary`(pill만) |
| `selected` | `Color/text/primary` + `font-weight/medium` | 2px, `Color/bg/interactive/primary` | `aria-selected="true"` |
| `focus-visible` | — | — | outline 2px `Color/border/info` |
| `disabled` | `Color/text/disabled` | 없음 | `aria-disabled="true"` |

> **선택 인디케이터에 브랜드 green을 쓰는 이유.**
> [design.md § 금지 규칙 4](../design.md#-디자인-금지-규칙-anti-patterns)는 green을 주요 액션용으로 아껴 쓰라고 하지만,
> [state.md §2](../foundations/state.md)의 `selected` 기본값인 info 파랑을 쓰면 **포커스 링(info)과 구분되지 않는다.**
> 2px 라인은 대면적이 아니므로, 여기서는 **선택 = green / 포커스 = info blue**로 역할을 분리한다.

### 2.4 오버플로

탭 라벨은 번역 시 폭이 늘어난다([i18n.md §3](../foundations/i18n.md)). **줄바꿈으로 도망가지 않는다.**

| 방식 | 동작 | 사용처 |
|------|------|--------|
| `scroll` (기본) | 가로 스크롤 + 좌우 페이드 마스크 | 모바일 · 탭 수 가변 |
| `menu` | 넘치는 탭을 `더 보기` 드롭다운으로 | 데스크톱 고정 레이아웃 |

```css
.tablist { display: flex; overflow-x: auto; scrollbar-width: none; scroll-snap-type: x proximity; }
.tablist::-webkit-scrollbar { display: none; }
.tab { white-space: nowrap; scroll-snap-align: start; }   /* 줄바꿈 금지 */
```

- 선택된 탭은 진입 시 `scrollIntoView({ inline: 'center', block: 'nearest' })`로 보이게 한다.
- 탭이 **8개를 넘으면** Tabs가 아니라 SNB나 Select를 검토한다.

### 2.5 모션

[motion.md §5.10](../foundations/motion.md) 준수.

- 인디케이터는 **X 위치·폭만** 트랜지션 — `duration/base` + `easing/emphasized`
- 패널 콘텐츠는 fade 100ms로 간결히 교체 (슬라이드 금지)
- `prefers-reduced-motion` 시 인디케이터 이동 없이 즉시 전환

```css
.indicator {
  position: absolute; bottom: 0; height: 2px;
  background: var(--color-bg-interactive-primary);
  transition: transform var(--motion-duration-base) var(--motion-easing-emphasized),
              width     var(--motion-duration-base) var(--motion-easing-emphasized);
}
```

### 2.6 A11y · 키보드

| 키 | 동작 |
|----|------|
| `Tab` | 탭 리스트 진입 → **선택된 탭 하나만** 포커스 (roving tabindex) |
| `←` `→` | 이전/다음 탭으로 이동 (양끝에서 순환) |
| `Home` `End` | 첫 / 마지막 탭 |
| `Enter` `Space` | `activation="manual"`일 때 선택 확정 |

- 선택 탭 `tabindex="0"`, 나머지 `tabindex="-1"`
- `<button role="tab" aria-selected aria-controls={panelId} id={tabId}>`
- `<div role="tabpanel" aria-labelledby={tabId} tabindex="0">`
- **활성화 방식**: 패널이 가벼우면 `automatic`(화살표 이동 즉시 전환), **데이터를 새로 불러오면 `manual`**(Enter로 확정)
- 탭 전환은 **URL에 반영**한다(쿼리스트링·해시). 새로고침·뒤로가기에서 상태가 살아 있어야 한다

### 2.7 Props

```tsx
type TabsProps = {
  value: string;
  onChange: (value: string) => void;
  variant?: 'underline' | 'pill';
  size?: 'sm' | 'md';
  align?: 'start' | 'stretch';
  overflow?: 'scroll' | 'menu';
  activation?: 'automatic' | 'manual';   // 기본 automatic
  children: React.ReactNode;             // <Tab>
};

type TabProps = {
  value: string;
  icon?: React.ReactNode;
  count?: number;            // 숫자 배지
  disabled?: boolean;
  children: React.ReactNode; // 라벨
};
```

---

## 3. Segmented Control

같은 콘텐츠의 **표시 방식·구간**을 바꾸는 컨트롤. 라디오 그룹이다.

### 3.1 Anatomy · Variants

```
[Segmented]                    role="radiogroup"
├── [Track]                    (연한 배경)
└── [Segment] × 2~4            role="radio" · aria-checked
    ├── [Icon]  (옵션)
    └── [Label]
```

| Property | 값 |
|----------|-----|
| `size` | `sm`(32px) · `md`(40px, 기본) |
| `fullWidth` | bool — 컨테이너 폭에 균등 분할 |
| `options` | 2~4개. **5개 이상이면 Select로 대체** |

### 3.2 Tokens

| 영역 | 토큰 |
|------|------|
| 트랙 배경 | `Color/bg/tertiary` |
| 트랙 패딩 · Radius | `spacing/2` · `border/radius/md` |
| 선택 세그먼트 | `Color/bg/primary` + `shadow/sm` |
| 선택 라벨 | `Color/text/primary` (`font-weight/medium`) |
| 비선택 라벨 | `Color/text/secondary` |
| 모션 | `duration/quick` + `easing/standard` |

선택 표시가 **뉴트럴 흰 면 + 그림자**다. 브랜드색을 쓰지 않아 화면당 여러 개를 놓아도 시끄럽지 않다.

```css
.seg { display: inline-flex; padding: var(--space-2); gap: var(--space-2);
       background: var(--color-bg-tertiary); border-radius: var(--radius-md); }
.seg button { height: 40px; padding: 0 var(--space-12); border: 0; background: transparent;
       border-radius: var(--radius-sm); color: var(--color-text-secondary);
       font-weight: var(--font-weight-medium);
       transition: background-color var(--motion-duration-quick) var(--motion-easing-standard); }
.seg button[aria-checked="true"] { background: var(--color-bg-primary);
       color: var(--color-text-primary); box-shadow: var(--shadow-sm); }
.seg button:focus-visible { outline: 2px solid var(--color-border-info); outline-offset: 2px; }
```

> 실제 구현 예: [examples/writing.html](../examples/writing.html)의 언어 토글이 이 사양을 그대로 따른다.

### 3.3 A11y · 키보드

| 키 | 동작 |
|----|------|
| `Tab` | 그룹 진입 → 선택된 세그먼트에 포커스 |
| `←` `→` | 이동 **+ 즉시 선택** (라디오 그룹 관례) |

- `role="radiogroup"` + **`aria-label` 필수** (무엇을 고르는 그룹인지)
- 각 세그먼트 `role="radio"` + `aria-checked`
- 네이티브 `<input type="radio">` + `<label>` 조합도 허용 — 폼 안에서는 이쪽을 권장
- **`role="tablist"`를 쓰지 않는다** — 패널을 바꾸는 게 아니다

### 3.4 Props

```tsx
type SegmentedProps = {
  value: string;
  onChange: (value: string) => void;
  options: { value: string; label: string; icon?: React.ReactNode; disabled?: boolean }[];
  size?: 'sm' | 'md';
  fullWidth?: boolean;
  'aria-label': string;      // 필수
};
```

---

## 4. Breadcrumb

현재 페이지의 계층 경로. **깊은 구조에서만** 쓴다. 2단계 이하면 뒤로가기 버튼으로 충분하다.

### 4.1 Anatomy

```
[Breadcrumb]              <nav aria-label>
└── [List]                <ol>
    ├── [Item]            <li> + <a>
    ├── [Separator]       "/" (aria-hidden)
    └── [Current]         <li> + aria-current="page" (링크 아님)
```

```
홈 / 주문 / 주문번호 #12345
```

### 4.2 규칙

| 항목 | 규칙 |
|------|------|
| 깊이 | **3단계 이하** 권장, 최대 4단계 |
| 마지막 항목 | **링크가 아니다.** `aria-current="page"` + `Color/text/primary` |
| 구분자 | `/` 텍스트, `Color/text/tertiary`, `aria-hidden="true"` |
| 축약 | 4단계 초과 시 **중간을 `…` 메뉴로 접는다** (첫 항목과 마지막 2개는 항상 노출) |
| 잘림 | 항목 라벨은 `max-width` + `ellipsis`, 전체 문구는 `title` 속성 |
| 모바일 | `sm` 미만에서는 Breadcrumb 대신 **뒤로가기 버튼** 하나로 대체 |

구분자를 `/`로 두는 것은 [page-header.md §8](./page-header.md)과 맞춘 것이다. 아이콘 chevron으로 바꾸지 않는다.

### 4.3 Tokens

| 영역 | 토큰 |
|------|------|
| 항목 텍스트 | `Color/text/tertiary` |
| 항목 hover | `Color/text/secondary` + underline |
| 현재 페이지 | `Color/text/primary` (`font-weight/medium`) |
| 구분자 | `Color/text/tertiary` |
| Text Style | `body/sm/regular` |
| 항목 ↔ 구분자 갭 | `spacing/8` |
| Breadcrumb ↔ Title 갭 | `spacing/8` ([page-header.md](./page-header.md)) |

### 4.4 A11y

- `<nav aria-label={t('common.nav.breadcrumb')}>` — **`aria-label`도 번역 대상**이다 ([i18n.md §4](../foundations/i18n.md))
  - ko `탐색 경로` · en `Breadcrumb`
- 순서가 의미를 가지므로 `<ol>` 사용 (`<ul>` 아님)
- 마지막 항목은 `<a>`로 감싸지 않는다 — 자기 자신으로 가는 링크는 혼란만 준다
- 구분자는 CSS `::after` 또는 `aria-hidden="true"` — 스크린리더가 "슬래시"를 읽지 않게 한다

### 4.5 Props

```tsx
type BreadcrumbProps = {
  items: { label: string; href?: string }[];   // 마지막 항목은 href 생략
  maxItems?: number;                            // 기본 4, 초과 시 중간 접기
  'aria-label'?: string;
};
```

`items` 시그니처는 [PageHeader](./page-header.md)의 `breadcrumb` prop과 동일하다.

---

## 5. 문구 규칙

[writing.md](../foundations/writing.md) 적용.

| 요소 | 규칙 | 예 |
|------|------|-----|
| 탭 라벨 | **명사구**, 1~2어절, 마침표 없음 | 프로필 · 알림 · 보안 |
| 세그먼트 라벨 | 더 짧게, 1어절 | 일별 · 주별 · 월별 |
| Breadcrumb 항목 | 해당 페이지의 **Title과 같은 단어** | 주문 목록 → "주문" |
| 개수 배지 | 숫자만. 999 초과는 `999+` | 알림 `12` |

- ❌ 탭 라벨에 동사(“설정하기”) — 동사는 버튼의 것이다
- ❌ 탭 라벨에 “~ 관리”, “~ 페이지” 같은 군더더기
- 라벨은 하드코딩하지 말고 i18n 키로 — 영어 전환 시 폭이 늘어난다 ([i18n.md §3](../foundations/i18n.md))
- 모바일 균등 분할(`stretch`)에서는 라벨이 잘리므로 **1~2어절을 넘기지 않는다** (§7)

---

## 6. 공통 Tokens 요약

| 영역 | 토큰 |
|------|------|
| 선택 인디케이터 (Tabs) | `Color/bg/interactive/primary` 2px |
| 선택 면 (Segmented) | `Color/bg/primary` + `shadow/sm` on `Color/bg/tertiary` |
| 라벨 (기본/선택) | `Color/text/tertiary` → `Color/text/primary` + `font-weight/medium` |
| 하단 경계선 (Tabs) | `Color/border/secondary` 1px |
| Focus | `Color/border/info` outline 2px / offset 2px |
| Radius | `border/radius/md`(Segmented·pill 탭) |
| Text Style | `body/md/medium`(Tabs·Segmented) · `body/sm/regular`(Breadcrumb) |
| 모션 | `duration/base` + `easing/emphasized`(인디케이터) · `duration/quick`(Segmented) |

---

## 7. 반응형 · 모바일

브레이크포인트는 [layout.md §5](../foundations/layout.md) 기준(`sm` 640 · `md` 768 · `lg` 1024 · `xl` 1280).
내비게이션은 전환 기준선을 **`md`(768px) 하나로** 통일한다.

| 컴포넌트 | ≥ 768 (데스크톱 · 태블릿) | < 768 (모바일) |
|----------|--------------------------|----------------|
| **Tabs** | `align="start"`, 넘치면 `overflow="menu"` | 3개 이하 `align="stretch"` · **4개 이상 `overflow="scroll"`** |
| **Segmented** | 자동 폭 | `fullWidth` (균등 분할) |
| **Breadcrumb** | 전체 경로 표시 | **숨기고 뒤로가기 버튼 1개로 대체** |
| **SNB** | 270px 고정 | 숨김 → 햄버거 + 드로어 ([layout.md §3.2](../foundations/layout.md)) |

### 7.1 공통 규칙

1. **터치 타깃 44px** — 모바일 Tabs는 `size="md"`(44px) 고정. `sm`(36px)은 데스크톱 전용
2. **좌우 패딩** — 데스크톱 `spacing/24`, 모바일 `spacing/16`
3. **탭은 어떤 폭에서도 줄바꿈하지 않는다** — 좁아지면 `stretch` → `scroll`로 내려갈 뿐이다
4. **스크롤 탭**은 선택 항목을 자동으로 보이게 하고(`scrollIntoView`) 좌우 페이드 마스크를 준다
5. **모바일 Breadcrumb는 줄이지 말고 없앤다** — 중간을 접어 2~3항목만 남기면 위치를 오해하게 만든다

```css
.tablist { padding-inline: var(--space-24); }

@media (max-width: 767px) {
  .tablist   { padding-inline: var(--space-16); }
  .tab       { min-height: 44px; }        /* size="sm" 금지 */
  .tabs[data-fit="stretch"] .tab { flex: 1; }
  .seg, .seg button { width: 100%; flex: 1; }
  .breadcrumb { display: none; }          /* 뒤로가기 버튼으로 대체 */
}
```

### 7.2 동화 레거시 내비게이션 용어 (GNB · LNB · SNB)

2024 디자인시스템(`동화디자인시스템_배포용`)은 3층 내비게이션 용어를 쓴다. DDS v2와 다음과 같이 대응한다.

| 레거시 | 역할 | DDS v2 대응 | 레거시 실측값 |
|--------|------|-------------|--------------|
| **GNB** | 전역 상단 헤더 | *DDS v2 미정의* — 헤더 컴포넌트 필요 | 높이 PC 56px / 모바일 40px, 좌우 패딩 30 / 16, 아이콘 30 / 24 |
| **LNB** | GNB 하단 메인 메뉴 | **Tabs** 또는 [Page Header](./page-header.md) 서브 내비 | 좌우 패딩 PC 30 / 모바일 16 |
| **SNB** | 좌측 사이드 메뉴 | [layout.md §3.2](../foundations/layout.md) SNB | 폭 236~260px, 좌우 패딩 16 또는 24, 아코디언 펼침 |

> 레거시 LNB 규정은 이미 모바일 전환 방침을 담고 있다 —
> *"화면 너비가 충분하지 않아 메인 메뉴를 표시할 수 없을 때 … 메뉴 버튼과 메뉴 레이어를 사용할 수 있다."*
> DDS v2의 "`md` 미만에서 SNB 숨김 → 드로어"와 같은 방향이므로, 용어만 SNB로 통일하면 된다.

---

## 8. Do / Don't

✅ **DO**
- 콘텐츠 교체는 Tabs, 보기 방식 전환은 Segmented로 **역할을 나눈다**
- 탭 상태를 **URL에 반영**해 새로고침·뒤로가기에서 유지
- 넘치는 탭은 **가로 스크롤 또는 메뉴**로 처리 (줄바꿈 금지)
- 현재 위치를 색 + 굵기 + `aria-selected`/`aria-current` **3중**으로 알린다
- 데이터를 새로 불러오는 탭은 `activation="manual"`

❌ **DON'T**
- Segmented에 `role="tablist"` 사용 — 라디오 그룹이다
- 탭 8개 이상 나열 — SNB나 Select를 검토
- 탭 라벨 줄바꿈 · 두 줄 탭
- Breadcrumb 마지막 항목을 링크로 처리
- 색만으로 선택 상태 표시
- 탭 안에 또 탭 (2단계 중첩) — 정보 구조를 다시 본다

---

## 9. Examples

```tsx
// 1. 기본 Tabs — PageHeader 하단 서브 내비게이션
<PageHeader
  title="설정"
  tabs={
    <Tabs value={tab} onChange={setTab}>
      <Tab value="profile">프로필</Tab>
      <Tab value="notif" count={12}>알림</Tab>
      <Tab value="security">보안</Tab>
      <Tab value="billing">결제</Tab>
    </Tabs>
  }
/>

// 2. 데이터를 불러오는 탭 — 수동 활성화 + URL 반영
<Tabs
  value={searchParams.get('tab') ?? 'summary'}
  onChange={(v) => setSearchParams({ tab: v })}
  activation="manual"
  overflow="menu"
>
  <Tab value="summary">요약</Tab>
  <Tab value="orders">주문 내역</Tab>
  <Tab value="settlement">정산</Tab>
</Tabs>

// 3. 모바일 균등 분할
<Tabs value={tab} onChange={setTab} align="stretch" variant="pill" size="sm">
  <Tab value="all">전체</Tab>
  <Tab value="ongoing">진행 중</Tab>
  <Tab value="done">완료</Tab>
</Tabs>

// 4. Segmented — 같은 데이터의 구간 전환
<Segmented
  aria-label="집계 구간"
  value={range}
  onChange={setRange}
  options={[
    { value: 'day',   label: '일별' },
    { value: 'week',  label: '주별' },
    { value: 'month', label: '월별' },
  ]}
/>

// 5. Segmented — 보기 방식 (아이콘)
<Segmented
  aria-label="보기 방식"
  value={view}
  onChange={setView}
  size="sm"
  options={[
    { value: 'card', label: '카드', icon: <Grid /> },
    { value: 'list', label: '목록', icon: <List /> },
  ]}
/>

// 6. Breadcrumb
<Breadcrumb
  items={[
    { label: '홈',   href: '/' },
    { label: '주문', href: '/orders' },
    { label: '주문번호 #12345' },        // 마지막 = 현재, href 없음
  ]}
/>
```
