# Input / Text Field

> 사용자가 텍스트를 입력하는 폼 컨트롤.

[← Components](./README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | componentKey |
|------|------|--------------|
| `Part/Text field placeholder` | component_set | `a00a00a43688a2051c685eeb8bc2a9014d6f34d9` |

---

## 2. Anatomy

```
[Field Wrapper]
├── [Label]            (옵션, 위)
├── [Input Container]
│   ├── [Leading Icon]    (옵션)
│   ├── [Prefix]          (옵션, 예: "₩", "https://")
│   ├── [Native <input>]  ← 실제 입력 영역
│   ├── [Clear Button]    (옵션, 값 있을 때)
│   ├── [Suffix]          (옵션)
│   └── [Trailing Icon]   (옵션, 상태 아이콘)
└── [Helper Text / Error] (옵션, 아래)
```

---

## 3. Variants

| Property | 값 | 의미 |
|----------|-----|------|
| `type` | `text` · `email` · `password` · `number` · `tel` · `url` · `search` | HTML input type |
| `state` | `default` · `focus` · `error` · `success` · `disabled` · `read-only` | 시각 상태 |
| `hasLeadingIcon` | bool | 좌측 아이콘 표시 |
| `hasTrailingIcon` | bool | 우측 아이콘 표시 |
| `hasClearButton` | bool | Clear (X) 버튼 |

---

## 4. Size

| 사이즈 | 높이 | 좌우 패딩 | Text Style |
|--------|------|-----------|------------|
| `sm` | 32px | `spacing/8` | `body/sm/regular` |
| `md` | 40px | `spacing/12` | `body/md/regular` |
| `lg` | 48px | `spacing/16` | `body/md/regular` |

---

## 5. States

| 상태 | 보더 | 배경 | 비고 |
|------|------|------|------|
| `default` | `Color/border/secondary` | `Color/bg/primary` | — |
| `hover` | `Color/border/primary` | `Color/bg/primary` | 마우스 오버 |
| `focus` | `Color/border/info` 2px | `Color/bg/primary` | 키보드/클릭 |
| `error` | `Color/border/danger` | `Color/bg/primary` | helper에 에러 메시지 |
| `success` | `Color/border/success` | `Color/bg/primary` | helper에 확인 메시지 |
| `disabled` | `Color/border/disabled` | `Color/bg/disabled` | cursor: not-allowed |
| `read-only` | `Color/border/secondary` | `Color/bg/secondary` | 보더 유지, 배경만 회색 |

```css
.input {
  height: 40px;
  padding: 0 var(--space-12);
  border: 1px solid var(--color-border-secondary);
  border-radius: var(--radius-md);
  background: var(--color-bg-primary);
  font: var(--body-md-regular);
  transition: border-color var(--motion-duration-quick) var(--motion-easing-standard);
}
.input:hover  { border-color: var(--color-border-primary); }
.input:focus-visible {
  border-color: var(--color-border-info);
  outline: 2px solid var(--color-border-info);
  outline-offset: -2px;
}
.input[aria-invalid="true"] { border-color: var(--color-border-danger); }
.input:disabled {
  background: var(--color-bg-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}
```

---

## 6. Props (React)

```tsx
type InputProps = {
  label?: string;
  helperText?: string;
  errorText?: string;
  size?: 'sm' | 'md' | 'lg';
  state?: 'default' | 'error' | 'success';
  leadingIcon?: React.ReactNode;
  trailingIcon?: React.ReactNode;
  prefix?: React.ReactNode;
  suffix?: React.ReactNode;
  clearable?: boolean;
  required?: boolean;
  readOnly?: boolean;
  disabled?: boolean;
  // ...native input attrs: type, placeholder, value, onChange, ...
} & React.InputHTMLAttributes<HTMLInputElement>;
```

---

## 7. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| 배경 | `Color/bg/primary` (default) · `Color/bg/disabled` |
| 보더 | `Color/border/{secondary|primary|info|danger|success}` |
| 라벨 색상 | `Color/text/primary` |
| Placeholder 색상 | `Color/text/tertiary` |
| Helper/Error 색상 | `Color/text/tertiary` · `Color/text/danger` |
| Radius | `border/radius/md` |
| 좌우 패딩 | `spacing/8` ~ `spacing/16` |
| 아이콘 ↔ 텍스트 갭 | `spacing/8` |
| 라벨 ↔ 인풋 갭 | `spacing/4` ~ `spacing/8` |
| 인풋 ↔ 헬퍼 갭 | `spacing/4` |

---

## 8. Accessibility

- **항상 `<label>`을 연결** — `htmlFor` + `id` 매칭
- 시각적으로 라벨 숨겨야 한다면 `.sr-only` 클래스 + 스크린리더용 텍스트
- 에러 상태: `aria-invalid="true"` + `aria-describedby={errorId}` + 에러 메시지에 `role="alert"`
- 필수 입력: `required` 속성 + 시각 표식 (예: `*`) — 색만으로 알리지 말 것
- `placeholder`는 라벨 대체용 금지 (단순 힌트로만)
- `autocomplete` 적절히 설정 (`email`, `current-password`, `one-time-code` 등)
- 모바일에서 `inputmode` 활용 (예: `numeric`, `decimal`, `tel`)
- 터치 타깃 최소 44 × 44px

---

## 9. Do / Don't

✅ **DO**
- 라벨은 위쪽 정렬 (좌측 정렬은 폭 변동에 약함)
- Placeholder는 예시 (예: "name@example.com")만
- 에러는 보더 색 + 아이콘 + 텍스트 메시지 3중 표시
- 비밀번호 필드는 표시/숨김 토글 제공

❌ **DON'T**
- 라벨 없이 placeholder만 사용
- 에러를 색으로만 표시
- 인풋 안에 너무 많은 정보 욱여넣기 (prefix + suffix + icon + …)
- `<div contenteditable>` 같은 비표준 사용

---

## 10. Examples

```tsx
// 1. 기본
<Input label="이메일" type="email" placeholder="name@example.com" />

// 2. 에러
<Input
  label="이메일"
  type="email"
  value={email}
  state="error"
  errorText="유효한 이메일 형식이 아닙니다."
/>

// 3. 아이콘 + Clear
<Input
  label="검색"
  type="search"
  leadingIcon={<Search />}
  clearable
  value={query}
  onChange={(e) => setQuery(e.target.value)}
/>

// 4. 비밀번호 + 표시 토글
<Input
  label="비밀번호"
  type={visible ? 'text' : 'password'}
  trailingIcon={
    <IconButton
      aria-label={visible ? '숨김' : '표시'}
      icon={visible ? <EyeOff /> : <Eye />}
      onClick={() => setVisible(v => !v)}
    />
  }
  autoComplete="current-password"
/>

// 5. Prefix (금액 입력)
<Input
  label="금액"
  type="number"
  prefix="₩"
  inputMode="numeric"
  required
/>

// 6. 읽기 전용
<Input label="회원 ID" value="DW-12345" readOnly />
```
