# Motion & Interaction

> 모션의 목적은 **사용자 인지 부담을 줄이고 다음 상태로 자연스럽게 연결**하는 것.
> 화려함보다 **신뢰감 있는 절제**가 우선이며, 모든 인터랙션은 손가락/커서가 닿는 순간 즉각 반응해야 한다.

[← design.md](../design.md)

---

## 1. 모션 원칙

| 원칙 | 의미 |
|------|------|
| **Purposeful** (목적성) | 모든 모션은 정보 위계 또는 인과 관계를 설명해야 함. 장식적 모션 금지 |
| **Calm** (절제) | 짧고 부드럽게. 큰 바운스/회전은 핵심 알림에 한정 |
| **Responsive** (즉시성) | 입력 시점 0–80ms 내 시각 피드백 시작 (perceived latency 제거) |
| **Continuous** (연속성) | 사라지는 요소와 등장하는 요소의 위치·크기를 잇는다 (shared transition) |
| **Restraint** (자제) | 한 화면에 동시 모션 5개 이하. 화면 전체가 흔들리지 않게 |
| **Respectful** (접근성) | `prefers-reduced-motion` 시 페이드만 유지 |

---

## 2. Duration 토큰

| 토큰 | ms | 용도 |
|------|----|------|
| `motion/duration/instant` | 80 | 컬러 호버, 작은 토글 색상 변화 |
| `motion/duration/quick` | 160 | 버튼 프레스, 체크박스 체크, 백드롭 페이드 |
| `motion/duration/base` | 240 | 카드 호버 리프트, 토스트, 드롭다운 |
| `motion/duration/moderate` | 320 | 모달/시트 등장, 페이지 내 섹션 전환 |
| `motion/duration/slow` | 480 | 큰 시트 · 풀스크린 · 페이지 전환 |
| `motion/duration/deliberate` | 640 | 환영 · 온보딩 1회성 강조 모션 |

> **700ms 상한**. 더 긴 효과는 stagger로 분할.

---

## 3. Easing 토큰

| 토큰 | cubic-bezier | 사용처 |
|------|--------------|--------|
| `motion/easing/standard` | `cubic-bezier(0.4, 0, 0.2, 1)` | 기본. 일반 트랜지션 |
| `motion/easing/decelerate` *(enter)* | `cubic-bezier(0, 0, 0.2, 1)` | **들어오는** 요소 (등장) |
| `motion/easing/accelerate` *(exit)* | `cubic-bezier(0.4, 0, 1, 1)` | **나가는** 요소 (퇴장) |
| `motion/easing/emphasized` | `cubic-bezier(0.2, 0, 0, 1)` | 중요한 상태 변화 강조 |
| `motion/easing/spring/soft` | `cubic-bezier(0.32, 0.72, 0, 1)` | 시트·모달·카드 탭 (부드러운 정착) |
| `motion/easing/spring/snappy` | `cubic-bezier(0.5, 1.25, 0.5, 1)` | 작은 토글·세그먼트 (살짝 튐) |

---

## 4. CSS 변수 설정

```css
:root {
  /* Durations */
  --motion-duration-instant:    80ms;
  --motion-duration-quick:      160ms;
  --motion-duration-base:       240ms;
  --motion-duration-moderate:   320ms;
  --motion-duration-slow:       480ms;
  --motion-duration-deliberate: 640ms;

  /* Easings */
  --motion-easing-standard:      cubic-bezier(0.4, 0, 0.2, 1);
  --motion-easing-decelerate:    cubic-bezier(0, 0, 0.2, 1);
  --motion-easing-accelerate:    cubic-bezier(0.4, 0, 1, 1);
  --motion-easing-emphasized:    cubic-bezier(0.2, 0, 0, 1);
  --motion-easing-spring-soft:   cubic-bezier(0.32, 0.72, 0, 1);
  --motion-easing-spring-snappy: cubic-bezier(0.5, 1.25, 0.5, 1);
}
```

---

## 5. 인터랙션 레시피

### 5.1 Tap / Press — 모든 클릭 가능 요소

```css
.interactive {
  transition:
    transform        var(--motion-duration-instant) var(--motion-easing-standard),
    background-color var(--motion-duration-instant) var(--motion-easing-standard),
    box-shadow       var(--motion-duration-quick)   var(--motion-easing-standard);
}
.interactive:active { transform: scale(0.97); }
```

- 누르는 순간 **0.97 스케일** 축소 (대형 카드는 0.99)
- 해제 시 spring/snappy로 복귀
- 키보드 활성(Enter/Space)에도 동일 피드백

### 5.2 Hover Lift — 카드 / 리스트 아이템

```css
.card {
  transition:
    transform  var(--motion-duration-base) var(--motion-easing-standard),
    box-shadow var(--motion-duration-base) var(--motion-easing-standard);
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}
.card:hover .card-image {
  transform: scale(1.04);
}
```

- Y축 **2–4px** 부상 + 그림자 한 단계 상승
- 내부 이미지가 있다면 `scale(1.04)` 허용 (overflow: hidden 필수)

### 5.3 Focus Ring

```css
:focus-visible {
  outline: 2px solid var(--color-border-info);
  outline-offset: 2px;
  transition: outline-offset var(--motion-duration-quick) var(--motion-easing-standard);
}
```

- **키보드 포커스만** 표시 (`:focus-visible`)
- 등장 시 offset 0 → 2px 애니메이션으로 "정착감" 부여

### 5.4 Sheet / Modal 등장

| 단계 | 모션 |
|------|------|
| 백드롭 | `opacity 0→1`, duration/quick, easing/standard |
| 컨테이너 (데스크톱) | `translateY(8–16px)` + `opacity 0→1`, duration/moderate, easing/spring/soft |
| 컨테이너 (모바일 바텀시트) | `translateY(100% → 0)` + 4–8% 오버슈트 후 정착, duration/moderate, easing/spring/soft |
| 닫힘 | `translateY(8px)` + `opacity 1→0`, duration/quick, easing/accelerate |

### 5.5 Toast / Snackbar

- 등장: 아래에서 위로 16px 슬라이드 + 페이드인 (duration/base, easing/decelerate)
- 자동 닫힘 **4초**, 호버 시 일시정지
- 닫힘: 위로 8px + 페이드아웃 (duration/quick, easing/accelerate)

### 5.6 List Stagger — 목록 첫 진입

- 항목당 **40ms** 지연 누적, **최대 6개**까지만 stagger
- 각 항목: `opacity 0→1`, `translateY(8px → 0)`
- 7번째부터는 한 번에 등장 (성능)

### 5.7 Skeleton → Content

- 스켈레톤 펄스: **1200ms**, ease-in-out, 무한
- 콘텐츠 도착 시: 스켈레톤 fade-out 120ms ↔ 콘텐츠 fade-in 200ms (중첩 80ms)
- **레이아웃 시프트 금지** — 스켈레톤 크기 = 실제 콘텐츠 크기

### 5.8 Number / Count-Up

- 금액·통계 숫자는 **0 → 목표값** 카운트업 (duration/moderate, easing/decelerate)
- 천 단위 콤마는 종료 시점에 한꺼번에 표시
- 폼 인풋의 실시간 계산값은 카운트업 없이 즉시 갱신

### 5.9 Drawer / Navigation 전환

- 좌측 드로어: `translateX(-100% → 0)`, duration/moderate, easing/spring/soft
- 백드롭 동시 페이드인
- 메인 콘텐츠는 반대 방향으로 8px 밀어 **깊이감** 부여

### 5.10 Tab / Segmented Indicator

- 인디케이터(언더라인 또는 필 배경)는 **X 위치만** 트랜지션
- duration/base + easing/emphasized
- 콘텐츠 영역은 fade 100ms로 간결히 교체

---

## 6. Shadow Elevation (모션과 결합)

| 토큰 | 사용 | 동반 모션 |
|------|------|-----------|
| `shadow/sm` | 정적 카드 기본 | — |
| `shadow/md` | 호버 카드, 작은 팝오버 | hover 시 sm → md |
| `shadow/lg` | 모달, 큰 시트 | enter 시 0 → lg |
| `shadow/xl` | 풀스크린 오버레이 | — |

---

## 7. 햅틱 / 사운드 (네이티브 · PWA)

| 트리거 | 강도 |
|--------|------|
| 토글 ON/OFF, 체크 | Light |
| 결제 완료, 큰 액션 성공 | Medium + 단일 펄스 |
| 에러 · 검증 실패 | Notification: Error |

웹에서는 `navigator.vibrate(10)` 대체(지원 브라우저 한정).

---

## 8. 접근성 — Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

- `transform` · `scale` 제거, **opacity만** 유지
- 자동 재생 캐러셀 정지
- Skeleton 펄스도 정적으로

---

## 9. 성능 가이드

| 항목 | 권장 |
|------|------|
| 애니메이션 속성 | `transform`, `opacity`만. `width/height/top/left` **금지** |
| `will-change` | 트리거 직전에 set, 종료 후 제거 |
| 동시 모션 수 | 한 화면 5개 이하 |
| 프레임 | 모바일 미드티어에서 60fps, jank ≤ 1프레임 |

---

## 10. LLM 모션 적용 우선순위

코드 생성 시 다음 순서로 자동 적용:

1. 모든 인터랙티브 요소 → **§5.1 Tap/Press**
2. 카드·리스트 아이템 → **§5.2 Hover Lift**
3. 모든 `:focus-visible` → **§5.3 Focus Ring**
4. 모달·시트·토스트 → **§5.4–5.5**
5. §5.6–5.10은 디자인에 명시될 때만 추가
6. **§8 Reduced Motion 미디어쿼리는 항상 포함**
