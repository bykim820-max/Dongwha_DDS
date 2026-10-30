# 가져가기 · 갱신하기 (MIGRATION)

> DDS를 **다른 시스템에서 쓰는 쪽**을 위한 문서. 처음 가져갈 때와, 새 버전이 나왔을 때 무엇을 하는지.
> 무엇이 바뀌었는지는 → [CHANGELOG.md](./CHANGELOG.md)

---

## 0. Claude Code를 쓴다면 — 플러그인이 이 문서를 대신 실행한다

아래 2~4장의 절차를 명령 하나로 한다. **기획자·개발자 모두** 이 방법을 권한다.

**팀 전체에 — 프로젝트에 등록 (권장).** 시스템 저장소 담당자가 프로젝트 폴더에서 한 번 실행하고, 생긴 `.claude/settings.json`을 커밋한다. 그 프로젝트를 여는 팀원은 설치를 안내받는다. `/dds:init`이 이 단계도 함께 한다.

```bash
claude plugin marketplace add bykim820-max/Dongwha_DDS --scope project
claude plugin install dds@dongwha-dds --scope project
```

**나만 — 개인 설치.** `--scope project` 없이 같은 두 줄.

```bash
claude plugin marketplace add bykim820-max/Dongwha_DDS
claude plugin install dds@dongwha-dds
```

| 할 일 | 명령 | 이 문서의 해당 절 |
|---|---|---|
| 처음 가져오기 | `/dds:init` | §2 |
| 새 버전 확인 · 영향 분석 | `/dds:check` | §3.1 · §4 |
| 새 버전으로 올리기 | `/dds:upgrade` | §3 · §4 |
| 화면 만들기 | 그냥 요청 — `dds:ui` 스킬이 고정 버전의 규칙을 자동 적용 | — |

자세한 내용 → [plugins/dds/README.md](./plugins/dds/README.md). 플러그인 없이 하려면 아래를 따른다.

---

## 1. 버전 규칙

DDS는 `MAJOR.MINOR.PATCH` 세 자리를 쓴다. **자리마다 해야 할 일이 다르다.**

| 자리 | 언제 올라가나 | 받는 쪽이 할 일 |
|---|---|---|
| **MAJOR** `2.x → 3.0` | 토큰 **이름이 삭제·변경**됨. 컴포넌트 사양이 비호환으로 바뀜 | **코드 수정 필요.** 이 문서의 대응표를 보고 찾아 바꾼다 |
| **MINOR** `2.4 → 2.5` | 토큰·컴포넌트·문서가 **추가**됨. 기존 것은 그대로 | 받기만 하면 된다. 새 토큰은 쓰고 싶을 때 쓴다 |
| **PATCH** `2.5.0 → 2.5.1` | 토큰 **값** 조정(대비 수정 등), 오타, 문서 정정 | 받으면 적용된다. **화면 색이 달라질 수 있으니 확인** |

> ⚠️ **PATCH라도 안심하면 안 되는 경우가 있다.** 문서의 안내가 틀렸다가 고쳐지는 경우,
> 토큰 파일은 그대로라서 **새로 받아도 내 코드는 안 고쳐진다.** CHANGELOG의 ⚠️ **확인 필요** 항목이 그것이다.
> 버전을 올릴 때는 숫자만 보지 말고 CHANGELOG의 ⚠️ 항목을 먼저 읽는다.

---

## 2. 처음 가져가기

### 2.1 무엇을 가져가나

| 파일 | 필요한 경우 |
|---|---|
| `dist/tokens.css` | **필수.** 색·간격·타이포 값이 전부 들어 있는 CSS 변수 파일 |
| `dist/tokens.tailwind.js` | Tailwind를 쓸 때만 |
| `dist/tokens.resolved.json` | AI 에이전트에 토큰 목록을 줄 때, 또는 직접 조회할 때 |

문서(`components/*.md` 등)는 **복사하지 않는다.** 저장소를 보거나 링크로 참조한다 — 복사하면 낡은 문서가 남는다.

### 2.2 버전을 고정해서 받기

태그 주소에서 파일 하나만 받는다. 주소의 `v2.6.0`이 버전 고정이다.

```bash
mkdir -p src/styles/dds
curl -fsSL https://raw.githubusercontent.com/bykim820-max/Dongwha_DDS/v2.6.0/dist/tokens.css -o src/styles/dds/tokens.css
```

어떤 버전이 있는지:

```bash
git ls-remote --tags --refs https://github.com/bykim820-max/Dongwha_DDS.git
```

### 2.3 받은 버전을 기록한다 — **이 단계를 건너뛰지 않는다**

내 프로젝트에 **어떤 버전을 쓰고 있는지 적어 둔다.** 적어 두지 않으면 나중에 "우리가 뭘 쓰고 있지?"를 알 수 없다.

```bash
echo "2.6.0" > src/styles/dds/DDS_VERSION
```

`dist/tokens.css`의 헤더에도 버전이 찍혀 있다 (v2.5.0부터).

```bash
head -3 src/styles/dds/tokens.css
#   DDS v2.6.0 · Design Tokens (생성 파일 — 직접 수정 금지)
```

> **v2.4.0 이전 파일은 헤더가 전부 `v2.0`으로 찍혀 있다.** 내가 가진 게 실제로 몇 버전인지는
> [CHANGELOG의 판별표](./CHANGELOG.md#먼저-읽어주세요--v240-이전-파일의-버전-표기-오류)로 확인한다.

### 2.4 쓰기

```css
/* 1. 토큰 로드 */
@import "./styles/dds/tokens.css";

/* 2. 컴포넌트는 var()로만 참조 — hex·px 직접 쓰지 않는다 */
.btn-primary {
  background: var(--color-bg-interactive-primary);
  padding: var(--space-8) var(--space-16);
  border-radius: var(--radius-md);
}
```

---

## 3. 새 버전으로 올리기

### 3.1 절차

```
1. CHANGELOG.md 에서 "내 버전 → 최신 버전" 사이 항목을 전부 읽는다
       ↓
2. ⚠️ 확인 필요 항목이 있나?
       ├─ 있음 → 4장 대응표대로 코드를 고친다 (파일만 받으면 안 고쳐진다)
       └─ 없음 → 다음
       ↓
3. 변경 항목이 있나? (토큰 값 변화)
       ├─ 있음 → 받은 뒤 해당 색이 쓰인 화면을 눈으로 확인
       └─ 없음 → 다음
       ↓
4. dist/ 파일을 새 버전으로 교체하고 DDS_VERSION 을 갱신한다
       ↓
5. 화면을 열어 확인한다 — 라이트 · 다크 양쪽
```

### 3.2 명령

```bash
curl -fsSL https://raw.githubusercontent.com/bykim820-max/Dongwha_DDS/v2.6.0/dist/tokens.css -o src/styles/dds/tokens.css
echo "2.6.0" > src/styles/dds/DDS_VERSION
```

### 3.3 내 버전과 최신 버전 비교

```bash
cat src/styles/dds/DDS_VERSION                                                    # 내 버전
git ls-remote --tags --refs https://github.com/bykim820-max/Dongwha_DDS.git        # 전체 버전
```

---

## 4. 버전별 대응표

새 버전으로 올릴 때 **코드를 직접 고쳐야 하는 것**만 모았다.

### Input lg 글자 크기 14px → 16px

**해당 버전: v2.6.0 미만 → v2.6.0 이상** · 심각도: 중간 (모바일 화면)

v2.6.0부터 Input `lg`(48px)의 글자가 `body/md`(14px) → `body/lg`(16px)다. 14px 입력칸은 **iOS Safari에서 포커스할 때 화면이 확대**된다.
모바일(768px 미만) 폼은 `lg`를 쓰는 것이 규칙이 됐다 → [input.md §4.1](./components/input.md#41-기본값과-사용처). **토큰 파일은 그대로라 새로 받아도 고쳐지지 않는다.**

| 쓰인 곳 | 이전 | 이후 |
|---|---|---|
| Input `lg` 글자 크기 | `var(--body-md-font-size)` | `var(--body-lg-font-size)` |
| Input `lg` 줄 높이 | `var(--body-md-line-height)` | `var(--body-lg-line-height)` |
| 모바일 폼 입력칸 | `md`(40px) | `lg`(48px) |

**찾기** — `/dds:check`가 이 명령을 실행한다

```bash
grep -rnE '<Input[^>]*size="lg"|input[-_]lg|input--lg' src/ --include="*.css" --include="*.scss" --include="*.vue" --include="*.tsx" --include="*.jsx"
```

나온 곳에서 글자 크기가 `--body-md-font-size`면 `--body-lg-font-size`로 바꾼다. 모바일 미디어 쿼리(`max-width: 767px`) 안의 입력칸이 `md`면 `lg`로 올린다.

**고친 뒤 확인** — 아이폰(또는 Safari 모바일 모드)에서 입력칸을 눌러 화면이 확대되지 않는지 본다.

### 폼 필드 옆 찾기 버튼 xs → md

**해당 버전: v2.6.0 미만 → v2.6.0 이상** · 심각도: 낮음 (높이 어긋남)

v2.6.0 이전 `button.md §4.1`이 폼 필드 옆 보조 액션("찾기")에 `xs`(24px)를 안내했다. 40px 필드 옆에 24px 버튼이 붙어 높이가 어긋난다.
**같은 줄의 Input과 Button은 같은 사이즈를 쓴다** → [button.md §4.1](./components/button.md#41-기본값과-사용처).

| 쓰인 곳 | 이전 | 이후 |
|---|---|---|
| 필드 옆 "찾기" · 우편번호 검색 등 | Button `xs` (24px) | 필드와 같은 사이즈 — 보통 `md` (40px) |

**찾기** — `/dds:check`가 이 명령을 실행한다

```bash
grep -rnE 'size="xs"|btn[-_]xs|btn--xs' src/ --include="*.css" --include="*.scss" --include="*.vue" --include="*.tsx" --include="*.jsx"
```

나온 곳 중 **입력칸 바로 옆**에 있는 버튼만 고친다. 테이블 행 · 칩 옆의 `xs`는 올바른 사용이다.

**고친 뒤 확인** — 입력칸과 버튼의 위아래 선이 맞는지 본다.

### 버튼 배경에 면 토큰을 쓴 경우

**해당 버전: v2.5.0 미만에서 가져간 모든 경우** · 심각도: 높음

v2.5.0 이전 `colors.md §5` 적용 가이드가 버튼 배경으로 **면(배경) 토큰**을 안내하는 오류가 있었다.
그 표를 보고 구현했다면 지금도 틀린 상태다. **토큰 파일은 정상이므로 새로 받아도 고쳐지지 않는다.**

| 쓰인 곳 | 잘못된 토큰 | 올바른 토큰 |
|---|---|---|
| 메인 액션 버튼 배경 | `--color-bg-primary` | `--color-bg-interactive-primary` |
| 보조 버튼 배경 | `--color-bg-secondary` | `--color-bg-interactive-secondary` |

**왜 문제인가**

`--color-bg-primary`는 **페이지 표면 색**이다 — 라이트에서 `#ffffff`, 다크에서 `#262626`.
브랜드 green(`#14bc62`)은 `--color-bg-interactive-primary`다.

보조 버튼 쪽이 더 잘 안 보인다. 라이트 모드에서는 둘 다 `#fafafa`라 **차이가 드러나지 않다가**,
다크 모드에서 면은 `#171717`, 버튼은 `#404040`으로 갈라진다. 면 토큰을 쓴 버튼은 **다크에서 배경에 묻힌다.**
`hover` · `pressed` 토큰은 `interactive/*` 아래에만 있다.

**찾기** — `/dds:check`가 이 명령을 실행한다

```bash
grep -rn "color-bg-primary\|color-bg-secondary" src/ --include="*.css" --include="*.scss" --include="*.vue" --include="*.tsx" --include="*.jsx"
```

버튼이 아닌 곳(페이지·카드·모달 배경)에 쓰였다면 **그건 올바른 사용이다.** 버튼에 쓰인 것만 고친다.

**고친 뒤 확인** — 다크 모드로 전환해 보조 버튼이 배경과 구분되는지 본다.

### 상태색이 어두워진 것

**해당 버전: v2.4.0 미만 → v2.4.0 이상** · 심각도: 낮음 (받으면 자동 적용)

경고·성공·정보·오류 메시지의 글자·아이콘 색과 비활성 색이 **의도적으로 어두워졌다.** WCAG AA 대비를 맞추기 위한 수정이다.
값 목록 → [CHANGELOG v2.4.0](./CHANGELOG.md#240--2026-08-14)

**할 일** — 코드 수정은 없다. 받은 뒤 알럿·토스트·비활성 버튼이 있는 화면을 눈으로 확인한다.
색이 디자인 시안과 달라 보이면, 시안이 아니라 **토큰이 맞다** (시안이 대비 미달이었다).

---

## 5. 새 버전이 나온 걸 어떻게 아나

| 방법 | 내용 |
|---|---|
| **Claude Code 시작 알림** | 플러그인을 설치했다면 자동. DDS를 쓰는 프로젝트에서 Claude Code를 시작할 때 새 버전이 있으면 화면에 뜬다 |
| **`/dds:check`** | Claude Code 플러그인. 내 버전과 최신을 비교하고 올릴 때 할 일까지 알려준다 |
| **GitHub 메일** | 저장소 오른쪽 위 **Watch → Custom → Releases** 체크. 새 버전의 [Release](https://github.com/bykim820-max/Dongwha_DDS/releases)가 올라오면 메일이 온다 (GitHub 계정 필요) |
| **사내 공지** | MAJOR·⚠️ 확인 필요 항목이 있는 버전은 담당자가 메신저로 공지한다 |
| **직접 확인** | `git fetch --tags && git tag -l` |

---

## 6. 자주 묻는 것

**Q. 토큰 값을 우리 시스템에 맞게 바꿔 써도 되나요?**
`tokens.css`를 직접 수정하면 다음 갱신 때 덮어쓰여 사라진다. 별도 파일에서 덮어쓰고, 그 사실을 기록한다.
다만 **값을 바꿔야 할 이유가 생겼다면 DDS에 등록 요청**하는 편이 맞다 — 같은 필요가 다른 시스템에도 있을 가능성이 높다.

**Q. 필요한 토큰이 없으면?**
임의로 만들지 말고 담당자에게 요청한다. 임시로 쓰더라도 `/* DDS 미등록 — 요청됨 */` 주석을 남긴다.

**Q. 문서도 복사해 둘까요?**
하지 않는다. 문서는 자주 고쳐지고, 복사본은 반드시 낡는다. 저장소 링크로 참조한다.

**Q. 버전을 건너뛰어도 되나요?**
된다. 단 **건너뛴 모든 버전의 CHANGELOG를 읽어야 한다.** v2.2 → v2.5라면 2.3·2.4·2.5의 ⚠️ 항목을 전부 확인한다.

---

*문의: 스마트워크팀 김부영*
