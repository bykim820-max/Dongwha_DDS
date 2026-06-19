# Checkbox

> 여러 항목 중 0개 이상을 선택하는 컨트롤. 폼 제출 시 값으로 전달.

[← Components](../components/README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | componentKey |
|------|------|--------------|
| `check-square` | component | `f9cc1062fadf00fbc6467d6824b90d516efbb4f5` |

> 그룹 사용 시 [Option Group](../components/option-group.md) 참고.

---

## 2. Anatomy

```
[Checkbox Wrapper] ← 클릭 영역 전체
├── [Box]
│   └── [Check Icon]  (checked 또는 indeterminate일 때)
└── [Label]           (옵션 우측)
```

---

## 3. Variants

| Property | 값 | 의미 |
|----------|-----|------|
| `state` | `unchecked` · `checked` · `indeterminate` | 체크 상태 |
| `disabled` | bool | 비활성 |
| `error` | bool | 에러 상태 (보더 빨강) |

`indeterminate`: 자식 항목 중 일부만 체크된 부모 체크박스에 사용 (시각적으로 "−" 표시).

---

## 4. Size

| 사이즈 | Box | 아이콘 |
|--------|-----|--------|
| `sm` | 16 × 16 | 10 |
| `md` | 20 × 20 | 14 |

---

## 5. States & Tokens

| 상태 | Box 배경 | Box 보더 | 아이콘 |
|------|----------|----------|--------|
| unchecked | `Color/bg/primary` | `Color/border/secondary` | 없음 |
| unchecked hover | `Color/bg/primary` | `Color/border/primary` | 없음 |
| checked | `Color/bg/interactive/primary` (green 500 = `#14bc62`) | none | white |
| indeterminate | `Color/bg/interactive/primary` (green 500 = `#14bc62`) | none | white (가로선) |
| disabled | `Color/bg/disabled` | `Color/border/disabled` | `Color/text/disabled` |
| error | `Color/bg/primary` | `Color/border/danger` | — |
| focus-visible | — | outline `Color/border/info` 2px | — |

```css
.checkbox {
  width: 20px; height: 20px;
  border: 1.5px solid var(--color-border-secondary);
  border-radius: var(--radius-sm);
  background: var(--color-bg-primary);
  display: inline-grid; place-items: center;
  transition:
    background-color var(--motion-duration-quick) var(--motion-easing-standard),
    border-color var(--motion-duration-quick) var(--motion-easing-standard);
}
.checkbox[aria-checked="true"],
.checkbox[aria-checked="mixed"] {
  background: var(--color-bg-interactive-primary); /* green 500 */
  border-color: transparent;
}
.checkbox[aria-checked="true"] svg,
.checkbox[aria-checked="mixed"] svg { color: #fff; }
.checkbox:focus-visible {
  outline: 2px solid var(--color-border-info);
  outline-offset: 2px;
}
```

---

## 6. Props (React)

```tsx
type CheckboxProps = {
  checked: boolean | 'indeterminate';
  onChange: (checked: boolean) => void;
  label?: string;
  size?: 'sm' | 'md';
  disabled?: boolean;
  error?: boolean;
  required?: boolean;
  name?: string;
  value?: string;
  'aria-label'?: string;          // label 없을 때 필수
};
```

---

## 7. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| Box 배경 (unchecked) | `Color/bg/primary` |
| Box 배경 (checked) | `Color/bg/interactive/primary` (green 500 = `#14bc62`) |
| Box 보더 | `Color/border/{secondary|primary|danger|disabled}` |
| 아이콘 | white |
| Radius | `border/radius/sm` |
| 라벨 색상 | `Color/text/primary` |
| 라벨 ↔ Box 갭 | `spacing/8` |
| 모션 | `duration/quick` + `easing/standard` |

---

## 8. Accessibility

- `<input type="checkbox">` 또는 `<button role="checkbox" aria-checked>` 사용
- `indeterminate`는 `aria-checked="mixed"`로 표현
- 라벨은 클릭 가능 영역에 포함 — `<label>` 또는 wrapper로 감싸기
- 그룹 사용 시 `<fieldset>` + `<legend>`로 묶기
- 키보드: `Tab` 포커스, `Space`로 토글
- 에러 메시지는 `aria-describedby`로 연결
- 색만으로 에러 표시 금지 — 텍스트 메시지 병행

---

## 9. Do / Don't

✅ **DO**
- 라벨을 명확한 명사구로 ("이용약관에 동의합니다")
- 그룹 시 `<fieldset legend>` 사용
- 부모-자식 그룹에서 indeterminate 활용
- 필수 동의 항목은 `required` + 시각 표식 (`*`)

❌ **DON'T**
- 단일 항목인데 그룹 처리
- `Switch`와 혼용 — 즉시 적용 설정은 Switch 사용
- 라벨을 동사로 ("동의하기") — Button처럼 보임

---

## 10. Examples

```tsx
// 1. 기본
const [agreed, setAgreed] = useState(false);
<Checkbox
  label="이용약관에 동의합니다"
  checked={agreed}
  onChange={setAgreed}
  required
/>

// 2. Indeterminate (부모-자식)
const all = items.every(i => i.checked);
const some = items.some(i => i.checked);
<Checkbox
  label="전체 선택"
  checked={all ? true : some ? 'indeterminate' : false}
  onChange={(c) => setAllItems(c)}
/>

// 3. 에러
<Checkbox
  label="필수 약관에 동의합니다"
  checked={agreed}
  onChange={setAgreed}
  error={!agreed && submitted}
  required
/>

// 4. 그룹
<fieldset>
  <legend className="text-body-sm-medium">관심 분야</legend>
  <div className="flex flex-col gap-8">
    {topics.map(t => (
      <Checkbox
        key={t.id}
        label={t.name}
        checked={selected.includes(t.id)}
        onChange={(c) => toggle(t.id, c)}
      />
    ))}
  </div>
</fieldset>
```
