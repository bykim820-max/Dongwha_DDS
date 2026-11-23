# DDS 사용법

> **Dongwha Design System(DDS)** — 동화 사내 시스템 화면의 공통 규칙. 색 · 간격 · 글자에 붙인 이름(토큰), 화면 부품을 언제 어떻게 쓰는지, 화면 문구를 어떻게 쓰는지.
> 최종 버전 **v2.6.0** · 2027년부터 유지 모드 (새 규칙을 추가하지 않는다) → 맡은 사람은 [HANDOVER.md](./HANDOVER.md)

**하려는 일을 고르세요.**

| 하려는 일 | 바로 가기 |
|---|---|
| AI로 화면을 만든다 | [1. AI로 화면 만들기](#1-ai로-화면-만들기) |
| 개발 중인 시스템에 DDS 색 · 간격을 넣는다 | [2. 개발자 — 토큰 넣기](#2-개발자--토큰-넣기) |
| 기획서 · 화면 정의서 · 시안을 쓴다 | [3. 기획 · 디자인](#3-기획--디자인) |

---

## 1. AI로 화면 만들기

가장 쉬운 방법이다. AI에게 **DDS 문서를 같이 주기만 하면** 색 · 버튼 · 문구 규칙을 따라 만든다. 문서를 안 주면 AI는 그럴듯한 색을 지어내고, 브랜드 색 · 다크 모드 · 문구 규칙을 지키지 않는다 (2026-11 비교 시연: 같은 요청에서 규칙 위반 20건 → 0건).

### ① 첨부할 파일

| 항상 | 만들 화면에 따라 추가 |
|---|---|
| `AGENTS.md` — AI가 지킬 규칙 | 버튼이 있으면 `components/button.md` |
| `design.md` — 어떤 제품을 위한 규칙인지 | 입력칸 · 폼이면 `components/input.md` |
| `dist/tokens.css` — 실제 색 · 간격 값 | 문구가 있으면 `foundations/writing.md` |
| | 표 · 목록이면 `components/table.md`, 팝업이면 `components/overlay.md` |

### ② 요청 문구 — 복사해서 `[ ]`만 채우기

```
첨부한 DDS 문서(AGENTS.md)를 먼저 읽고, 그 규칙대로 아래 화면을 만들어줘.

■ 화면: [거래처 등록]
■ 유형: [목록 / 상세 / 등록·수정 폼 / 대시보드]
■ 들어갈 것: [필드 · 열 · 버튼을 나열]
■ 상태: [빈 화면 · 오류 · 로딩 중 보여줄 것]

제약:
- 색 · 간격은 tokens.css의 토큰 이름만 쓰고, 색상 코드나 px를 직접 쓰지 말 것
- 초록(primary) 버튼은 화면에 1개
- 버튼은 동사로, "확인 / 예 / OK" 금지
- 문서에 없는 판단은 지어내지 말고 [미확인: 무엇]으로 표시

끝나면 알려줘: 사용한 부품 / 초록 버튼 개수 / [미확인] 목록
```

"예쁘게 · 깔끔하게" 같은 말은 넣지 않는다 — AI가 자기 취향으로 채운다. 화면마다 더 자세한 템플릿은 [가이드 페이지 §5.3](./guides/index.html#s5-3).

### ③ 결과 5분 검수

- [ ] 초록 버튼이 1개인가
- [ ] 색 · 간격이 `var(--…)` 이름으로 쓰였는가 — `#14bc62`, `13px` 같은 값이 보이면 다시 요청
- [ ] 이모지 아이콘이 없는가
- [ ] 버튼이 동사인가 ("확인 · 예 · OK" 없음)
- [ ] `[미확인]` 목록이 있는가 — 있으면 AI 잘못이 아니라 **문서에 답이 없는 것**이다. [HANDOVER.md §5.3](./HANDOVER.md)에 한 줄 남긴다

> **Claude Code를 쓰는 개발자라면** — 이미 DDS 플러그인(`/dds:init`)을 설치한 프로젝트는 첨부 없이 그냥 요청해도 규칙이 적용된다. 새로 설치하는 것은 GitHub 보관 저장소가 남아 있는 동안만 된다 → [HANDOVER.md §1.2](./HANDOVER.md)

---

## 2. 개발자 — 토큰 넣기

### ① 파일 받기

동화Lab의 `dist/` 폴더에서 받는다.

| 파일 | 필요한 경우 |
|---|---|
| `tokens.css` | **필수** — 색 · 간격 · 글자 크기 · 라이트/다크가 모두 들어 있는 CSS 변수 파일 |
| `tokens.tailwind.js` | Tailwind를 쓸 때 |
| `tokens.resolved.json` | 토큰 이름 → 값 목록이 필요할 때 (AI 첨부용으로도 쓸 수 있다) |

### ② 넣고 버전 적기

```bash
mkdir -p src/styles/dds
cp tokens.css src/styles/dds/tokens.css        # 동화Lab에서 받은 파일
echo "2.6.0" > src/styles/dds/DDS_VERSION       # 어떤 버전인지 꼭 적어 둔다
```

### ③ 쓰기

```css
@import "./styles/dds/tokens.css";

.btn-primary {
  background: var(--color-bg-interactive-primary);   /* 색은 이름으로 */
  padding: var(--space-8) var(--space-16);           /* 간격도 이름으로 */
  border-radius: var(--radius-md);
}
```

```js
// Tailwind
module.exports = { presets: [require('./src/styles/dds/tokens.tailwind.js')] }
```

- 다크 모드는 자동이다 — OS 설정을 따르고, `<html data-theme="dark">`로 강제할 수 있다
- **받은 `tokens.css`를 고치지 않는다.** 바꿔야 할 값이 있으면 별도 파일에서 덮어쓰고 그 사실을 적어 둔다
- 어떤 토큰을 어디에 쓰는지: [design.md](./design.md) · [foundations/colors.md](./foundations/colors.md) · 부품별 [components/](./components/README.md)
- 알려진 문제(다크 모드 Toast 등)는 [design.md 끝 "알려진 이슈"](./design.md)를 먼저 본다

---

## 3. 기획 · 디자인

| 하려는 일 | 볼 것 |
|---|---|
| 이 자리에 어떤 부품을 쓸지 | [가이드 페이지](./guides/index.html) §1.0 표 → 해당 부품 문서의 **§0 선택 기준** |
| 화면 정의서 · 시안에 스타일 적기 | 가이드 페이지 §1.6 · §1.7 · §1.8 · §2.4 — 복사 버튼이 달린 템플릿 |
| 버튼 · 오류 · 안내 문구 쓰기 | 가이드 페이지 §3 · [foundations/writing.md](./foundations/writing.md) |
| 넘기기 전 점검 | 가이드 페이지 §4.2 — 5분 체크리스트 |
| Figma에서 그리기 | 라이브러리 `2026_DDS_v2_배포용` — 색 변수는 2026-11 정정본. Tabs · Segmented · Breadcrumb는 라이브러리에 없으니 문서 사양대로 그린다 |
| 실제 화면 예시 보기 | [index.html](./index.html) — 부품 쇼케이스 (라이트 · 다크), `examples/` — 예시 화면 6개 |

---

## 묶음 구성

```
START.md            ← 지금 이 문서 (사용법)
HANDOVER.md         ← 맡은 사람용 — 유지 모드 규칙 · 자주 올 문의 · 미결 과제
README.md           ← 전체 소개 (GitHub 시절 기준 — 링크 일부는 보관 저장소를 가리킨다)
design.md           ← 설계 원칙 · 제품 문맥 · 금지 규칙 · 알려진 이슈
AGENTS.md           ← AI가 작업 전에 읽는 규칙
CHANGELOG.md        ← 버전별 변경 + 유지 모드 정정 기록
MIGRATION.md        ← 버전 올리기 · 버전별 대응표
VERSION             ← 2.6.0
index.html          ← 부품 쇼케이스
guides/             ← 기획자 · 디자이너용 가이드 페이지 (index.html)
foundations/        ← 색 · 글자 · 간격 · 레이아웃 · 모션 · 문구 · 다국어 규칙 + 토큰 원본 JSON
components/         ← 부품 14종 사양 · 사용 규칙
dist/               ← 토큰 파일 (tokens.css · tokens.resolved.json · tokens.tailwind.js)
examples/           ← 예시 화면 (대시보드 · 레이아웃 · 피드백 · 오버레이 · 다크 · 문구)
scripts/            ← 재개용 — 토큰 빌드 · 하드코딩 검사 (Python)
```

- **HTML 파일은 혼자 열린다.** 토큰 CSS가 파일 안에 들어 있다. 글꼴(Pretendard)은 인터넷에서 받는다 — 막혀 있으면 시스템 글꼴로 보인다
- **md 문서끼리의 링크**는 폴더 구조가 그대로일 때 동작한다. `[미확인: 동화Lab이 폴더 · 상대 링크를 지원하는지]` — 안 열리면 파일 이름으로 찾는다
