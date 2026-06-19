# State System

> 모든 인터랙티브 컴포넌트는 다음 상태 시스템을 일관되게 사용한다.

[← design.md](../design.md)

---

## 1. 상태 정의

| 상태 | 트리거 | 시각 표현 |
|------|--------|----------|
| `default` | 기본 | 기본 토큰 |
| `hover` | 마우스 오버 | 배경/보더 한 단계 변화 |
| `pressed` / `active` | 클릭 중 | 배경 두 단계 어둡게 + `scale(0.97)` |
| `focus-visible` | 키보드 탭 | 2px outline (`Color/border/info`) + 2px offset |
| `disabled` | `disabled` 속성 | 회색 배경 + 회색 텍스트 + `cursor: not-allowed` |
| `error` | 검증 실패 | 빨간 보더·텍스트 |
| `success` | 검증 성공 | 녹색 보더·아이콘 |
| `loading` | 비동기 작업 중 | 스피너 · 스켈레톤, 클릭 비활성 |
| `selected` | 선택됨 | 강조 배경 · 보더 |
| `read-only` | 편집 불가 | 배경 변경, 보더 유지 |

---

## 2. 토큰 매핑

| 상태 | 권장 토큰 |
|------|-----------|
| `default` | `Color/bg/primary`, `Color/text/primary` |
| `hover` | bg 한 단계 어둡게 (Primitive 한 단계 내려) |
| `pressed` | bg 두 단계 어둡게 |
| `focus-visible` | outline: `Color/border/info` 2px |
| `disabled` | `Color/bg/disabled` + `Color/text/disabled` |
| `error` | `Color/bg/danger` (옅게) + `Color/border/danger` + `Color/text/danger` |
| `success` | `Color/bg/success` + `Color/border/success` |
| `selected` | `Color/bg/info` (옅게) + `Color/border/info` |

---

## 3. CSS 셀렉터 표준

```css
.button {
  /* default */
  background: var(--color-bg-primary);
  color: var(--color-text-primary);
  transition:
    background-color var(--motion-duration-instant) var(--motion-easing-standard),
    transform var(--motion-duration-instant) var(--motion-easing-standard);
}

.button:hover {
  /* hover */
  background: var(--color-bg-interactive-secondary-hover);
}

.button:active {
  /* pressed */
  transform: scale(0.97);
  background: var(--color-bg-interactive-secondary-pressed);
}

.button:focus-visible {
  outline: 2px solid var(--color-border-info);
  outline-offset: 2px;
}

.button:disabled,
.button[aria-disabled="true"] {
  background: var(--color-bg-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
  pointer-events: none;
}

.button[data-state="error"] {
  border-color: var(--color-border-danger);
  color: var(--color-text-danger);
}

.button[data-loading="true"] {
  pointer-events: none;
  position: relative;
}
```

---

## 4. React 예시

```tsx
type ButtonProps = {
  variant?: 'primary' | 'secondary';
  state?: 'default' | 'error' | 'success';
  loading?: boolean;
  disabled?: boolean;
  children: React.ReactNode;
};

function Button({ variant = 'primary', state = 'default', loading, disabled, children }: ButtonProps) {
  return (
    <button
      className="button"
      data-variant={variant}
      data-state={state}
      data-loading={loading || undefined}
      disabled={disabled}
      aria-busy={loading || undefined}
    >
      {loading ? <Spinner /> : children}
    </button>
  );
}
```

---

## 5. 접근성

- **`disabled` 대신 `aria-disabled="true"`를 우선 검토** — 포커스 가능 유지로 스크린리더가 인지
- 모든 인터랙티브 요소는 **키보드로 접근** 가능해야 함 (`Tab`, `Enter`, `Space`)
- **포커스 링은 `:focus-visible`만 표시** — 마우스 클릭에는 표시 X
- **에러 상태는 색만이 아니라** 아이콘·텍스트로도 표시 (색맹 대응)
- `loading` 상태는 **`aria-busy="true"`** 추가
- 상태 변경은 스크린리더에 알릴 것 (`aria-live` 영역 사용)
- 터치 타깃 최소 **44 × 44px** 확보

---

## 6. 상태 우선순위

여러 상태가 동시에 발생할 때 적용 순서:

```
disabled > loading > error > pressed > focus-visible > hover > selected > default
```

- `disabled`면 다른 상태 모두 무시 (시각·인터랙션 모두)
- `loading`이면 `error` 표시는 가능하지만 인터랙션은 막음
- `focus-visible`과 `hover`는 함께 표시 가능
- `selected`는 다른 활성 상태와 함께 표시될 수 있음 (예: selected + hover)

---

## 7. 컴포넌트별 상태 매트릭스

| 컴포넌트 | default | hover | pressed | focus | disabled | error | loading | selected |
|----------|---------|-------|---------|-------|----------|-------|---------|----------|
| Button | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| Input | ✅ | ✅ | — | ✅ | ✅ | ✅ | — | — |
| Checkbox | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ (checked) |
| Radio | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | ✅ (checked) |
| Switch | ✅ | ✅ | — | ✅ | ✅ | — | — | ✅ (on) |
| Tab | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | ✅ (active) |
| Card | ✅ | ✅ | ✅ | ✅ | — | — | ✅ | ✅ |
| Link | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — |
