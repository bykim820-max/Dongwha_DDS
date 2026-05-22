# Border Radius

> `Semantic:Appearance` 컬렉션, 스코프 `CORNER_RADIUS`.

[← design.md](../design.md)

---

## 1. 토큰

| 토큰 | 권장 px | 사용처 |
|------|---------|--------|
| `border/radius/sm` | 4 | Tag, Chip, 작은 인풋 |
| `border/radius/md` | 8 | Button, Card, Tooltip |
| `border/radius/lg` | 12 | Modal, Section |
| `border/radius/xl` | 16 | 큰 카드, Hero |
| `border/radius/2xl` | 24 | Container |
| `border/radius/rounded` | 9999 | Pill, Avatar |

> 정확한 px 값은 Figma 변수 패널에서 확인. 위 값은 일반 컨벤션 기준 추정치.

---

## 2. CSS 매핑

```css
:root {
  --radius-sm:      4px;
  --radius-md:      8px;
  --radius-lg:      12px;
  --radius-xl:      16px;
  --radius-2xl:     24px;
  --radius-rounded: 9999px;
}

.button { border-radius: var(--radius-md); }
.tag    { border-radius: var(--radius-sm); }
.modal  { border-radius: var(--radius-lg); }
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
        sm:        'var(--radius-sm)',
        md:        'var(--radius-md)',
        lg:        'var(--radius-lg)',
        xl:        'var(--radius-xl)',
        '2xl':     'var(--radius-2xl)',
        rounded:   'var(--radius-rounded)',
      },
    },
  },
}
```

---

## 4. 적용 가이드

| 요소 | 권장 |
|------|------|
| 버튼 | `md` |
| 인풋 필드 | `md` |
| Tag · Chip | `sm` |
| 카드 (일반) | `md` ~ `lg` |
| 카드 (대형/히어로) | `xl` |
| 모달 · 시트 | `lg` |
| 컨테이너 · 섹션 | `2xl` (필요 시) |
| 아바타 | `rounded` |
| 필 버튼 (Capsule) | `rounded` |
| 이미지 썸네일 | `sm` 또는 `md` |
| 토스트 · 알림 배너 | `md` |

---

## 5. 규칙

1. **같은 위계의 요소는 같은 radius** (예: 모든 폼 인풋 → `md`)
2. **중첩된 요소는 부모보다 작은 radius**
   - 카드 안의 버튼: 카드 `lg`, 버튼 `md`
   - 모달 안의 카드: 모달 `lg`, 카드 `md`
3. 임의 px 금지 → 토큰만 사용
4. 한 컴포넌트의 4개 모서리는 동일 값 (예외: 바텀시트 상단만 둥글기 등 디자인 의도 시)
5. 아이콘 전용 버튼은 정사각형이면 `md`, 원형이면 `rounded`
