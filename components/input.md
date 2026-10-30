# Input / Text Field

> 사용자가 텍스트를 입력하는 폼 컨트롤.

[← Components](./README.md) · [← design.md](../design.md)

이 문서는 **사양(무엇인가)** 과 **문법(언제 · 어디에 · 어떻게 쓰는가)** 을 함께 다룬다.
라벨 · Helper · Placeholder 문구는 [writing.md §6](../foundations/writing.md), 오류 문구는 [writing.md §5](../foundations/writing.md)가 원본이며 여기서는 링크만 한다.

---

## 0. 선택 기준 — 입력인가, 선택인가

| 사용자가 하려는 것 | 쓰는 것 | 시맨틱 | 이유 |
|---|---|---|---|
| **한 줄 자유 텍스트를 씀** — 이름 · 제목 · 거래처명 | **Input** `type="text"` | `<input>` | 값을 사용자가 새로 만든다 |
| **형식이 정해진 값을 씀** — 이메일 · 전화 · URL | **Input** `type="email"` · `tel` · `url` | `<input>` + `autocomplete` | 모바일 키보드 · 자동완성 · 브라우저 기본 검증이 따라온다 |
| **계산하지 않는 숫자를 씀** — 사번 · 우편번호 · 사업자번호 · 주문번호 | **Input** `type="text"` + `inputmode="numeric"` | `<input>` | `type="number"`는 앞자리 0을 지우고, 휠 스크롤로 값이 바뀌고, 하이픈을 받지 않는다 |
| **여러 줄 텍스트를 씀** — 사유 · 비고 · 설명 | Textarea `[미확인: 컴포넌트 부재 — Textarea]` | `<textarea>` | 한 줄 Input에 문단을 받으면 내용을 검토할 수 없다. 문서가 생기기 전까지 이 문서의 States · Tokens를 그대로 적용한다 |
| 정해진 값 중 **하나를 고름** — 2~4개 | [Option Group](./option-group.md) (radio) | `radiogroup` | 선택지가 한눈에 보인다 |
| 정해진 값 중 **하나를 고름** — 5개 이상 | Select `[미확인: 컴포넌트 부재 — Select]` | `<select>` | [option-group.md §9](./option-group.md) · [navigation.md](./navigation.md)가 이미 Select를 가리킨다. 문서가 생기기 전까지 네이티브 `<select>`에 이 문서의 States · Tokens를 적용한다 |
| **날짜 · 기간을 지정** | Date Picker `[미확인: 컴포넌트 부재 — Date Picker]` | `<input type="date">` | 형식(`2026-10-29` · `10/29`)을 사용자가 맞히게 하지 않는다. 문서가 생기기 전까지 네이티브 `type="date"`를 쓴다 |
| **목록을 검색 · 필터** | **Input** `type="search"` + 검색 아이콘 | `<input type="search">` | 테이블 툴바 좌측 → [button.md §12](./button.md#12-배치--어디에-어떤-버튼이-오는가) · [table.md](./table.md) |
| 설정을 **켜고 끔** | [Switch](./switch.md) | `role="switch"` | 즉시 반영되는 상태다. 텍스트 입력이 아니다 |
| 동의 · 여러 개 **체크** | [Checkbox](./checkbox.md) | `checkbox` | — |
| **보기만** 함 — 수정 불가 값 | 폼 안: Input `readOnly` / 상세 화면: 일반 텍스트 | `<input readonly>` · `<dl>` | 폼에서는 값이 함께 제출되고 복사할 수 있어야 한다. 상세 화면에 테두리 친 상자를 늘어놓지 않는다 |

**판별 질문 하나 — "값을 사용자가 새로 만드는가, 정해진 것 중에서 고르는가?"** 만들면 Input(한 줄) · Textarea(여러 줄), 고르면 Option Group · Select. 값이 정해져 있는데 Input으로 받으면 오타가 데이터가 된다.

**Dropdown Menu는 값 선택에 쓰지 않는다.** [overlay.md §6](./overlay.md#6-dropdown-menu)의 Dropdown Menu는 **액션 목록**(`role="menu"`)이다. 값을 고르는 것은 Select다 — 생김새가 비슷해도 시맨틱이 다르다.

**`readOnly`와 `disabled`를 구분한다.**

| | `readOnly` | `disabled` |
|---|---|---|
| 뜻 | 값은 유효하다. 여기서 바꿀 수 없을 뿐 | 지금은 해당 없다 |
| 폼 제출 | 포함된다 | **빠진다** |
| 포커스 · 복사 | 된다 | 안 된다 |
| 예 | 회원 ID · 등록일 · 자동 계산된 합계 | "직접 입력"을 고르기 전의 기타 사유 칸 |

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

### 2.1 라벨 · 텍스트 — 길이와 넘침

문구 자체는 [writing.md §6](../foundations/writing.md#6-안내--상태-문구)(Helper · Placeholder)와 [§5](../foundations/writing.md#5-오류-메시지)(오류). 여기서는 **길이와 넘침**만 다룬다.

| 요소 | 길이 ([writing.md §3.3](../foundations/writing.md#33-길이)) | 넘칠 때 |
|---|---|---|
| **라벨** | 2~8자 권장, **15자 상한**. 명사구, 마침표 없음 | 줄바꿈 허용 (2줄까지). **말줄임 금지** — 라벨은 필드의 접근성 이름이라 잘리면 뜻이 사라진다. 2줄을 넘으면 라벨을 줄이고 설명은 Helper로 옮긴다 |
| **Helper** | 1문장, 40자 | 줄바꿈. 말줄임 금지 |
| **오류** | 1~2문장, 60자 | 줄바꿈. 말줄임 금지. 오류가 Helper를 **대체**한다 (둘을 동시에 쌓지 않는다) |
| **Placeholder** | 예시 값만 | 잘려도 되는 정보만 넣는다. 입력하면 사라지므로 조건 · 규칙은 Helper로 |
| **입력 값** | — | 한 줄 안에서 가로 스크롤 (브라우저 기본). 긴 값이 예상되면 필드 폭을 늘리거나 Textarea (§0) |

- 라벨 위치는 **위** (§9). 좌측 라벨은 영문 번역 시 라벨 폭이 늘어 필드 시작선이 흔들린다 ([i18n.md §3](../foundations/i18n.md#3-문자열-확장--레이아웃)).
- **시각 라벨 생략은 테이블 툴바 검색 하나만.** 검색 아이콘 + `aria-label`로 이름을 준다 (§8). 그 외 필드는 시각 라벨 필수.
- 필수 표시는 라벨 뒤 `*`(`Color/text/danger`) + `required`. **표시는 필수 쪽에만 한다** — 선택 항목에 "(선택)"을 붙이는 방식과 섞지 않는다. 사내 업무 폼은 필수가 대부분이어도 같은 규칙을 쓴다 (화면마다 표시 방식이 바뀌면 예측할 수 없다).
- 영문 라벨은 Sentence case — `Business number`, ❌ `Business Number` ([i18n.md §6](../foundations/i18n.md#6-톤의-언어별-차이)).

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
| `lg` | 48px | `spacing/16` | `body/lg/regular` |

### 4.1 기본값과 사용처

**`md`(40px)가 기본이다.** 높이는 [button.md §4](./button.md#4-size)의 같은 이름 사이즈와 같다 — 같은 줄에 놓이는 Input과 Button은 **같은 사이즈 이름**을 쓴다. 한 폼 안의 필드는 **모두 같은 사이즈**다.

| 사이즈 | 쓰는 곳 | 쓰지 않는 곳 |
|---|---|---|
| `lg` 48 | 모바일(`md` 브레이크포인트 미만) 폼 · 로그인처럼 **필드가 1~2개뿐인** 단독 화면 | 데스크톱 등록 · 수정 폼 (필드가 많으면 화면이 길어진다) |
| `md` 40 | **기본.** 등록 · 수정 폼 · 모달 폼 · 필터 패널 | — |
| `sm` 32 | 테이블 툴바의 검색 · 필터(옆 버튼도 `sm`) · 테이블 셀 인라인 편집 · `compact` 밀도 화면 | 등록 · 수정 폼의 본 필드 |

- 모바일에서는 폼 필드를 **`lg`로 승격**한다. `md` 40px은 터치 타깃 44px([layout.md §6](../foundations/layout.md#6-터치-타깃--정렬))에 못 미친다. 폼 푸터 버튼도 같이 `lg`가 된다 ([button.md §4.1](./button.md#41-기본값과-사용처)).
- `lg`만 글자가 `body/lg`(16px)다. iOS Safari는 16px 미만 입력에 포커스하면 화면을 확대하므로, 모바일 폼은 반드시 `lg`를 쓴다. `sm` · `md`는 데스크톱 전용이라 `body/md`(14px)를 유지한다.
- **사이즈를 바꿔 강조하지 않는다.** 중요한 필드는 순서(앞쪽)와 필수 표시로 알린다.

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
  font: var(--body-md-font-weight) var(--body-md-font-size)/var(--body-md-line-height) var(--font-body);
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

### 5.1 검증 — 언제 오류를 보여주는가

**조건은 Helper로 먼저, 오류는 나중에** ([writing.md §6.1](../foundations/writing.md#61-규칙)). 입력 중인 사람에게 오류를 들이밀지 않는다.

| 시점 | 처리 |
|---|---|
| **입력 중** (처음 입력하는 필드) | 검증하지 않는다. 오류 표시 없음 |
| **포커스가 떠날 때** (blur) | 형식 검증 (이메일 · 자릿수 · 범위). 틀리면 필드 오류 표시. **비어 있는 필수 필드는 blur에서 오류를 띄우지 않는다** — 탭으로 지나간 것뿐이다 |
| **이미 오류인 필드를 고치는 중** | 입력할 때마다 다시 검증해 **고치는 즉시 오류를 지운다** |
| **제출할 때** | 모든 필드 검증 (빈 필수 포함). 오류 필드마다 필드 오류 + 오류가 **2개 이상이면** 폼 상단 Inline Alert로 요약 + **첫 오류 필드로 포커스** ([writing.md §5.2](../foundations/writing.md#52-3계층-배치)). 제출 버튼은 비활성화하지 않는다 ([button.md §5.1](./button.md#51-disabled--언제-허용하는가)) |
| **서버가 거절할 때** | 해당 필드에 매핑할 수 있으면 필드 오류로, 없으면 폼 상단 Inline Alert로. Toast 단독 금지 |

- **`success` 상태는 서버 확인을 통과했을 때만** 쓴다 (아이디 중복 확인 · 사업자번호 조회). 형식만 맞은 필드를 초록으로 칠하지 않는다 — 모든 필드가 초록이면 신호가 사라진다.
- 오류 문구는 그 필드만 고치는 **짧은 지시** — [무슨 일] + [어떻게] ([writing.md §5.1](../foundations/writing.md#51-3요소-구조)). "필수 항목입니다"보다 "이메일을 입력해 주세요".
- 오류는 보더 + 라인 아이콘 + 텍스트 3중 표시 (§9).

### 5.2 loading — 처리 중 표시 규칙

| 상황 | 처리 |
|---|---|
| **비동기 확인** — 중복 확인 · 사업자번호 조회 | Trailing Icon 자리에 Spinner `sm`(16). Helper를 진행형으로: "확인하는 중…". **0.3초 이상**일 때만 표시 ([feedback.md §4](./feedback.md#4-spinner)). 필드는 계속 편집 가능 — 값이 바뀌면 이전 요청 결과는 버린다 |
| **수정 폼의 기존 값 불러오기** | 필드 자리에 [Skeleton](./skeleton.md). 빈 필드를 먼저 보여 줬다가 값을 채우지 않는다 (입력하던 중 덮어쓰기) |
| **제출 중** | 버튼이 loading을 맡는다 ([button.md §5.2](./button.md#52-loading--처리-중-표시-규칙)). 필드를 `disabled`로 바꾸지 않는다 — 값이 제출에서 빠지고 포커스를 잃는다 |
| **검색 · 필터 실시간 반영** | 입력이 멈추고 **300ms 뒤** 요청, `Enter`는 즉시 요청. 응답이 느린 대량 데이터 화면은 실시간 반영 없이 `Enter`로만 검색한다. 결과 영역에 로딩을 표시하고 Input 자체에는 Spinner를 넣지 않는다 |

- 로딩 중인 필드에는 `aria-busy="true"`, 결과 Helper에는 `aria-live="polite"`.

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

---

## 11. 배치 — 어디에 어떤 필드가 오는가

위치가 정해지면 사이즈 · 라벨 · 폭이 따라온다.

| 위치 | 사이즈 | 라벨 | 폭 · 열 | 참조 |
|---|---|---|---|---|
| **등록 · 수정 폼 (페이지)** | `md` | 위 | 컨테이너 `--container-prose`(680). **1열 기본** | [layout.md §3](../foundations/layout.md#3-container-최대폭) · 푸터 버튼 [button.md §12](./button.md#12-배치--어디에-어떤-버튼이-오는가) |
| **모달 폼** | `md` | 위 | 1열. 모달은 흐름을 멈추는 개입이라 짧은 폼만 담는다. **모달 본문에 스크롤이 생기면 페이지 폼으로 옮긴다** | [overlay.md §2](./overlay.md#2-modal-dialog) |
| **테이블 툴바 검색** | `sm` | 생략 + `aria-label` (§2.1) | 툴바 좌측. 옆 필터 · 버튼도 `sm` | [table.md](./table.md) |
| **필터 패널** | `md` | 위 | 1열 | — |
| **테이블 셀 인라인 편집** | `sm` | 생략 + `aria-label`(열 헤더명) | 셀 폭 그대로. 우측 `[취소] [저장]` `sm` | [button.md §12](./button.md#12-배치--어디에-어떤-버튼이-오는가) |
| **모바일 (`md` 미만)** | `lg` (§4.1) | 위 | 풀폭 1열 | — |
| **상세 화면** | 쓰지 않는다 | — | 값은 텍스트로 (§0) | — |

- **같은 줄에 두 필드는 의미상 한 쌍일 때만** — 시작일 · 종료일, 우편번호 · 찾기 버튼. 관련 없는 필드를 공간이 남는다고 나란히 두지 않는다 (시선이 지그재그가 된다).
- **필드 폭은 들어갈 값의 길이를 알린다.** 우편번호 · 사번 · 수량은 짧게(`col-3` 안팎), 주소 · 거래처명은 길게. 모든 필드를 같은 풀폭으로 늘이지 않는다 ([layout.md §4](../foundations/layout.md#4-grid-12컬럼)).
- **관련 필드는 묶는다** — `<fieldset>` + `<legend>`, 묶음 사이는 테두리가 아니라 여백으로 ([layout.md §1](../foundations/layout.md#1-원칙)).
- **필드와 필드 사이는 `--layout-block-gap`(24).** 필드 하나(라벨 + 인풋 + 헬퍼)를 한 블록으로 본다. 라벨 ↔ 인풋(4~8) · 인풋 ↔ 헬퍼(4)보다 확실히 넓어야 어느 헬퍼가 어느 필드 것인지 읽힌다 (§7 · [layout.md §2](../foundations/layout.md#2-간격-리듬-3단계)).
- **같은 종류의 화면은 같은 자리.** 목록 화면의 검색은 항상 툴바 좌측이다 ([design.md 제품 문맥 — 예측 가능성](../design.md)).
