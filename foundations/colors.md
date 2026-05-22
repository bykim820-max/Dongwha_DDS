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
| `neutral`* | white, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900 | `Brand/Secondary/netural/{scale}` |

> Figma 라이브러리에 등록된 다른 hue(`blue`, `green`, `orange`, `yellow`, `purple` 등)도 동일한 50–900 패턴을 따른다.

### 1.2 브랜드 컬러

| 토큰 | 용도 |
|------|------|
| `Brand/Primary/navy` | 동화 브랜드 메인 |
| `Brand/Primary/black` | 본문/강조 |
| `Brand/Secondary/netural/white` | 베이스 배경 |
| `brand primary` | 레거시 호환 별칭 (`Colors` 컬렉션) |

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

## ⚠️ 주의 사항

- `Brand/Secondary/netural`의 `netural`은 Figma 측 **오타**이지만 코드 일관성을 위해 그대로 유지.
- 정확한 hex 값은 Figma 변수 패널에서 직접 확인 (Figma MCP `get_variable_defs`는 노드 선택 필요).
- 다크 모드 토큰은 Phase 2(2026 7월~)에 추가 예정.
- 컬러만으로 정보를 전달하지 말 것 (색맹 대응) — 아이콘·텍스트 병행.
