# Spacing

> **8pt 그리드 기반**. `Semantic:Appearance` 컬렉션.
> 모든 패딩·마진·갭에 토큰만 사용. 임의 px 금지.

[← design.md](../design.md)

---

## 1. 토큰

| 토큰 | px |
|------|----|
| `spacing/0` | 0 |
| `spacing/2` | 2 |
| `spacing/4` | 4 |
| `spacing/8` | 8 |
| `spacing/12` | 12 |
| `spacing/16` | 16 |
| `spacing/24` | 24 |
| `spacing/32` | 32 |
| `spacing/40` | 40 |
| `spacing/48` | 48 |
| `spacing/64` | 64 |

스코프: `WIDTH_HEIGHT`, `GAP` (패딩·마진·갭에 공통 적용).

---

## 2. CSS 매핑

```css
:root {
  --space-0:  0;
  --space-2:  2px;
  --space-4:  4px;
  --space-8:  8px;
  --space-12: 12px;
  --space-16: 16px;
  --space-24: 24px;
  --space-32: 32px;
  --space-40: 40px;
  --space-48: 48px;
  --space-64: 64px;
}

.card { padding: var(--space-16); }
.stack { display: flex; flex-direction: column; gap: var(--space-12); }
```

---

## 3. Tailwind 매핑

```js
// tailwind.config.js
module.exports = {
  theme: {
    spacing: {
      0:  '0',
      2:  '2px',
      4:  '4px',
      8:  '8px',
      12: '12px',
      16: '16px',
      24: '24px',
      32: '32px',
      40: '40px',
      48: '48px',
      64: '64px',
    },
  },
}
```

> ⚠️ Tailwind 기본 `p-4` = `16px`인데 DDS는 **토큰 키 = px 값**으로 통일.
> 따라서 DDS Tailwind에서 `p-16`이 `16px`이다.

---

## 4. 적용 가이드

| 컨텍스트 | 권장 토큰 |
|----------|-----------|
| 버튼 내부 좌우 패딩 | `spacing/12` ~ `spacing/16` |
| 버튼 내부 상하 패딩 | `spacing/8` ~ `spacing/12` |
| 인풋 내부 패딩 | `spacing/12` ~ `spacing/16` |
| 카드 내부 패딩 | `spacing/16` ~ `spacing/24` |
| 모달 내부 패딩 | `spacing/24` ~ `spacing/32` |
| 섹션 간 간격 | `spacing/32` ~ `spacing/48` |
| 페이지 좌우 여백 (데스크톱) | `spacing/40` ~ `spacing/64` |
| 페이지 좌우 여백 (모바일) | `spacing/16` ~ `spacing/24` |
| 폼 필드 간 갭 | `spacing/12` ~ `spacing/16` |
| 인라인 아이콘과 텍스트 갭 | `spacing/4` ~ `spacing/8` |
| 리스트 아이템 간 갭 | `spacing/8` ~ `spacing/12` |
| 텍스트 줄 사이 (다른 위계) | `spacing/4` ~ `spacing/8` |

---

## 5. 규칙

1. **임의 px 금지** — 토큰에 없는 값(예: 18, 22)은 가까운 토큰으로 스냅 (디자이너 컨펌)
2. 새 값이 필요하면 **토큰 추가 요청**, 인라인 px 금지
3. 음수 마진은 가급적 피하고 부모 패딩으로 조정
4. **`gap` 우선, 마진 두 번째** — flexbox/grid에서 `gap`을 우선 사용
5. 동일 위계의 요소는 동일 spacing 사용 (예: 모든 카드 내부 → `spacing/16`)
6. 중첩 시 outer > inner 원칙 (페이지 > 섹션 > 카드 > 카드 내부)
