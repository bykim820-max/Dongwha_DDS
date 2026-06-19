# Skeleton

> 콘텐츠가 도착하기 전, **실제 레이아웃과 동일한 형태의 자리표시자**를 보여주는 로딩 피드백.
> 스피너보다 체감 대기시간을 줄이고, 레이아웃 시프트를 방지한다.

[← Components](./README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | 비고 |
|------|------|------|
| `Skeleton` | 패턴(유틸) | 단일 블록. variant로 형태 지정 |
| `Skeleton Group` | 패턴 | 카드·리스트·테이블 행 등 복합 자리표시자 조합 |

> Figma 컴포넌트가 아니라 **토큰 기반 구현 패턴**. 실제 콘텐츠 컴포넌트의 크기를 그대로 본떠 만든다.

---

## 2. Anatomy

```
[Skeleton Block]            ← 실제 요소 1개당 1블록
├── 형태: text | circle | rect | card
├── 크기: 실제 콘텐츠와 동일 (w/h)
└── 펄스 애니메이션 (shimmer)
```

---

## 3. Variants

| Property | 값 | 의미 |
|----------|-----|------|
| `variant` | `text` · `circle` · `rect` · `card` | 자리표시자 형태 |
| `lines` | number (text 전용) | 텍스트 줄 수 (마지막 줄은 60% 폭) |
| `animation` | `pulse`(기본) · `none` | 펄스 on/off (reduced-motion 시 강제 none) |

- `text`: 한 줄 높이 = 본문 line-height, radius `sm`
- `circle`: 아바타·아이콘 자리, radius `rounded`
- `rect`: 이미지·썸네일, radius `md`
- `card`: 카드 전체 골격(여러 블록 조합)

---

## 4. Sizes

자체 사이즈 토큰 없음 — **본뜨는 실제 컴포넌트의 크기를 그대로 사용**한다.

| 자리표시 대상 | 권장 |
|----------------|------|
| 본문 텍스트 줄 | height = `--body-md-line-height`, radius `sm` |
| 제목 | height = `--heading-sm-font-size`, radius `sm` |
| 아바타 | 실제 아바타 px, radius `rounded` |
| 썸네일/이미지 | 실제 px, radius `md` |

---

## 5. States

| 상태 | 설명 | 처리 |
|------|------|------|
| `loading` | 데이터 요청 중 | 스켈레톤 표시, 컨테이너에 `aria-busy="true"` |
| `loaded` | 데이터 도착 | 스켈레톤 fade-out 120ms ↔ 콘텐츠 fade-in 200ms (중첩 80ms) — motion.md §5.7 |
| `error` | 실패 | 스켈레톤 제거 후 에러 피드백(→ [feedback.md](./feedback.md) Inline Alert) |

> **레이아웃 시프트 금지**: 스켈레톤 크기 = 실제 콘텐츠 크기. 도착 후 위치가 튀면 안 된다.

```css
.skeleton {
  background: var(--color-bg-tertiary);
  border-radius: var(--radius-sm);
  position: relative;
  overflow: hidden;
}
.skeleton--circle { border-radius: var(--radius-rounded); }
.skeleton--rect   { border-radius: var(--radius-md); }

/* shimmer: 좌→우로 지나가는 하이라이트 (motion.md §5.7, 1200ms 무한) */
.skeleton::after {
  content: "";
  position: absolute; inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(90deg, transparent, var(--color-bg-secondary), transparent);
  animation: skeleton-shimmer 1200ms ease-in-out infinite;
}
@keyframes skeleton-shimmer { 100% { transform: translateX(100%); } }

@media (prefers-reduced-motion: reduce) {
  .skeleton::after { animation: none; }
  .skeleton { opacity: 0.7; }   /* 정적 표시 */
}
```

> 참고: shimmer는 **로딩 피드백이라는 기능적 목적**의 그라데이션이라 [디자인 금지 규칙](../design.md#-디자인-금지-규칙-anti-patterns)의 "장식적 그라데이션 띠"에 해당하지 않는다.

---

## 6. Props (React)

```tsx
type SkeletonProps = {
  variant?: 'text' | 'circle' | 'rect' | 'card';
  width?: number | string;
  height?: number | string;
  lines?: number;              // variant="text"일 때 줄 수
  animation?: 'pulse' | 'none';
  className?: string;
};

// 컨테이너에서 로딩 상태 분기
function UserCard({ loading, user }: { loading: boolean; user?: User }) {
  if (loading) {
    return (
      <div className="card" aria-busy="true" aria-live="polite">
        <Skeleton variant="circle" width={40} height={40} />
        <Skeleton variant="text" lines={2} />
      </div>
    );
  }
  return <div className="card">{/* 실제 콘텐츠 */}</div>;
}
```

---

## 7. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| 베이스 면 | `Color/bg/tertiary` |
| shimmer 하이라이트 | `Color/bg/secondary` |
| Radius | text/제목 `sm` · 이미지 `md` · 아바타 `rounded` |
| 줄 높이 | `--body-*-line-height` / `--heading-*-font-size` |
| 펄스 모션 | 1200ms ease-in-out 무한 (motion.md §5.7) |
| 전환 | fade-out 120ms ↔ fade-in 200ms |

---

## 8. Accessibility

- 로딩 컨테이너에 `aria-busy="true"`, 도착 시 `false`로 전환
- 스켈레톤 블록 자체는 `aria-hidden="true"`(장식). 상태는 컨테이너의 `aria-live="polite"`로 안내
- 스크린리더용 텍스트 보조: "콘텐츠를 불러오는 중" 등 시각적으로 숨긴 라벨 권장
- `prefers-reduced-motion`: 펄스 제거, 정적 표시 유지

---

## 9. Do / Don't

✅ **DO**
- 스켈레톤 크기 = 실제 콘텐츠 크기 (시프트 0)
- 실제 레이아웃 구조(아바타+2줄 등)를 그대로 본뜸
- 0.3초 이내 끝나는 로딩은 스켈레톤 없이 즉시 표시 (깜빡임 방지)
- 긴 로딩(>1초)·리스트/카드형 콘텐츠에 사용

❌ **DON'T**
- 스피너와 스켈레톤 **동시 표시**
- 콘텐츠보다 작거나 큰 스켈레톤 → 도착 시 레이아웃 점프
- 무한 스켈레톤(타임아웃·에러 처리 없이 방치)
- 텍스트 한 줄짜리·즉시 뜨는 값에 스켈레톤 남발

---

## 10. Examples

```tsx
// 1. 텍스트 2줄
<Skeleton variant="text" lines={2} />

// 2. 아바타 + 이름/직책
<div className="row" aria-busy="true">
  <Skeleton variant="circle" width={40} height={40} />
  <div>
    <Skeleton variant="text" width={120} />
    <Skeleton variant="text" width={80} />
  </div>
</div>

// 3. 테이블 행 5개
{loading
  ? Array.from({ length: 5 }).map((_, i) => (
      <tr key={i} aria-hidden="true">
        <td><Skeleton variant="text" width={64} /></td>
        <td><Skeleton variant="text" width={100} /></td>
        <td><Skeleton variant="text" width={48} /></td>
      </tr>
    ))
  : rows.map(/* 실제 행 */)}

// 4. 카드 그리드
{loading && <SkeletonCard />}
```
