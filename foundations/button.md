# Button

> 사용자가 취할 수 있는 액션을 표현. 폼 제출 · 작업 시작 · 페이지 이동 등.

[← Components](./README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | componentKey | 용도 |
|------|------|--------------|------|
| `button` | component_set | `fdff8da5b3c2d1f992a124335acbfbd4c7252f7e` | 기본 버튼 (사이즈 변형) |
| `Button` | component | `6fc735282dd1333a73e920e6c292d0f61d74761e` | 단일 인스턴스 |
| `button_48px` | component_set | `8e2a3a35bd5ca8de9c0e70fe1dfa4204aed0eac8` | 고정 48px 변형 |
| `btn_s_default` | component_set | `ba398865e4078f4f04c3d7624deed7dceb2853e7` | Small 사이즈 |
| `icon button` | component_set | `c7a26ef430b0d19af0996b7bf101a5b821ed2ebb` | 아이콘 전용 |
| `Button Stack` | component_set | `f0f26be2292c003aef2d3858a771dec0a17eb78f` | 버튼 그룹 |

---

## 2. Anatomy

```
[Button]
├── [Leading Icon]   (옵션, 좌측)
├── [Label]          (필수)
└── [Trailing Icon]  (옵션, 우측: chevron, arrow 등)
```

---

## 3. Variant (Hierarchy)

| 변형 | 용도 | 배경 | 텍스트 |
|------|------|------|--------|
| `primary` | 메인 액션, 페이지당 1개 | `Color/bg/interactive/primary` (green 500) | 흰색 |
| `secondary` | 보조 액션 | `Color/bg/secondary` | `Color/text/primary` |
| `tertiary` (ghost) | 약한 액션 | transparent | `Color/text/primary` |
| `outline` | 보조 강조 | transparent + `Color/border/primary` | `Color/text/primary` |
| `danger` | 파괴적 액션 (삭제) | `Color/bg/danger` | 흰색 |
| `link` | 인라인 텍스트 액션 | transparent | `Color/text/info` + underline |

---

## 4. Size

| 사이즈 | 높이 | 패딩 좌우 | Text Style | 아이콘 크기 | Figma |
|--------|------|-----------|------------|-------------|-------|
| `xs` | 24px | `spacing/8` | `body/sm/medium` | 12 | `btn_s_default` |
| `sm` | 32px | `spacing/12` | `body/sm/medium` | 16 | `button` (Small) |
| `md` | 40px | `spacing/16` | `body/md/medium` | 16 | `button` (Medium, default) |
| `lg` | 48px | `spacing/16` | `body/md/medium` | 20 | `button_48px` |

---

## 5. States

[foundations/state.md](../foundations/state.md) 기준. 각 variant × 사이즈 × 상태 조합.

```css
.btn {
  border-radius: var(--radius-md);
  transition:
    transform var(--motion-duration-instant) var(--motion-easing-standard),
    background-color var(--motion-duration-instant) var(--motion-easing-standard);
}

.btn[data-variant="primary"] {
  background: var(--color-bg-interactive-primary); /* green 500 #14bc62 */
  color: #fff;
}
.btn[data-variant="primary"]:hover  { background: var(--color-bg-interactive-primary-hover); }   /* green 700 */
.btn[data-variant="primary"]:active { background: var(--color-bg-interactive-primary-pressed); transform: scale(0.97); } /* green 800 */

.btn:focus-visible {
  outline: 2px solid var(--color-border-info);
  outline-offset: 2px;
}
.btn:disabled,
.btn[aria-disabled="true"] {
  background: var(--color-bg-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
  pointer-events: none;
}
.btn[data-loading="true"] { pointer-events: none; }
```

---

## 6. Props (React)

```tsx
type ButtonProps = {
  variant?: 'primary' | 'secondary' | 'tertiary' | 'outline' | 'danger' | 'link';
  size?: 'xs' | 'sm' | 'md' | 'lg';
  iconBefore?: React.ReactNode;
  iconAfter?: React.ReactNode;
  loading?: boolean;
  disabled?: boolean;
  fullWidth?: boolean;
  type?: 'button' | 'submit' | 'reset';
  onClick?: (e: React.MouseEvent) => void;
  children: React.ReactNode;
};
```

---

## 7. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| 배경 | primary → `Color/bg/interactive/primary` (green) · 그 외 `Color/bg/{secondary|danger|disabled}` |
| 라벨 색상 | `Color/text/*` |
| 보더 (outline 변형) | `Color/border/primary` |
| Radius | `border/radius/md` |
| 좌우 패딩 | `spacing/8` ~ `spacing/16` |
| 아이콘 ↔ 라벨 갭 | `spacing/4` ~ `spacing/8` |
| 모션 | press `scale(0.97)`, `duration/instant` |
| Focus | `Color/border/info` outline 2px / offset 2px |

---

## 8. Icon Button

아이콘만 표시하는 정사각형 버튼. componentKey: `c7a26ef430b0d19af0996b7bf101a5b821ed2ebb`.

| 사이즈 | 크기 | 아이콘 크기 |
|--------|------|-------------|
| sm | 32 × 32 | 16 |
| md | 40 × 40 | 20 |
| lg | 48 × 48 | 24 |

- 정사각형, `border/radius/md` 또는 `rounded`(원형 버튼)
- **`aria-label` 필수**

```tsx
<IconButton aria-label="더 보기" icon={<MoreHorizontal />} />
```

---

## 9. Button Stack

여러 버튼을 그룹으로 정렬. componentKey: `f0f26be2292c003aef2d3858a771dec0a17eb78f`.

```tsx
<ButtonStack align="end" gap="12">
  <Button variant="tertiary">취소</Button>
  <Button variant="primary">저장</Button>
</ButtonStack>
```

- 갭: `spacing/8` (좁게) 또는 `spacing/12` (기본)
- 정렬: `start` · `center` · `end` · `between`
- 모바일 풀폭: 세로 스택 + 풀폭 버튼

---

## 10. Accessibility

- `<button>` 엘리먼트 사용 (div + onClick 금지)
- `type="submit" | "button" | "reset"` 명시
- 로딩 중 `aria-busy="true"`
- 아이콘 전용 버튼은 `aria-label` 필수
- 폼 내부 기본 type은 `"button"` (의도치 않은 submit 방지)
- 터치 타깃 최소 **44 × 44px** 확보 (xs/sm은 클릭 영역만 확장)
- 키보드: `Tab` 포커스, `Enter`/`Space` 활성화

---

## 11. Do / Don't

✅ **DO**
- 페이지당 `primary` 1개
- 액션 동사로 명명 ("저장", "삭제 확인", "결제하기")
- 위험한 액션은 `danger` variant + 추가 확인 단계
- 비활성 이유는 툴팁/도움말로 설명

❌ **DON'T**
- 한 행에 primary 여러 개 배치
- "확인", "OK", "예" 같은 모호한 라벨
- 임의 padding/border-radius 인라인
- disabled만 두고 이유 설명 없이 방치

---

## 12. Examples

```tsx
// 1. 기본 저장
<Button variant="primary">저장</Button>

// 2. 아이콘 + 라벨
<Button variant="secondary" iconBefore={<Plus />}>새로 만들기</Button>

// 3. 로딩 중
<Button variant="primary" loading>처리 중…</Button>

// 4. 위험 액션
<Button variant="danger" iconBefore={<Trash />}>삭제</Button>

// 5. 풀폭 (모바일)
<Button variant="primary" fullWidth>로그인</Button>

// 6. 아이콘 전용
<IconButton aria-label="알림" icon={<Bell />} />

// 7. 버튼 그룹 (모달 푸터)
<ButtonStack align="end" gap="12">
  <Button variant="tertiary">취소</Button>
  <Button variant="primary" type="submit">제출</Button>
</ButtonStack>
```
