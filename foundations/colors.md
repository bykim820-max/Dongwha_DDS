# Colors

> 3-레이어 컬러 시스템: **Primitive → Semantic → Component**.
> 모든 UI는 **Semantic 토큰만** 참조한다. Primitive 직접 사용 금지.

[← design.md](../design.md)

---

## 1. Primitive Colors

`Primitive:Colors` 컬렉션. 코드 매핑 시 절대 직접 사용하지 말고 Semantic 토큰을 거친다.

### 1.1 컬러 램프 (50–900 스케일)

각 hue별 50, 100, 200, 300, 400, 500, 600, 700, 800, 900 스케일을 갖는다.

| hue | 확인된 스케일 | 토큰 패턴 |
|-----|--------------|-----------|
| `red` | 50, 100, 200, 400, 500, 600, 700, 800, 900 | `Primitive/red/{scale}` |
| `pink` | 50, 100, 200, 400, 600, 700 | `Primitive/pink/{scale}` |
| `neutral`* | white, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900 | `Brand/Secondary/neutral/{scale}` |

> Figma 라이브러리에 등록된 다른 hue(`blue`, `green`, `orange`, `yellow`, `purple` 등)도 동일한 50–900 패턴을 따른다.

### 1.2 브랜드 컬러

| 토큰 | 실제 값 (SSOT) | 용도 |
|------|---------------|------|
| `Brand/Primary/green` | `#00ad50` (ramp 500 = `#14bc62`) | **동화 브랜드 메인** |
| `Brand/Primary/navy` | `#1d3c6a` | 보조 강조 (메인 아님) |
| `Brand/Primary/black` | `#262626` | 본문/강조 |
| `Brand/Secondary/neutral/white` | `#ffffff` | 베이스 배경 |
| `brand primary` | — | 레거시 호환 별칭 (`Colors` 컬렉션) |

> ⚠️ **v2.0 정정**: 이전 문서는 브랜드 메인을 `Brand/Primary/navy`로 기재했으나
> 이는 오류다. 동화 브랜드 메인은 **green 계열**이며, JSON SSOT의 모든
> `*_interactive_primary` 토큰이 `brand_primary_green_500`을 참조한다.
> navy는 보조 강조용으로만 사용한다.

### 1.3 인터랙티브(브랜드 메인) 적용 토큰

메인 액션·선택 상태에 쓰는 green 인터랙티브 토큰. **상태별 ramp가 이미 정의돼 있으니 직접 hex 대신 이 토큰을 쓴다.**

| Semantic 토큰 | 참조 Primitive | hex |
|---------------|----------------|-----|
| `Color/bg/interactive/primary` | green 500 | `#14bc62` |
| `Color/bg/interactive/primary_hover` | green 700 | `#0c8048` |
| `Color/bg/interactive/primary_pressed` | green 800 | `#0a6036` |

> `text/interactive/primary`, `icon/interactive/primary`, `border/interactive/primary`도
> 동일한 green 500/700/800 체계를 따른다(4 roles × 3 states).

---

## 2. Semantic Colors

`Semantic: Colors` 컬렉션. **모든 UI 컬러는 이 토큰만 사용**.

### 2.1 네이밍 규칙

```
Color/<role>/<intent>
```

- `role`: `bg` (배경) · `text` (글자) · `icon` (아이콘) · `border` (테두리)
- `intent`: `primary` · `secondary` · `tertiary` · `info` · `success` · `warning` · `danger` · `disabled`

총 **32개 슬롯** (4 roles × 8 intents).

### 2.2 토큰 매트릭스

| role \ intent | primary | secondary | tertiary | info | success | warning | danger | disabled |
|---------------|---------|-----------|----------|------|---------|---------|--------|----------|
| **bg** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **text** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **icon** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **border** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

코드 매핑 예: `Color/bg/danger` ↔ CSS `--color-bg-danger`.

### 2.2.1 상태색: 면과 글자는 다른 ramp를 쓴다

같은 intent라도 **면(`bg`)은 선명한 500, 글자·아이콘(`text`/`icon`)은 어두운 700~800**을 참조한다.
면과 글자에 같은 단계를 쓰면 흰 배경·`*-subtle` 면에서 대비가 무너지기 때문이다.

| intent | `bg/*` (면) | `text/*` · `icon/*` (글자·아이콘) | 흰 배경 대비 | `*-subtle` 대비 |
|--------|------------|----------------------------------|-------------|----------------|
| info | blue 500 `#196ce8` | **blue 700 `#0f4aa8`** | 8.19:1 | 7.52:1 |
| success | green 500 `#14bc62` | **green 700 `#0c8048`** | 5.0:1 | 4.59:1 |
| warning | yellow 600 `#e0b20f` | **yellow 800 `#806108`** | 5.78:1 | 5.49:1 |
| danger | red 500 `#f51a1a` | **red 700 `#a71010`** | 7.71:1 | 6.78:1 |

- 기준: 본문 텍스트 **AA 4.5:1**, 아이콘 등 비텍스트 **3:1**
- `icon/*`은 `text/*`와 **같은 단계**를 쓴다. 알럿 안에서 아이콘과 문구의 색이 어긋나지 않게 하기 위함
- 다크 테마는 반대로 **400 단계**(밝은 쪽)를 써서 어두운 면 위 대비를 확보한다 → [§ 다크 모드](#-다크-모드)

> ⚠️ **노란색은 두 단계 내려야 한다.** yellow 700(`#b3890b`)은 흰 배경에서 3.23:1로
> 본문 기준에 미달한다. warning만 800을 쓰는 이유다.

### 2.2.2 disabled: 면과 글자를 반드시 다른 값으로

`bg/disabled`와 `text/disabled`가 같은 primitive를 참조하면 비활성 요소의 글자가 사라진다.

| 테마 | `bg/disabled` | `text/disabled` | 대비 |
|------|--------------|-----------------|------|
| Light | neutral 200 `#e5e5e5` | neutral 500 `#737373` | 3.76:1 |
| Dark | neutral 700 `#404040` | neutral 400 `#a3a3a3` | 4.11:1 |

### 2.3 Figma 스코프

| Figma 스코프 | 가이드 |
|--------------|--------|
| `ALL_FILLS` | `bg/*` 토큰 |
| `TEXT_FILL` | `text/*` 토큰 |
| `SHAPE_FILL` | `icon/*` 토큰 |
| `STROKE` | `border/*` 토큰 |

---

## 3. CSS Variables 매핑

```css
:root {
  /* Backgrounds */
  --color-bg-primary:   /* Color/bg/primary */;
  --color-bg-secondary: /* Color/bg/secondary */;
  --color-bg-tertiary:  /* Color/bg/tertiary */;
  --color-bg-info:      /* Color/bg/info */;
  --color-bg-success:   /* Color/bg/success */;
  --color-bg-warning:   /* Color/bg/warning */;
  --color-bg-danger:    /* Color/bg/danger */;
  --color-bg-disabled:  /* Color/bg/disabled */;

  /* Text */
  --color-text-primary:   /* Color/text/primary */;
  --color-text-secondary: /* Color/text/secondary */;
  --color-text-tertiary:  /* Color/text/tertiary */;
  --color-text-info:      /* Color/text/info */;
  --color-text-success:   /* Color/text/success */;
  --color-text-warning:   /* Color/text/warning */;
  --color-text-danger:    /* Color/text/danger */;
  --color-text-disabled:  /* Color/text/disabled */;

  /* Icons */
  --color-icon-primary:   /* Color/icon/primary */;
  --color-icon-info:      /* Color/icon/info */;
  --color-icon-danger:    /* Color/icon/danger */;
  /* ... */

  /* Borders */
  --color-border-primary: /* Color/border/primary */;
  --color-border-info:    /* Color/border/info */;
  --color-border-danger:  /* Color/border/danger */;
  /* ... */
}
```

---

## 4. Tailwind 매핑

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        bg: {
          primary:   'var(--color-bg-primary)',
          secondary: 'var(--color-bg-secondary)',
          tertiary:  'var(--color-bg-tertiary)',
          info:      'var(--color-bg-info)',
          success:   'var(--color-bg-success)',
          warning:   'var(--color-bg-warning)',
          danger:    'var(--color-bg-danger)',
          disabled:  'var(--color-bg-disabled)',
        },
        text:   { primary: 'var(--color-text-primary)', /* … */ },
        icon:   { primary: 'var(--color-icon-primary)', /* … */ },
        border: { info:    'var(--color-border-info)',  /* … */ },
      },
    },
  },
}
```

---

## 5. 적용 가이드

| 상황 | 권장 토큰 |
|------|-----------|
| 메인 액션 버튼 배경 | `Color/bg/primary` |
| 보조 버튼 배경 | `Color/bg/secondary` |
| 본문 텍스트 | `Color/text/primary` |
| 도움말·캡션 텍스트 | `Color/text/tertiary` |
| 에러 메시지 텍스트 | `Color/text/danger` |
| 인풋 포커스 보더 | `Color/border/info` |
| 비활성 버튼 | `Color/bg/disabled` + `Color/text/disabled` |
| 정보 알림 아이콘 | `Color/icon/info` |
| 경고 알림 아이콘 | `Color/icon/warning` |

---

## 🌙 다크 모드

semantic 토큰만 다크 값으로 다시 매핑한다. **primitive(hex 램프)는 그대로**, 컴포넌트 코드는 **수정 없음**(같은 `var(--color-*)`가 테마에 따라 값만 바뀜).

### 적용 방법
```html
<!-- 수동: 루트에 속성 지정 -->
<html data-theme="dark"> … </html>   <!-- 또는 "light" 강제 -->
```
- `[data-theme="dark"]` → 다크 강제
- `[data-theme="light"]` → 라이트 강제
- 속성 미지정 → **OS 설정 따름**(`@media (prefers-color-scheme: dark)`)

값은 `dist/tokens.css`의 `[data-theme="dark"]` 블록에 생성된다(`scripts/build_tokens.py`).
다크 매핑 정의: `foundations/DDS_tokens_dark.json`.

### 매핑 원칙
| 항목 | Light | Dark |
|------|-------|------|
| 페이지 배경 `bg/secondary` | neutral 50 | **neutral 900** (`#171717`) |
| 표면 `bg/primary`(카드) | white | **neutral 800** (`#262626`) |
| inset `bg/tertiary` | neutral 100 | **neutral 700** |
| 본문 `text/primary` | neutral 900 | **neutral 50** |
| 보조 `text/secondary·tertiary` | 700·600 | **300·400** |
| 브랜드 hover | 한 단계 **어둡게**(green 700) | 한 단계 **밝게**(green 400) |
| 상태 텍스트(success·danger…) | 500 | **400 tier**(밝게) |
| subtle 틴트(`*-subtle`) | 50 tier(밝음) | **900 tier**(어두운 틴트) |

> 다크에선 그림자가 약하므로 **표면 밝기 차(900↔800↔700)로 깊이**를 표현한다. → [elevation.md](./elevation.md)
> 대비: 본문/배경 대비 WCAG AA(4.5:1) 이상 유지.

---

## ⚠️ 주의 사항

- `Brand/Secondary/neutral` — 이전 버전의 `netural` 오타는 **v2.0에서 `neutral`로 정정 완료**(Figma 변수 및 `DDS_tokens_w3c.json` 반영). 문서·코드 모두 `neutral`로 통일한다.
- 정확한 hex 값은 Figma 변수 패널에서 직접 확인 (Figma MCP `get_variable_defs`는 노드 선택 필요).
- 다크 모드 토큰은 Phase 2(2026 7월~)에 추가 예정.
- 컬러만으로 정보를 전달하지 말 것 (색맹 대응) — 아이콘·텍스트 병행.
