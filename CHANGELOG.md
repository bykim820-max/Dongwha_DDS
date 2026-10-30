# 변경 이력 (CHANGELOG)

> DDS의 모든 버전과 변경 내용. **가져다 쓰는 쪽에서 무엇을 해야 하는지**를 기준으로 적는다.
> 갱신 방법 → [MIGRATION.md](./MIGRATION.md) · 토큰 사용법 → [dist/README.md](./dist/README.md)

각 버전은 세 가지로 나눈다.

| 표시 | 뜻 | 소비자가 할 일 |
|---|---|---|
| **추가** | 새 토큰·컴포넌트·문서. 기존 것은 그대로 | 받기만 하면 됨 |
| **변경** | 기존 토큰의 **값**이 달라짐 (이름은 유지) | 받으면 적용됨. **화면 색이 달라질 수 있으니 확인** |
| ⚠️ **확인 필요** | 받는 것만으로는 안 고쳐짐 | **직접 코드를 고쳐야 함.** [MIGRATION.md](./MIGRATION.md) 참조 |

---

## 먼저 읽어주세요 — v2.4.0 이전 파일의 버전 표기 오류

**v2.5.0 이전에 배포된 `dist/tokens.css`는 내용과 무관하게 헤더가 전부 `DDS v2.0`으로 찍혀 있었습니다.**
빌드 스크립트에 버전이 하드코딩돼 있었기 때문입니다. 따라서 **"v2.0"이라는 같은 이름표를 단 서로 다른 파일이 5가지** 유통됐습니다.

| 가지고 계신 파일에 있는 것 | 실제 버전 |
|---|---|
| `--topbar-h` 있음 + `--color-text-warning: #806108` | **v2.4.0** (또는 v2.5.0) |
| `--topbar-h` 있음 + `--color-text-warning: #e0b20f` | **v2.2.0 ~ v2.3.0** |
| `--topbar-h` 없음 + `prefers-color-scheme` 블록 있음 | **v2.1.0** |
| `dist/tokens.css` 파일 자체가 없음 | **v2.0.0** — 이 버전에는 토큰 파일이 없습니다 |

> 버전 태그 `v2.0.0` ~ `v2.4.0`은 2026-10-14에 **소급해서** 붙였습니다. 당시 릴리스된 적은 없고, 각 버전이 완성된 시점의 커밋을 가리킵니다.

v2.5.0부터 헤더에 실제 버전이 찍힙니다. 아래처럼 확인하세요.

```bash
head -3 dist/tokens.css
```

---

## [2.6.0] — 2026-10-30

Input 문법 단계. 입력칸을 "언제 · 어디에 · 어떻게" 쓰는지 정했다.

**추가**
- `input.md` 문법 보강 (213 → 327줄) — §0 선택 기준(입력 vs 선택, `readOnly` vs `disabled`), §2.1 라벨 · 텍스트 길이와 넘침, §4.1 사이즈 기본값과 사용처, §5.1 검증 시점, §5.2 로딩 표시, §11 배치
- 입력 규칙 확정 — 필수 표시는 `*` 하나 · 검색 실시간 반영은 입력 멈춘 뒤 300ms(`Enter` 즉시) · 모달 본문에 스크롤이 생기면 페이지 폼으로 · 필드 사이 간격 `--layout-block-gap`(24)
- 컴포넌트 문서 템플릿에 `0. 선택 기준` 추가 (`components/README.md`)
- 알려진 이슈 등록 — Select · Textarea · Date Picker 문서 부재. 그 전까지 네이티브 요소에 Input의 States · Tokens 적용

> 플러그인 `dds` 1.0.1(2026-10-15, 팀 전체 설치 — `/dds:init`이 프로젝트 설정에 플러그인 등록)은 이 버전 이전에 이미 배포됐다. 플러그인 버전은 DDS 버전과 별개다.

**변경**
- 없음 (토큰 값 변화 없음)

⚠️ **확인 필요**
- **Input `lg` 글자 크기 14px → 16px.** `lg`의 Text Style이 `body/md` → `body/lg`로 바뀌었다. 14px 입력칸은 iOS Safari에서 포커스할 때 화면이 확대된다. 모바일 폼은 `lg`를 쓰는 것이 규칙이 됐다.
  **토큰 파일은 바뀌지 않았으므로 파일을 새로 받아도 고쳐지지 않는다.**
  → [MIGRATION.md](./MIGRATION.md#input-lg-글자-크기-14px--16px)
- **폼 필드 옆 "찾기" 버튼 `xs`(24px) → `md`(40px).** 이전 `button.md §4.1`이 필드 옆 보조 액션에 `xs`를 안내해 40px 필드 옆에 24px 버튼이 붙어 높이가 어긋났다. 같은 줄의 Input과 Button은 같은 사이즈를 쓴다.
  → [MIGRATION.md](./MIGRATION.md#폼-필드-옆-찾기-버튼-xs--md)

---

## [2.5.0] — 2026-10-14

문법·문맥 단계. 문서가 "무엇인가"만 말하고 "언제·어디에 쓰는가"를 말하지 않던 공백을 메웠다.

**추가**
- **버전 체계** — `VERSION` 파일 단일 출처, `dist/` 헤더에 실제 버전 주입, `CHANGELOG.md`·`MIGRATION.md`, 버전 태그
- **Claude Code 플러그인 `dds`** — `/dds:init` · `/dds:check` · `/dds:upgrade` + `dds:ui` 스킬 + **새 버전 시작 알림**. 저장소가 마켓플레이스를 겸한다 (`plugins/dds/`)
- `AGENTS.md` + `CLAUDE.md` — AI 에이전트 진입점 (읽는 순서·절대 규칙·검증 절차)
- `design.md § 제품 문맥` — 어떤 제품·사용자·업무를 위한 시스템인지
- `button.md` 문법 보강 (216 → 452줄) — §0 선택 기준, variant 결정 절차, primary 1개 예외, 배치 표
- 비개발자 가이드에 컴포넌트 라우팅 · Button · **AI에게 화면 요청하는 법**(§5) 추가
- index 쇼케이스에 Writing 섹션 · 리뷰 체크리스트 카드

**변경**
- 없음 (토큰 값 변화 없음)

⚠️ **확인 필요**
- **메인 액션 버튼 배경 토큰 안내 오류 정정.** `colors.md §5` 적용 가이드가 버튼 배경으로
  `Color/bg/primary`(= 페이지 표면, 흰색)를 안내하고 있었다. 올바른 값은 `Color/bg/interactive/primary`(브랜드 green).
  보조 버튼도 `Color/bg/secondary`(면) → `Color/bg/interactive/secondary`.
  **토큰 파일은 바뀌지 않았으므로 파일을 새로 받아도 고쳐지지 않는다.** 코드를 직접 확인해야 한다.
  → [MIGRATION.md](./MIGRATION.md#버튼-배경에-면-토큰을-쓴-경우)

---

## [2.4.0] — 2026-08-14

거버넌스 1단계. 접근성 대비 미달 수정.

**추가**
- 하드코딩 검사 CI (`scripts/check_hardcoding.py` + `.github/workflows/validate.yml`)
- 비개발자 선적용 가이드 (`guides/non-developer-guide.md`)
- UX 라이팅 리뷰 체크리스트 (`foundations/writing-checklist.md`)

**변경** — ⚠️ **상태색·비활성색 값이 달라졌습니다. 화면에 반영됩니다.**

| 토큰 | 이전 | 이후 | 이유 |
|---|---|---|---|
| `--color-text-warning` · `--color-icon-warning` | `#e0b20f` | `#806108` | 흰 배경 대비 1.99:1 → 5.78:1 |
| `--color-text-success` · `--color-icon-success` | `#14bc62` | `#0c8048` | 2.5:1 → 5.0:1 |
| `--color-text-info` · `--color-icon-info` | `#196ce8` | `#0f4aa8` | 대비 강화 |
| `--color-text-danger` · `--color-icon-danger` | `#f51a1a` | `#a71010` | 대비 강화 |
| `--color-bg-disabled` | `#a3a3a3` | `#e5e5e5` | 면과 글자가 같은 값이라 비활성 글자가 안 보이던 문제 |
| `--color-text-disabled` | `#525252` | `#737373` | 〃 |

> 상태 메시지·알럿·비활성 버튼의 색이 **의도적으로 어두워졌습니다.** 디자인 변경이 아니라 WCAG AA 충족을 위한 수정입니다.

---

## [2.3.0] — 2026-08-10

**추가**
- 내비게이션 컴포넌트 사양 — Tabs · Segmented Control · Breadcrumb (`components/navigation.md`)
- index 쇼케이스 Navigation 섹션

> Figma 라이브러리 게시 전 **코드 우선 정의**. `componentKey` 미발급 상태.

---

## [2.2.0] — 2026-08-10

**추가**
- UX 라이팅 가이드 (`foundations/writing.md`) — 보이스·톤, 버튼/오류/안내 문구 규칙, 용어 사전
- 다국어 i18n 규범 (`foundations/i18n.md`) — 문자열 키, 확장률, ICU 복수형, 한↔영 용어 대응
- `--topbar-h` 토큰 + layout.md Topbar 규격
- 거래처 관리 라이팅 샘플 (`examples/writing.html`)

---

## [2.1.0] — 2026-06-19

**`dist/tokens.css`가 처음 생긴 버전.** 이전에는 토큰 파일이 없었다.

**추가**
- **토큰 빌드 파이프라인** (`scripts/build_tokens.py` → `dist/`) — tokens.css · tokens.resolved.json · Tailwind preset
- **다크 모드** — semantic 다크 토큰 + `[data-theme="dark"]` · `prefers-color-scheme` 자동
- Layout · Elevation 파운데이션, Accent/Chart 컬러, 타이포 굵기 축
- Skeleton · Feedback · Overlay 컴포넌트
- 디자인 금지 규칙 (이모지 아이콘 · 장식 그라데이션 · 맹목적 고밀도)

---

## [2.0.0] — 2026-06-19

**문서만 있는 버전. `dist/` 폴더가 존재하지 않는다.**

**추가**
- 3-레이어 토큰 아키텍처 (Primitive → Semantic → Component)
- W3C Design Tokens 형식 export (`foundations/DDS_tokens_w3c.json`)
- 기본 컴포넌트 카탈로그
- 오타 정정 — `netural` → `neutral`, `transpaernt` → `transparent`, `Interctive` → `Interactive`

---

*버전 번호 규칙 → [MIGRATION.md § 버전 규칙](./MIGRATION.md#버전-규칙)*
