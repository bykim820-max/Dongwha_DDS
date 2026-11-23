# DDS 시작하기 — 동화Lab

> **Dongwha Design System(DDS)** — 동화 사내 시스템 화면의 공통 규칙. 색 · 간격 · 글자에 붙인 이름(토큰), 컴포넌트를 언제 어떻게 쓰는지, 화면 문구를 어떻게 쓰는지.
> 최종 버전 **v2.6.0** · 2027년부터 유지 모드 → [HANDOVER.md](./HANDOVER.md)

---

## 누가 무엇을 보나

| 나는 | 먼저 볼 것 | 그다음 |
|---|---|---|
| **기획자 · PM · 디자이너** | [guides/index.html](./guides/index.html) — 비개발자 가이드 페이지 | 컴포넌트를 고를 때 `components/` 의 해당 문서 **§0 선택 기준** |
| **개발자** | [dist/tokens.css](./dist/tokens.css) 를 받아 프로젝트에 넣기 → [dist/README.md](./dist/README.md) | [design.md](./design.md) · `components/` · [MIGRATION.md §2.3~2.4](./MIGRATION.md) |
| **AI로 화면을 만드는 사람** | AI에게 [AGENTS.md](./AGENTS.md) · [design.md](./design.md) · 관련 컴포넌트 문서를 첨부하고 "먼저 읽어" | 가이드 페이지 §5 프롬프트 템플릿 |
| **DDS를 맡은 사람** | [HANDOVER.md](./HANDOVER.md) | — |
| **화면 예시를 보고 싶은 사람** | [index.html](./index.html) — 컴포넌트 쇼케이스 (라이트 · 다크) | `examples/` 의 예시 화면 6개 |

---

## 묶음 구성

```
START.md            ← 지금 이 문서
README.md           ← 전체 소개 (GitHub 시절 기준 — 링크 일부는 보관 저장소를 가리킨다)
HANDOVER.md         ← 인계 · 유지 모드 규칙
design.md           ← 설계 원칙 · 제품 문맥 · 금지 규칙 · 로드맵 · 알려진 이슈
AGENTS.md           ← AI가 작업 전에 읽는 규칙
CHANGELOG.md        ← 버전별 변경 + 유지 모드 정정 기록
MIGRATION.md        ← 가져가기 · 버전 올리기
VERSION             ← 2.6.0
index.html          ← 컴포넌트 쇼케이스
guides/             ← 비개발자 가이드 페이지 (index.html)
foundations/        ← 색 · 타이포 · 간격 · 레이아웃 · 모션 · 문구 · 다국어 규칙 + 토큰 원본 JSON
components/         ← 컴포넌트 14종 사양 · 사용 규칙
dist/               ← 토큰 파일 (tokens.css · tokens.resolved.json · tokens.tailwind.js)
examples/           ← 예시 화면 (대시보드 · 레이아웃 · 피드백 · 오버레이 · 다크 · 문구)
scripts/            ← 재개용 — 토큰 빌드 · 하드코딩 검사 (Python)
```

- **HTML 파일은 혼자 열린다.** 토큰 CSS를 파일 안에 넣어 두어서, 동화Lab에서 하나만 열어도 색이 제대로 나온다. 글꼴(Pretendard)은 인터넷에서 받는다 — 막혀 있으면 시스템 글꼴로 보인다.
- **md 문서끼리의 링크**(`./components/button.md` 등)는 폴더 구조가 그대로일 때 동작한다. `[미확인: 동화Lab이 폴더 · 상대 링크를 지원하는지]` — 링크가 안 열리면 파일 이름으로 찾는다.
- **`dist/` 토큰 파일은 고치지 않는다.** 생성 파일이다 → [HANDOVER.md §2](./HANDOVER.md)
