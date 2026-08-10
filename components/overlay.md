# Overlay

> 현재 맥락 위에 **떠서** 작업을 진행시키는 컴포넌트군. 깊이(elevation)로 위계를, 모션으로 등장/퇴장을 표현한다.
> 짧은 도움말은 → [Tooltip](./tooltip.md), 상태 알림은 → [Feedback](./feedback.md).

[← Components](./README.md) · [← design.md](../design.md)

이 문서는 **5개 오버레이**를 묶어 다룬다: Modal · Bottom Sheet · Drawer · Popover · Dropdown Menu.
공통 토큰·모션·접근성을 §1에서 정의하고, 각 컴포넌트는 §2~6에서 차이만 기술한다.

---

## 1. 공통 규칙

### 1.1 스크림(Backdrop)
모달형(포커스를 가두는) 오버레이는 뒤를 **스크림**으로 덮는다.
- 색: `rgba(0,0,0,0.45)` (반투명 뉴트럴). 그라데이션·블러 남용 금지([금지 규칙](../design.md#-디자인-금지-규칙-anti-patterns))
- 등장: `opacity 0→1`, `duration/quick`, `easing/standard`
- 클릭 시 닫힘(파괴적 폼은 예외 — 확인 요구)

### 1.2 깊이 · 모서리
| 요소 | elevation | radius |
|------|-----------|--------|
| Modal | `--elevation-modal` (shadow/lg) | `border/radius/xl`~`2xl` (12~16) |
| Bottom Sheet | `--elevation-modal` | 상단만 `2xl`(16) |
| Drawer | `--elevation-modal` | 0 (화면 끝에 붙음) |
| Popover / Menu | `--elevation-overlay` (shadow/md) | `border/radius/md`~`lg` |

### 1.3 모션 (motion.md 연결)
| 컴포넌트 | 등장 | 퇴장 |
|----------|------|------|
| Modal | `translateY(8~16px)`+페이드, `duration/moderate`, `easing/spring/soft` (§5.4) | `translateY(8px)`+페이드, `duration/quick`, `easing/accelerate` |
| Bottom Sheet | `translateY(100%→0)` + 4~8% 오버슈트, `duration/moderate`, `spring/soft` | `translateY(100%)`, `duration/quick`, `accelerate` |
| Drawer | `translateX(±100%→0)`, `duration/moderate`, `spring/soft` (§5.9) | 반대 방향, `duration/quick` |
| Popover/Menu | `opacity`+`translateY(4px)`, `duration/base` | 페이드, `duration/quick` |

> `prefers-reduced-motion`: transform 제거, **opacity만** 유지.

### 1.4 접근성 (공통 필수)
- **포커스 트랩**: 모달형은 열릴 때 내부로 포커스 이동, Tab이 밖으로 못 나감
- **ESC로 닫기**, 닫히면 **트리거로 포커스 복귀**
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby`(제목)
- 열린 동안 **배경 스크롤 잠금**(body scroll lock)
- 닫기 버튼은 라인 아이콘(✕) + `aria-label="닫기"` (이모지 금지)

---

## 2. Modal (Dialog)

화면 중앙에 떠 작업·확인을 요구. 흐름을 **멈추는** 강한 개입이라 꼭 필요할 때만.

```
[Scrim]
└── [Dialog]  role="dialog" aria-modal
    ├── [Header]  제목(Heading/sm) + 닫기(IconButton)
    ├── [Body]    내용 (스크롤 가능)
    └── [Footer]  보조 액션 · primary 액션(우측)
```

| Property | 값 |
|----------|-----|
| `size` | `sm`(400) · `md`(560) · `lg`(720) |
| `dismissible` | 스크림/ESC로 닫힘 여부 (파괴적 확인은 false) |

```css
.modal { width: min(560px, calc(100vw - var(--space-32)));
  background: var(--color-bg-primary); border-radius: var(--radius-2xl);
  box-shadow: var(--elevation-modal); }
.modal-footer { display: flex; justify-content: flex-end; gap: var(--space-8); }
```

---

## 3. Bottom Sheet

모바일 우선. 화면 하단에서 올라오는 시트. 손가락 동선이 짧아 모바일 액션·선택에 적합.

| Property | 값 |
|----------|-----|
| `detents` | 높이 정착점 (`peek` · `half` · `full`) |
| `grabber` | 상단 핸들(드래그 표시) 유무 |

- 상단 모서리만 `radius/2xl`, 상단에 **grabber**(`bg/tertiary`, 36×4)
- 등장 시 4~8% 오버슈트 후 정착(`spring/soft`)
- 데스크톱에서는 Modal로 대체 가능

```css
.sheet { border-radius: var(--radius-2xl) var(--radius-2xl) 0 0;
  background: var(--color-bg-primary); box-shadow: var(--elevation-modal); }
.sheet .grabber { width: 36px; height: 4px; border-radius: var(--radius-rounded);
  background: var(--color-bg-tertiary); margin: var(--space-8) auto; }
```

---

## 4. Drawer (Side Panel)

좌/우 가장자리에서 슬라이드. 필터·상세·내비 보조에 사용. → 좌측 영구 내비는 [layout.md §3.2 SNB](../foundations/layout.md#32-app-shell--snb-사이드-내비게이션).

| Property | 값 |
|----------|-----|
| `side` | `right`(기본) · `left` |
| `width` | `sm`(320) · `md`(400) · `lg`(480) |

- 화면 끝에 붙어 radius 0, 전체 높이
- 메인 콘텐츠를 반대로 살짝(8px) 밀어 깊이감(선택)

```css
.drawer { position: fixed; top: 0; right: 0; height: 100vh; width: 400px;
  background: var(--color-bg-primary); box-shadow: var(--elevation-modal); }
```

---

## 5. Popover

특정 요소에 **앵커**된 비모달 떠있는 면. 추가 정보·작은 폼. 스크림 없음, 바깥 클릭 시 닫힘.

- `--elevation-overlay`, radius `md`~`lg`, 앵커에 8px 간격
- 화살표(선택)는 [tooltip.md](./tooltip.md) 패턴 재사용
- 포커스 트랩 없음(비모달), ESC로 닫힘

---

## 6. Dropdown Menu

앵커된 **액션 목록**. 버튼/더보기(가로 점 3개)에서 펼침.

```
[Trigger] → [Menu]  role="menu"
            ├── [MenuItem]  라인 아이콘 + 라벨   role="menuitem"
            ├── [Divider]
            └── [MenuItem destructive]  Color/text/danger
```

| 항목 | 토큰 |
|------|------|
| 배경 · 깊이 | `Color/bg/primary` · `--elevation-overlay` |
| hover 항목 | `Color/bg/interactive/secondary-hover` |
| 파괴적 항목 | `Color/text/danger` |
| 아이콘 | 라인 SVG (이모지 금지) |
| 항목 높이 | 36~40 (터치 타깃 ≥44 권장) |

### 키보드
- `↑/↓` 항목 이동, `Enter` 실행, `Esc` 닫기, `Tab` 닫고 다음으로
- `role="menu"` / `role="menuitem"`, 트리거 `aria-haspopup` · `aria-expanded`

---

## 7. 공통 Tokens 요약

| 영역 | 토큰 |
|------|------|
| 표면 | `Color/bg/primary` |
| 스크림 | `rgba(0,0,0,0.45)` |
| 깊이 | `--elevation-modal`(Modal·Sheet·Drawer) · `--elevation-overlay`(Popover·Menu) |
| Radius | `border/radius/{md,lg,xl,2xl}` (요소별 §1.2) |
| 간격 | `--layout-stack-gap`(내부) · `spacing/16~24`(패딩) |
| 모션 | motion.md §5.4(Modal·Sheet) · §5.9(Drawer) |

---

## 8. Do / Don't (공통)

✅ **DO**
- 모달형은 **포커스 트랩 + ESC + 포커스 복귀 + 스크롤 잠금**
- 한 번에 오버레이 **1개**만 (중첩 지양)
- 모바일=Bottom Sheet, 데스크톱=Modal/Popover로 형식 분기
- 닫기는 라인 아이콘 `✕` + `aria-label`

❌ **DON'T**
- 오버레이 위에 또 오버레이 쌓기(스택)
- 스크림에 그라데이션·과한 블러 ([금지 규칙](../design.md#-디자인-금지-규칙-anti-patterns))
- 닫을 방법 없는 모달(ESC·닫기·스크림 중 최소 하나)
- 이모지 닫기 버튼 / 포커스 트랩 없는 모달
