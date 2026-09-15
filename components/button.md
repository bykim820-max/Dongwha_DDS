# Button

> 사용자가 취할 수 있는 액션을 표현. 폼 제출 · 작업 시작 · 페이지 이동 등.

[← Components](./README.md) · [← design.md](../design.md)

이 문서는 **사양(무엇인가)** 과 **문법(언제 · 어디에 · 어떻게 쓰는가)** 을 함께 다룬다.
문구 자체는 [writing.md §4](../foundations/writing.md), 번역 시 폭 변화는 [i18n.md §3](../foundations/i18n.md)이 원본이며 여기서는 링크만 한다.

---

## 0. 선택 기준 — 버튼인가, 아닌가

| 사용자가 하려는 것 | 쓰는 것 | 시맨틱 | 이유 |
|---|---|---|---|
| **작업을 실행** — 저장 · 삭제 · 제출 · 모달 열기 | **Button** | `<button>` | 현재 화면의 상태를 바꾼다 |
| **다른 페이지로 이동** — 상세 보기 · 목록으로 · 외부 링크 | **링크** | `<a href>` | URL이 바뀐다. 새 탭 · 주소 복사 · 뒤로가기가 동작해야 한다 |
| 이동인데 **버튼처럼 보여야** 함 — 헤더의 "새 주문"(작성 페이지로) | `<a>` + Button 스타일 | `<a class="btn">` | 시맨틱은 이동, 시각은 액션 |
| 실행인데 **문장 속에 들어감** — "이미 계정이 있나요? **로그인**" | Button `link` variant | `<button>` | 인라인 텍스트 액션. 이동이면 `<a>` |
| 공간이 없는 **반복 액션** — 테이블 행의 편집 · 삭제, 툴바 | **Icon Button** → [§8](#8-icon-button) | `<button aria-label>` | 라벨 대신 아이콘 + `aria-label` + 툴팁 |
| 액션이 **4개 이상** 몰림 | 대표 1~3개 + **메뉴**(`···`) → [overlay.md](./overlay.md) | `<button aria-haspopup>` | 헤더 · 행 액션 과밀 방지 |
| 여러 값 중 **하나를 고름** — 일별 / 주별 / 월별 | [Segmented Control](./navigation.md) | `radiogroup` | 선택이지 실행이 아니다 |
| 설정을 **켜고 끔** | [Switch](./switch.md) | `role="switch"` | 즉시 반영되는 상태 |
| 콘텐츠 **패널 전환** | [Tabs](./navigation.md) | `tablist` | 내비게이션이다 |

**판별 질문 하나 — "누르면 URL이 바뀌는가?"** 바뀌면 `<a>`, 안 바뀌면 `<button>`. 모달을 여는 것은 URL이 안 바뀌므로 버튼이다.

`<div onClick>` · `<span onClick>`은 어느 경우에도 쓰지 않는다 (→ [§10](#10-accessibility)).

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

### 3.1 variant 결정 절차

한 화면(또는 한 영역)의 버튼은 **위계를 먼저 정한 뒤** variant를 배정한다. 색부터 고르지 않는다.

```
1. 이 영역에서 사용자가 "끝내야 하는 일"은 무엇인가?   → 그 하나만 primary
2. 그 일을 돕거나 대안이 되는 액션은?                  → secondary
3. 취소 · 닫기 · 뒤로처럼 흐름을 빠져나가는 액션은?      → tertiary
4. 되돌릴 수 없는 파괴적 액션은?                       → danger (확인 다이얼로그 안에서만, §3.3)
5. 문장 속에서 이어지는 액션은?                        → link
```

| 헷갈리는 쌍 | 구분 |
|---|---|
| `secondary` vs `outline` | **secondary가 기본.** outline은 색 면(`bg/secondary`)이 배경과 붙어 안 보이는 곳 — 틴트 배경(`*-subtle`) 위 · 카드 안 · 이미지 위 — 에서만 쓴다. 한 영역에 둘을 섞지 않는다 |
| `tertiary` vs `link` | tertiary는 **버튼 크기 · 패딩을 유지**한 채 배경만 없다 → 버튼 스택 안에 놓인다. link는 **텍스트 흐름 안**에 들어간다 → 문장 · 테이블 셀 · 헬퍼 텍스트 |
| `primary` vs `danger` | danger는 primary의 "빨간 버전"이 아니다. **확인 다이얼로그의 실행 버튼 자리에서만** primary를 대신한다 |

### 3.2 primary는 화면당 1개 — 원칙과 예외

**원칙.** 한 화면(뷰포트에 함께 보이는 영역)에 `primary`는 1개. 사용자가 "다음에 뭘 누르지"를 고민하지 않게 한다.

**허용되는 예외** — 아래 경우만. 코드 주석에 이유를 남긴다.

| 상황 | 허용 | 조건 |
|---|---|---|
| 긴 폼의 **상단 헤더와 하단 푸터에 같은 "저장"** 반복 | ✅ | **같은 액션**의 반복이어야 한다. 서로 다른 액션 2개는 ❌ |
| 모달이 열려 있을 때 **뒤 페이지의 primary** | ✅ | 스크림이 덮으므로 한 시점에 보이는 primary는 1개 |
| 빈 상태(Empty State)의 **"첫 항목 만들기"** | ✅ | 이 시점 화면의 유일한 할 일. 헤더의 "새로 만들기"와 **같은 액션**이면 헤더 쪽을 secondary로 내린다 |
| 위저드(다단계)의 **"이전"과 "다음"** | 다음만 | 이전은 tertiary. 마지막 단계는 "완료"가 primary |
| **동급 선택지 2개** — "임시 저장" vs "제출" | ❌ | 최종 액션(제출)만 primary, 임시 저장은 secondary |
| 리스트의 **각 카드 / 행마다** primary | ❌ | 행 액션은 tertiary · Icon Button · 메뉴. 행이 아니라 **선택 후 일괄 액션**을 primary로 |

### 3.3 danger 사용 규칙

- **페이지 본문에 danger를 바로 노출하지 않는다.** 목록 · 상세의 "삭제"는 `tertiary` 또는 `outline` + 휴지통 아이콘으로 두고, 클릭하면 **확인 다이얼로그**([writing.md §7](../foundations/writing.md))가 열리며 그 안의 실행 버튼이 `danger`다.
- 예외: 해당 화면의 **유일한 목적이 삭제**인 경우(예: "계정 삭제" 설정 페이지)는 본문에 danger를 둘 수 있다. 이때도 확인 단계는 생략하지 않는다.
- danger 라벨은 대상을 밝힌다: `삭제` → `주문 3건 삭제` ([writing.md §4.1](../foundations/writing.md)).
- 되돌릴 수 있는 삭제(휴지통 · 보관)는 danger가 아니다 → secondary + 실행 후 "실행 취소" Toast ([feedback.md](./feedback.md)).

---

## 4. Size

| 사이즈 | 높이 | 패딩 좌우 | Text Style | 아이콘 크기 | Figma |
|--------|------|-----------|------------|-------------|-------|
| `xs` | 24px | `spacing/8` | `body/sm/medium` | 12 | `btn_s_default` |
| `sm` | 32px | `spacing/12` | `body/sm/medium` | 16 | `button` (Small) |
| `md` | 40px | `spacing/16` | `body/md/medium` | 16 | `button` (Medium, default) |
| `lg` | 48px | `spacing/16` | `body/md/medium` | 20 | `button_48px` |

### 4.1 기본값과 사용처

**`md`(40px)가 기본이다.** 다른 사이즈는 아래 상황에서만 쓴다. 한 영역(스택 · 툴바 · 푸터) 안의 버튼은 **모두 같은 사이즈**다.

| 사이즈 | 쓰는 곳 | 쓰지 않는 곳 |
|---|---|---|
| `lg` 48 | 모바일 풀폭 CTA · 로그인 / 시작처럼 **화면에 버튼이 하나뿐인** 단독 액션 | 데스크톱 폼 푸터 · 헤더 (md와 섞이면 위계가 흔들린다) |
| `md` 40 | **기본.** 페이지 헤더 · 폼 푸터 · 모달 푸터 · 빈 상태 · 카드 액션 | — |
| `sm` 32 | 테이블 툴바(필터 · 내보내기) · 카드 헤더의 보조 액션 · 인라인 편집 확정 / 취소 · 밀도 높은 데이터 화면 | 화면의 primary (작은 primary는 위계를 잃는다) |
| `xs` 24 | 테이블 **행 안의** 텍스트 액션 · 칩 / 태그 옆 · 폼 필드 옆 보조 액션("찾기") | 단독 배치. 터치 타깃 44px을 클릭 영역 확장으로 반드시 확보 ([§10](#10-accessibility)) |

- 모바일(`md` 브레이크포인트 미만)에서는 폼 · 모달 푸터 버튼을 **풀폭 `lg`로 승격**하고 세로 스택한다 (§9.1).
- **사이즈를 바꿔 강조하지 않는다.** 강조는 variant로, 크기는 배치 맥락으로 정한다.

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

/* 이유 설명이 필요 없는 비활성 — 호버 · 포커스 · 클릭 모두 차단 */
.btn:disabled {
  background: var(--color-bg-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
  pointer-events: none;
}
/* 이유를 툴팁으로 설명해야 하는 비활성 — 호버 · 포커스는 유지, 클릭만 핸들러에서 무시 (§5.1) */
.btn[aria-disabled="true"] {
  background: var(--color-bg-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}
.btn[data-loading="true"] { pointer-events: none; }
```

### 5.1 disabled — 언제 허용하는가

**기본은 "비활성화하지 않는다."** 사용자가 누르게 두고 안 되는 이유를 인라인 오류로 보여주는 편이 낫다. disabled는 이유를 말하지 못하고, 스크린리더가 건너뛴다.

| 상황 | 처리 |
|---|---|
| 폼 필수값 미입력 | ❌ disabled 금지. **활성 유지** → 클릭 시 해당 필드에 인라인 오류 + 포커스 이동 ([input.md](./input.md)) |
| 권한 없음 | ✅ `aria-disabled` + **툴팁으로 이유** ("승인 권한이 없습니다") → [tooltip.md](./tooltip.md). 아예 숨기지 않는다 — 기능이 존재함은 알려야 한다 |
| 선택 항목 0개인 일괄 액션 ("선택 삭제") | ✅ disabled. 라벨에 개수 표시 권장 ("선택 삭제 (0)") |
| 처리 중 | disabled가 아니라 **loading** (§5.2). 둘을 동시에 쓰지 않는다 |
| 이전 단계 미완료 (위저드) | ✅ disabled. 단계 표시로 이유가 드러나면 툴팁 생략 가능 |
| 요금제 · 기능 제한 | ✅ `aria-disabled` + 툴팁 또는 배지 |

- `disabled` 속성은 호버 · 포커스를 받지 못해 **툴팁이 뜨지 않는다.** 이유를 설명해야 하면 `aria-disabled="true"`를 쓰고 `onClick`에서 무시한다 (§5 CSS 참조).

### 5.2 loading — 처리 중 표시 규칙

| 항목 | 규칙 |
|---|---|
| 라벨 | 진행형으로 바꾼다: `저장` → `저장 중…` ([writing.md §4.1](../foundations/writing.md)). `…`는 U+2026 하나 |
| 스피너 | **Leading Icon 자리**에 사이즈 표의 아이콘 크기로. 기존 leading 아이콘이 있으면 스피너로 교체 |
| 폭 | 라벨이 바뀌어도 **버튼 폭이 흔들리지 않게** `min-width`를 원래 라벨 폭 이상으로 유지. 스피너가 라벨을 대체하지 않는다 (Icon Button은 예외) |
| 같은 스택의 다른 버튼 | **취소는 활성 유지** (중단할 수 있어야 한다). 단, 취소가 실제로 요청을 중단시키지 못하면 취소도 disabled |
| 중복 클릭 | `pointer-events: none` + `aria-busy="true"`. `disabled`는 쓰지 않는다 (포커스 유지) |
| 3초 초과 | 버튼 로딩만으로 부족하다. 진행률([feedback.md Progress](./feedback.md)) 또는 결과를 Toast로 비동기 알림 |
| 완료 후 | 원래 라벨로 복귀. 성공은 Toast로 ([feedback.md](./feedback.md)). 버튼 자체를 "완료됨"으로 바꾸지 않는다 |

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
| 배경 | `Color/bg/{primary|secondary|danger|disabled}` |
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

### 8.1 사용 기준

- 아이콘만으로 뜻이 **관습적으로 명확한 액션**에만: 닫기(✕) · 편집(연필) · 삭제(휴지통) · 더 보기(···) · 검색 · 새로고침 · 즐겨찾기.
- 그 외는 **라벨 있는 버튼**. "내보내기" · "승인" · "동기화"는 아이콘만으로 전달되지 않는다.
- 쓰는 곳: 테이블 **행 액션** · 툴바 · 카드 헤더 · 모달 닫기 · 페이지 헤더의 부가 액션.
- **툴팁 필수**(마우스) + `aria-label` 필수(스크린리더) → [tooltip.md](./tooltip.md). 둘의 문구는 같다.
- 한 행에 Icon Button은 **3개까지.** 넘으면 메뉴(`···`)로 접는다.
- 화면의 **primary 액션을 Icon Button으로 만들지 않는다.**

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
- 방향: `row`(기본) · `column` (모바일 풀폭)
- 모바일 풀폭: 세로 스택 + 풀폭 버튼

### 9.1 순서 규칙

**실행이 오른쪽, 빠져나가기가 왼쪽.** 읽기 방향의 끝에 "다음으로 가는" 액션이 온다.

```
[tertiary: 취소]  [secondary: 임시 저장]  [primary: 저장]      ← 데스크톱, align="end"
```

- 오른쪽 끝 = primary (또는 확인 다이얼로그의 danger). 그 왼쪽 = secondary. 가장 왼쪽 = tertiary(취소 · 닫기 · 뒤로).
- **한 스택에 3개까지.** 넘치면 메뉴로 접거나 화면을 나눈다.
- 파괴적 액션이 스택에 같이 있으면 **다른 버튼과 떨어뜨린다**: `align="between"`으로 삭제를 왼쪽 끝에, 나머지를 오른쪽에.
- **모바일(세로 스택)**: primary가 **맨 위**, 취소가 맨 아래. 엄지 도달 순서가 아니라 **시선 순서**를 따른다. 전부 `fullWidth` + `lg`.

```
데스크톱                          모바일
[취소] [임시 저장] [저장]    →     [     저장      ]
                                  [   임시 저장    ]
                                  [     취소      ]
```

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

## 11. 라벨 · 아이콘

### 11.1 라벨 — 길이와 넘침

문구 자체는 [writing.md §4](../foundations/writing.md)(동사 · 대상 명시 · 표준 라벨 표). 여기서는 **길이와 넘침**만 다룬다.

| 규칙 | 내용 |
|---|---|
| 길이 | 한국어 **2~6자 권장, 12자 상한** ([writing.md §3.3](../foundations/writing.md)). 영문은 **3단어 이내** |
| 줄바꿈 | **금지.** `white-space: nowrap`. 두 줄 버튼은 없다 |
| 말줄임 | **금지.** 잘린 라벨은 뜻이 사라진다. 넘치면 라벨을 줄이거나(`거래처 정보 저장` → `저장`) Icon Button으로 바꾼다 |
| 폭 | `width` 고정 금지, `min-width` + 패딩으로만 ([i18n.md §3](../foundations/i18n.md)). 2자 라벨은 영문에서 +28~80% 늘어난다 — `취소` → `Cancel` |
| 풀폭 | `fullWidth`는 모바일 세로 스택 · 단독 CTA에서만. 데스크톱 스택에서 풀폭 금지 |
| 대소문자 (영문) | Sentence case — `Save changes`, ❌ `Save Changes` ([i18n.md §6](../foundations/i18n.md)) |

### 11.2 아이콘

**아이콘 없는 버튼이 기본이다.** 아이콘은 라벨을 돕지, 대신하지 않는다.

| 위치 | 언제 | 예 |
|---|---|---|
| Leading (좌) | 액션의 **종류**를 한눈에 — 추가 · 삭제 · 내보내기 · 업로드 | `[+] 새 주문` · `[↓] 내보내기` |
| Trailing (우) | **방향 · 펼침 · 외부 이동**만 | `다음 [→]` · `옵션 [⌄]` · `도움말 [↗]` |
| 둘 다 | ❌ 금지 | — |

- 아이콘은 라인 SVG 한 세트, `stroke="currentColor"` ([icons.md](./icons.md)). 이모지 금지 ([design.md 금지 규칙 1](../design.md#-디자인-금지-규칙-anti-patterns)).
- 같은 스택 안에서 **일부만 아이콘**을 달지 않는다 — primary에만 달거나, 전부 없거나.
- 아이콘 크기는 §4 사이즈 표를 따르고, 라벨과의 갭은 `spacing/4`(sm 이하) · `spacing/8`(md 이상).

---

## 12. 배치 — 어디에 어떤 버튼이 오는가

위치가 정해지면 variant · size · 정렬이 따라온다.

| 위치 | 정렬 | 사이즈 | 구성 | 참조 |
|---|---|---|---|---|
| **페이지 헤더** | 우측 | `md` | primary 1 + secondary 0~2 + 메뉴. **가장 중요한 것이 가장 우측** | [page-header.md](./page-header.md) |
| **폼 하단** | 우측 (`end`) | `md` | `[취소] [저장]`. 긴 폼은 하단 **sticky 푸터** | — |
| **모달 푸터** | 우측 (`end`) | `md` | `[취소] [실행]`. 확인 다이얼로그는 실행이 `danger` | [overlay.md](./overlay.md) · [writing.md §7](../foundations/writing.md) |
| **바텀 시트 (모바일)** | 세로 풀폭 | `lg` | primary 위, 취소 아래 | [overlay.md](./overlay.md) |
| **테이블 툴바** | 좌: 필터 · 검색 / 우: 액션 | `sm` | 우측에 `[내보내기] [+ 새 항목]`. 행 선택 시 **일괄 액션 바**로 교체 | [table.md](./table.md) |
| **테이블 행** | 우측 끝 컬럼 | `sm` Icon Button | 편집 · 삭제 · 더 보기 **3개까지**, 넘으면 메뉴 | [table.md](./table.md) · §8.1 |
| **카드** | 하단 우측 또는 헤더 우측 | `sm` | tertiary · link 위주. **카드마다 primary 금지** (§3.2) | — |
| **빈 상태** | 중앙 | `md` | primary 1개("첫 거래처 등록") + 선택적 link("가져오기") | [feedback.md Empty State](./feedback.md) |
| **인라인 편집** | 필드 바로 우측 | `sm` | `[취소] [저장]` 또는 Icon Button ✕ · ✓ | [input.md](./input.md) |
| **Toast 안** | 문구 우측 | `sm` link / tertiary | 액션 1개만("실행 취소") | [feedback.md](./feedback.md) |

- **같은 종류의 화면은 같은 자리.** 목록 화면의 "새로 만들기"는 항상 헤더 우측이다. 화면마다 옮기지 않는다 ([design.md 제품 문맥 — 예측 가능성](../design.md)).
- 한 화면에 버튼이 놓이는 영역이 **셋을 넘으면** 화면이 너무 많은 일을 한다. 분리를 검토한다.

---

## 13. Do / Don't

✅ **DO**
- 페이지당 `primary` 1개 — 예외는 §3.2의 표에 있는 경우만
- "URL이 바뀌면 `<a>`, 아니면 `<button>`" (§0)
- 액션 동사로 명명 ("저장", "주문 3건 삭제", "결제하기") → [writing.md §4](../foundations/writing.md)
- 위험한 액션은 확인 다이얼로그 안에서만 `danger` (§3.3)
- 사이즈는 `md` 기본, 한 영역 안에서는 하나의 사이즈 (§4.1)
- 실행은 오른쪽 · 빠져나가기는 왼쪽, 모바일은 primary 맨 위 (§9.1)
- 비활성 이유는 툴팁으로 — 폼 미입력은 비활성 대신 인라인 오류 (§5.1)
- 로딩 중 라벨은 진행형, 폭 유지, 취소는 활성 (§5.2)

❌ **DON'T**
- 한 행 · 한 영역에 primary 여러 개 · 카드 / 행마다 primary
- "확인", "OK", "예" 같은 모호한 라벨
- 라벨 줄바꿈 · 말줄임 — 넘치면 라벨을 줄인다 (§11.1)
- `width` 고정 — 영문에서 잘린다
- 페이지 본문에 `danger` 직접 노출
- 아이콘을 좌우 양쪽에 · 스택 안 일부만 아이콘
- 이모지 아이콘
- `<div onClick>`
- 임의 padding / border-radius 인라인
- 크기를 키워서 강조 — 강조는 variant로

---

## 14. Examples

```tsx
// 1. 기본 저장
<Button variant="primary">저장</Button>

// 2. 아이콘 + 라벨
<Button variant="secondary" iconBefore={<Plus />}>새로 만들기</Button>

// 3. 로딩 중
<Button variant="primary" loading>처리 중…</Button>

// 4. 위험 액션 — 확인 다이얼로그 안
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

// 8. 이동은 <a> — 버튼처럼 보여도 (§0)
<a className="btn" data-variant="primary" href="/orders/new">새 주문</a>

// 9. 목록의 삭제 — 본문은 tertiary, 확인 다이얼로그 안에서 danger (§3.3)
<Button variant="tertiary" iconBefore={<Trash />} onClick={openConfirm}>삭제</Button>
// → 다이얼로그 푸터: [취소] [주문 3건 삭제]  ← 여기서 danger

// 10. 권한 없음 — 숨기지 않고 비활성 + 이유 (§5.1)
<Tooltip content="승인 권한이 없습니다">
  <Button variant="primary" aria-disabled="true" onClick={noop}>승인</Button>
</Tooltip>

// 11. 일괄 액션 — 선택 0개면 비활성, 개수 표시 (§5.1)
<Button variant="secondary" disabled={selected.length === 0}>
  선택 삭제 ({selected.length})
</Button>

// 12. 모바일 세로 스택 — primary 맨 위 (§9.1)
<ButtonStack direction="column">
  <Button variant="primary" size="lg" fullWidth>저장</Button>
  <Button variant="tertiary" size="lg" fullWidth>취소</Button>
</ButtonStack>

// 13. 파괴적 액션을 스택에서 분리 (§9.1)
<ButtonStack align="between">
  <Button variant="tertiary" iconBefore={<Trash />}>삭제</Button>
  <ButtonStack gap="12">
    <Button variant="tertiary">취소</Button>
    <Button variant="primary">저장</Button>
  </ButtonStack>
</ButtonStack>
```
