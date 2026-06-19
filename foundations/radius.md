# Border Radius

> `Semantic:Appearance` 컬렉션, 스코프 `CORNER_RADIUS`.
> **이 문서의 px 값은 추정치가 아니라 `DDS_tokens_w3c.json`(SSOT) 실측값이다.**

[← design.md](../design.md)

---

## 1. 토큰

| 토큰 | px (SSOT 실측) | 사용처 |
|------|---------------|--------|
| `border/radius/sm` | 2 | Tag, Chip, 작은 인풋, Checkbox |
| `border/radius/md` | 4 | Button, Card, Tooltip, Input |
| `border/radius/lg` | 8 | Modal, Section |
| `border/radius/xl` | 12 | 큰 카드, Hero |
| `border/radius/2xl` | 16 | Container |
| `border/radius/rounded` | 999999 | Pill, Avatar, Switch |

> ⚠️ **v2.0 정정**: 이전 문서는 `sm=4 / md=8 / lg=12 / xl=16 / 2xl=24 / rounded=9999`로
> 적혀 있었으나 이는 일반 컨벤션 추정치였다. 실제 Figma 변수( `DDS_tokens_w3c.json`)는
> 위 표대로 **한 단계씩 더 작다**(`md=4px`). 모든 CSS/Tailwind 매핑을 이 값으로 교체할 것.

### 1.1 관련 토큰 — Border Width (참고)

radius와 함께 자주 쓰이는 보더 두께 토큰. 동일하게 SSOT 실측.

| 토큰 | px |
|------|----|
| `border/width/sm` | 1 |
| `border/width/md` | 2 |
| `border/width/lg` | 4 |

---

## 2. CSS 매핑

```css
:root {
  --radius-sm:      2px;
  --radius-md:      4px;
  --radius-lg:      8px;
  --radius-xl:      12px;
  --radius-2xl:     16px;
  --radius-rounded: 999999px;

  /* 관련: border width */
  --border-width-sm: 1px;
  --border-width-md: 2px;
  --border-width-lg: 4px;
}

.button { border-radius: var(--radius-md); }   /* 4px */
.input  { border-radius: var(--radius-md); }   /* 4px */
.tag    { border-radius: var(--radius-sm); }   /* 2px */
.modal  { border-radius: var(--radius-lg); }   /* 8px */
.avatar { border-radius: var(--radius-rounded); }
```

---

## 3. Tailwind 매핑

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      borderRadius: {
        sm:        'var(--radius-sm)',      // 2px
        md:        'var(--radius-md)',      // 4px
        lg:        'var(--radius-lg)',      // 8px
        xl:        'var(--radius-xl)',      // 12px
        '2xl':     'var(--radius-2xl)',     // 16px
        rounded:   'var(--radius-rounded)', // 999999px
      },
      borderWidth: {
        sm: 'var(--border-width-sm)', // 1px
        md: 'var(--border-width-md)', // 2px
        lg: 'var(--border-width-lg)', // 4px
      },
    },
  },
}
```

---

## 4. 적용 가이드

| 요소 | 권장 토큰 | px |
|------|-----------|----|
| 버튼 | `md` | 4 |
| 인풋 필드 | `md` | 4 |
| Tag · Chip | `sm` | 2 |
| Checkbox 박스 | `sm` | 2 |
| 카드 (일반) | `md` ~ `lg` | 4~8 |
| 카드 (대형/히어로) | `xl` | 12 |
| 모달 · 시트 | `lg` | 8 |
| 컨테이너 · 섹션 | `2xl` (필요 시) | 16 |
| 아바타 | `rounded` | — |
| 필 버튼 (Capsule) | `rounded` | — |
| Switch 트랙/썸 | `rounded` | — |
| 툴팁 | `md` | 4 |
| 이미지 썸네일 | `sm` 또는 `md` | 2~4 |
| 토스트 · 알림 배너 | `md` | 4 |

---

## 5. 규칙

1. **같은 위계의 요소는 같은 radius** (예: 모든 폼 인풋 → `md`)
2. **중첩된 요소는 부모보다 작은 radius**
   - 카드 안의 버튼: 카드 `lg`(8), 버튼 `md`(4)
   - 모달 안의 카드: 모달 `lg`(8), 카드 `md`(4)
3. 임의 px 금지 → 토큰만 사용
4. 한 컴포넌트의 4개 모서리는 동일 값 (예외: 바텀시트 상단만 둥글기 등 디자인 의도 시)
5. 아이콘 전용 버튼은 정사각형이면 `md`, 원형이면 `rounded`

---

## ⚠️ 변경 이력

- **2026-06-15**: 전체 radius 값을 `DDS_tokens_w3c.json` 실측값으로 정정.
  기존 추정치(`md=8px` 등) → 실제값(`md=4px` 등)으로 한 단계씩 하향.
  `rounded`는 `9999px` → `999999px`로 정정. Border Width 토큰 추가.
