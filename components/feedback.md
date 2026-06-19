# Feedback & Status

> 시스템 상태·작업 결과를 사용자에게 알리는 피드백 컴포넌트군.
> 로딩 자리표시는 → [Skeleton](./skeleton.md), 짧은 도움말은 → [Tooltip](./tooltip.md).

[← Components](./README.md) · [← design.md](../design.md)

이 문서는 **5개 피드백 컴포넌트**를 묶어 다룬다: Toast · Inline Alert · Spinner · Progress · Empty State.
공통 규칙: **색만으로 의미 전달 금지** — 의미색 + **라인 아이콘**(이모지 금지, [icons.md §0](./icons.md)) + 텍스트 3중 표시.

---

## 1. 피드백 선택 기준

| 상황 | 컴포넌트 | 지속성 |
|------|----------|--------|
| 작업 결과 알림(저장됨·삭제됨) | **Toast / Snackbar** | 일시(4초 자동) |
| 페이지/폼 영역의 지속 상태(에러·안내) | **Inline Alert / Banner** | 영구(닫기 전까지) |
| 짧은 비결정 로딩(버튼·영역) | **Spinner** | 작업 동안 |
| 진행률이 있는 작업(업로드·단계) | **Progress** | 작업 동안 |
| 데이터 없음·첫 진입 | **Empty State** | 데이터 생길 때까지 |
| 콘텐츠 골격 로딩 | [Skeleton](./skeleton.md) | 도착까지 |

의미(intent)는 4종 공통: `info` · `success` · `warning` · `danger`.

---

## 2. Toast / Snackbar

작업 결과를 화면 모서리에 **일시적으로** 띄우는 알림.

### Variants · Anatomy
```
[Toast]
├── [Leading Icon]  (intent 라인 아이콘)
├── [Message]       (1~2줄)
├── [Action]        (선택, 예: "실행 취소")
└── [Close]         (선택)
```

| Property | 값 |
|----------|-----|
| `intent` | `info` · `success` · `warning` · `danger` |
| `action` | 텍스트 버튼 (선택) |
| `position` | `bottom-center`(기본) · `bottom-right` · `top-center` |

### States & 모션
- 등장: 아래에서 16px 슬라이드 + 페이드인 (`duration/base`, `easing/decelerate`) — motion.md §5.5
- 자동 닫힘 **4초**, 호버 시 일시정지
- 닫힘: 위로 8px + 페이드아웃 (`duration/quick`, `easing/accelerate`)
- 동시 표시 최대 **3개**, 세로 스택

### Tokens
| 영역 | 토큰 |
|------|------|
| 배경 | `Color/bg/inverse-bold` (뉴트럴 다크) 또는 intent `*-subtle` |
| 텍스트 | 다크 배경 위 `#fff` / subtle 위 `Color/text/{intent}` |
| 아이콘 | `Color/icon/{intent}` |
| Radius · 그림자 | `border/radius/md` · `shadow/lg` |
| 모션 | `duration/base`·`quick` + `easing/decelerate`·`accelerate` |

```css
.toast {
  display: flex; align-items: center; gap: var(--space-8);
  padding: var(--space-12) var(--space-16);
  background: var(--color-bg-inverse-bold); color: #fff;
  border-radius: var(--radius-md); box-shadow: var(--shadow-lg);
}
```

### A11y
- `role="status"` (info/success) / `role="alert"` (warning/danger)
- `aria-live="polite"`(status) / `"assertive"`(alert)
- 자동 닫힘이라도 **중요 정보는 Toast 단독으로 쓰지 않음**(놓칠 수 있음)

---

## 3. Inline Alert / Banner

폼·페이지 영역 안에 **지속 표시**되는 상태 메시지. 연한 틴트(`*-subtle`) 면 사용.

| Property | 값 |
|----------|-----|
| `intent` | `info` · `success` · `warning` · `danger` |
| `title` | 굵은 제목 (선택) |
| `dismissible` | 닫기 버튼 유무 |

### Tokens
| intent | 배경 | 텍스트/아이콘 | 보더(선택) |
|--------|------|---------------|-----------|
| info | `Color/bg/info-subtle` | `Color/text/info` | `Color/border/info` |
| success | `Color/bg/success-subtle` | `Color/text/success` | `Color/border/success` |
| warning | `Color/bg/warning-subtle` | `Color/text/warning` | `Color/border/warning` |
| danger | `Color/bg/danger-subtle` | `Color/text/danger` | `Color/border/danger` |

```css
.alert {
  display: flex; gap: var(--space-8);
  padding: var(--space-12) var(--space-16);
  border-radius: var(--radius-md);
  font-size: var(--body-md-font-size);
}
.alert--danger { background: var(--color-bg-danger-subtle); color: var(--color-text-danger); }
.alert .title  { font-weight: var(--font-weight-medium); }
```

### A11y
- `role="alert"`(danger/warning) / `role="status"`(info/success)
- 아이콘은 `aria-hidden`, 의미는 텍스트로

---

## 4. Spinner

진행률을 알 수 없는 **짧은 비결정 로딩**. 라인(원형 스트로크) SVG.

| Property | 값 |
|----------|-----|
| `size` | `sm`(16) · `md`(20) · `lg`(24) |
| `tone` | `primary`(브랜드) · `neutral` · `inverse`(다크 위) |

- stroke 두께 2px, 원호 270° 회전(`360deg`, 800ms linear 무한)
- **0.3초 이상 걸릴 때만** 표시(깜빡임 방지)

### Tokens
| 영역 | 토큰 |
|------|------|
| 트랙 | `Color/border/secondary` |
| 인디케이터 | `Color/bg/interactive/primary`(primary) / `Color/icon/secondary`(neutral) |

```css
.spinner { width: 20px; height: 20px; animation: spin 800ms linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce){ .spinner{ animation-duration: 1600ms; } }
```

### A11y
- `role="status"` + `aria-label="로딩 중"`, 시각 라벨 없을 때 필수

---

## 5. Progress

진행률이 **있는** 작업(업로드·단계 위저드). 선형 바.

| Property | 값 |
|----------|-----|
| `value` | 0–100 (determinate) / 생략 시 indeterminate |
| `intent` | `primary`(기본) · `success` · `warning` · `danger` |
| `size` | `sm`(4px) · `md`(8px) |

### Tokens
| 영역 | 토큰 |
|------|------|
| 트랙 | `Color/bg/tertiary` |
| 채움 | `Color/bg/interactive/primary` (intent별 `Color/bg/{intent}`) |
| Radius | `border/radius/rounded` |
| 모션 | `width` 트랜지션 `duration/base` + `easing/standard` |

```css
.progress-track { height: 8px; background: var(--color-bg-tertiary); border-radius: var(--radius-rounded); overflow: hidden; }
.progress-fill  { height: 100%; background: var(--color-bg-interactive-primary); border-radius: var(--radius-rounded);
  transition: width var(--motion-duration-base) var(--motion-easing-standard); }
```

### A11y
- `role="progressbar"` + `aria-valuenow/min/max` (determinate)
- indeterminate는 `aria-valuetext="처리 중"`

---

## 6. Empty State

데이터가 없거나 첫 진입 화면. **다음 행동을 유도**하는 게 목적.

```
[Empty State]
├── [Illustration / 라인 아이콘]  (32~48, aria-hidden)
├── [Title]      (Heading/sm)
├── [Description](body/md/regular, text/tertiary)
└── [Primary Action] (선택 — 예: "첫 항목 추가")
```

### Tokens
| 영역 | 토큰 |
|------|------|
| 아이콘 | `Color/icon/tertiary`, size 32~48 (라인) |
| 제목 | `Heading/sm` (`--font-weight-semibold`) |
| 설명 | `body/md/regular` · `Color/text/tertiary` |
| 간격 | 아이콘↔제목 `spacing/12`, 제목↔설명 `spacing/8`, 설명↔버튼 `spacing/16` |

### A11y · Do/Don't
- 일러스트는 `aria-hidden`, 의미는 제목·설명으로
- ✅ 빈 이유 + 해결 행동 함께 제시 · ❌ "데이터 없음"만 덩그러니, ❌ 이모지 일러스트

---

## 7. 공통 Tokens 요약

| 영역 | 토큰 |
|------|------|
| intent 색 | `Color/{bg|text|icon|border}/{info|success|warning|danger}` (+ `*-subtle` 면) |
| 아이콘 | 라인 SVG · `Color/icon/{intent}` (이모지 금지) |
| Radius | `border/radius/md`(Toast·Alert) · `rounded`(Progress) |
| 그림자 | `shadow/lg`(Toast) |
| 모션 | motion.md §5.5(Toast) · §5.7(Skeleton) · `duration/base`+`easing/standard`(Progress) |
| 본문/제목 | `body/md/regular` · `Heading/sm`(`--font-weight-semibold`) |

---

## 8. Do / Don't (공통)

✅ **DO**
- 의미색 + 라인 아이콘 + 텍스트 3중 표시
- 일시 알림은 Toast, 지속 상태는 Inline Alert로 구분
- 0.3초 이내 로딩엔 인디케이터 생략(즉시 표시)
- 모든 피드백에 `prefers-reduced-motion` 대응

❌ **DON'T**
- 색만으로 성공/에러 구분
- **이모지 아이콘**(`✅⚠️🔔`) 사용 — 라인 SVG로 대체
- 중요한 영구 정보를 자동 사라지는 Toast로만 전달
- 스피너 + 스켈레톤 동시 사용
