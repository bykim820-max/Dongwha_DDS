# Icon System

> 아이콘은 텍스트의 보조 시각 정보. 단독 사용 시 반드시 `aria-label` 또는 인접 라벨 필요.

[← Components](../components/README.md) · [← design.md](../design.md)

---

## 0. 🚫 절대 금지 규칙

> **이모지를 아이콘으로 사용하는 것을 절대 금지한다.**
> `₩ 🛒 👤 📦 ⏱ ↩ ✅ ⚠️ 🔔 📊 ✨` 등 모든 이모지·기호 문자를 UI 아이콘 자리에 쓰지 않는다.
> 통화·단위 표기(예: 금액의 `₩`, `%`)처럼 **텍스트의 일부로 쓰는 글리프는 예외** — 단, 아이콘 칩/버튼/네비 자리에는 금지.

- **모든 아이콘은 라인(아웃라인) 스타일 SVG 1종 세트로 통일한다.** (`stroke="currentColor"`, fill 없음)
  - 권장: Lucide / Feather 계열 같은 **얇은 라인 아이콘**. solid·duotone·3D·컬러풀 이모지형 금지.
- stroke 두께는 §2 규칙(16–20px → 1.5px / 24px+ → 2px)으로 **한 세트 안에서 일관**.
- 색은 `Color/icon/*` 토큰 + `currentColor`. 아이콘 자체에 다색·그라데이션 금지(상태 의미색은 허용).
- 라이브러리에 없는 의미가 필요하면 **같은 라인 세트에서 추가**하고 Figma·문서에 등록(임의 이모지 대체 금지).

---

## 1. 컴포넌트 패밀리

라이브러리에 게시된 대표 아이콘 (전체는 Figma에서 확인):

| 이름 | componentKey | 용도 |
|------|--------------|------|
| `user` | `4203c055d4acfd5c84bd2fde6ce625e23e16dc8a` | 사용자, 프로필 |
| `bell_on` | `12399fd9d6af63bf410306bedebbc9fb3c9880f6` | 알림 |
| `more-horizontal` | `5b7ad793f26e79fe7e349c005a12d3b7b74a3ff7` | 더보기 메뉴 (가로 점 3개) |
| `check-square` | `f9cc1062fadf00fbc6467d6824b90d516efbb4f5` | 체크박스용 |
| `message-square` | `ffb772730a30ef84dfdd0df9afd965e5b0329818` | 메시지, 댓글 |
| `Icon placeholder` | `8868c045bed192a967b70eacec637ec8ea259a35` | 자리 표시자 (Variant Set) |

---

## 2. Sizes

| 사이즈 | px | 용도 |
|--------|----|----- |
| `xs` | 12 | xs 버튼 내부, 인라인 보조 |
| `sm` | 16 | 기본 (버튼, 인풋, 인라인) |
| `md` | 20 | lg 버튼, 헤더 |
| `lg` | 24 | 페이지 헤더, 강조 |
| `xl` | 32 | 빈 상태 일러스트 |
| `2xl` | 48 | 히어로 |

> Stroke 두께: 16/20px → **1.5px**, 24px+ → **2px** (Figma 정의 기준)

---

## 3. Color Tokens

| 컨텍스트 | 토큰 |
|----------|------|
| 기본 본문 옆 | `Color/icon/primary` |
| 보조/부가 | `Color/icon/secondary` |
| 약한 강조 | `Color/icon/tertiary` |
| 정보 알림 | `Color/icon/info` |
| 성공 | `Color/icon/success` |
| 경고 | `Color/icon/warning` |
| 에러 | `Color/icon/danger` |
| 비활성 | `Color/icon/disabled` |
| 버튼 내부 (브랜드 배경 위) | `#FFFFFF` |

**`currentColor` 활용**: SVG `fill="currentColor"` 또는 `stroke="currentColor"`로 두면 부모 `color` 변경 시 자동 따라감.

```css
.icon { color: var(--color-icon-primary); }
.text-text-danger .icon { color: var(--color-icon-danger); }
```

---

## 4. SVG 컴포넌트 패턴 (React)

```tsx
type IconProps = {
  size?: 12 | 16 | 20 | 24 | 32 | 48;
  color?: string;            // CSS 변수 가능
  'aria-label'?: string;     // 단독 사용 시 필수
  'aria-hidden'?: boolean;   // 텍스트 옆에 장식용일 때 true
  className?: string;
};

function BellIcon({ size = 16, 'aria-label': label, 'aria-hidden': hidden = !label, ...rest }: IconProps) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={size >= 24 ? 2 : 1.5}
      role={label ? 'img' : undefined}
      aria-label={label}
      aria-hidden={hidden || undefined}
      {...rest}
    >
      {/* path */}
    </svg>
  );
}
```

---

## 5. 사용 위치별 가이드

| 위치 | 사이즈 | 색상 | 라벨 |
|------|--------|------|------|
| 버튼 내부 (라벨 옆) | 16 또는 20 | 라벨 색상 따라감 | `aria-hidden="true"` |
| Icon Button | 16 / 20 / 24 | 버튼 텍스트 색 | `aria-label` 필수 (부모 버튼에) |
| 인풋 leading/trailing | 16 또는 20 | `Color/icon/tertiary` | `aria-hidden="true"` |
| 알림 배지 | 16 | 컨텍스트 색 | `aria-label` (의미 있을 때) |
| 빈 상태 일러스트 | 48 ~ 64 | 흐릿한 톤 | `aria-hidden="true"` |
| 페이지 헤더 옆 | 24 | `Color/icon/primary` | `aria-hidden="true"` |
| 상태 아이콘 (성공·경고·에러) | 16 ~ 20 | 의미 토큰 | `aria-label` (상태 명) |

---

## 6. Accessibility

### 단독 사용 (장식 아님)
- `role="img"` + `aria-label="설명"`
- 예: 외부 링크 표시 아이콘만 있는 경우 `aria-label="외부 링크 (새 창)"`

### 텍스트 옆 (장식)
- `aria-hidden="true"` 부여
- 텍스트가 의미를 전달하므로 아이콘은 시각 보조

### 버튼 안에 있을 때
- 부모 `<button>`이 라벨을 가지면 아이콘은 `aria-hidden="true"`
- Icon-only 버튼이면 부모에 `aria-label="액션 이름"` 필수

### 색만으로 의미 전달 금지
- 성공/에러를 색으로만 표시 ✕
- 색 + 아이콘 형상 + 텍스트 3중 표시 ✓

---

## 7. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| 아이콘 색 | `Color/icon/*` (primary/secondary/tertiary/info/success/warning/danger/disabled) |
| Stroke 두께 | 16-20px → 1.5px / 24px+ → 2px |
| 사이즈 | 12 · 16 · 20 · 24 · 32 · 48 |

---

## 8. Do / Don't

✅ **DO**
- 동일 의미 = 동일 아이콘 (예: 삭제 = 항상 휴지통)
- `currentColor`로 색 상속 활용
- 16/20px 아이콘에는 1.5px stroke 유지 (시각 균형)
- 의미 있는 아이콘에는 `aria-label`, 장식 아이콘은 `aria-hidden`

❌ **DON'T**
- **이모지·기호 문자를 아이콘으로 사용** (`🛒 👤 📦 🔔 ✅` 등) — §0 절대 금지
- solid·duotone·3D·컬러 이모지형 아이콘을 라인 세트와 혼용
- 라벨 없는 아이콘 버튼 ("?" 같은 모호한 모양)
- 같은 페이지 안에 같은 의미에 다른 아이콘 혼용
- 아이콘 크기 임의 조정 (12.5, 18 같은 비표준 값)
- 다른 stroke 두께 아이콘 혼용

---

## 9. Examples

```tsx
// 1. 텍스트 옆 장식 아이콘
<button>
  <Plus aria-hidden="true" /> 새로 만들기
</button>

// 2. 아이콘 단독 (의미 있음)
<a href="https://..." aria-label="외부 링크에서 열기">
  <ExternalLink aria-hidden="true" />
</a>

// 3. 상태 아이콘 (의미 + 색)
<span role="status" className="text-text-success">
  <CheckCircle aria-label="성공" size={16} />
  저장되었습니다
</span>

// 4. Icon Button
<IconButton aria-label="알림" icon={<Bell size={20} />} />

// 5. 인풋 leading
<Input
  type="search"
  label="검색"
  leadingIcon={<Search aria-hidden="true" size={16} />}
/>

// 6. 빈 상태
<EmptyState
  icon={<Inbox size={48} aria-hidden="true" />}
  title="받은 메시지가 없습니다"
/>
```
