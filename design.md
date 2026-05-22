# Dongwha Design System (DDS) v2.0

> 동화 디자인시스템 v2.0의 단일 진실 소스(SSOT).
> AI 에이전트와 사람이 모두 읽기 좋은 구조로 정리한 디자인 가이드.

---

## 📚 문서 구조

### Foundations (디자인 토큰)

| 문서 | 내용 |
|------|------|
| [Colors](./foundations/colors.md) | Primitive · Semantic 컬러 토큰, 32-슬롯 매트릭스 |
| [Typography](./foundations/typography.md) | Heading · Body 스케일, Pretendard, Letter Spacing |
| [Spacing](./foundations/spacing.md) | 8pt 그리드, `spacing/0` ~ `spacing/64` |
| [Radius](./foundations/radius.md) | `border/radius/sm` ~ `rounded` |
| [State](./foundations/state.md) | default · hover · focus · disabled · error · loading |
| [Motion](./foundations/motion.md) | Duration · Easing · 인터랙션 레시피 10종 |
| **토큰 export** (`DDS_tokens.w3c.json`) | W3C Design Tokens 형식. Primitive 참조 구조 적용, 기계 판독용 SSOT |

### Components

| 카테고리 | 문서 |
|----------|------|
| Actions | [Button](./components/button.md) (Icon Button · Button Stack 포함) |
| Form Inputs | [Input](./components/input.md) · [Switch](./components/switch.md) · [Checkbox](./components/checkbox.md) · [Option Group](./components/option-group.md) |
| Feedback & Overlay | [Tooltip](./components/tooltip.md) |
| Data Display | [Table](./components/table.md) |
| Layout | [Page Header](./components/page-header.md) |
| Foundation | [Icon System](./components/icons.md) |

📋 전체 카탈로그 및 `componentKey` 인덱스 → [components/README.md](./components/README.md)

---

## 🎯 디자인 철학

DDS는 **3-레이어 토큰 아키텍처**를 갖는다.

```
Primitive  →  Semantic   →  Component
(원시 값)     (의미 매핑)    (변형/상태)
```

- **Primitive**: 컬러 램프(50–900), 원시 수치. **직접 참조 금지**.
- **Semantic**: 의미 기반 토큰 (`Color/bg/primary`, `spacing/16`). 모든 UI는 여기를 거친다.
- **Component**: 컴포넌트의 변형(Variant)·상태(State) 정의.

---

## 🔧 코드 매핑 핵심 규칙

1. **컬러는 hex 인라인 금지** → Semantic 토큰만 사용
2. **간격은 `spacing/*` 토큰만**, 임의 px 금지
3. **모서리는 `border/radius/*` 토큰만**
4. **타이포는 Text Style** (`Heading/lg`, `body/md/regular`)을 클래스/유틸로 매핑
5. **상태는 표준 셀렉터** (`:hover`, `:focus-visible`, `:disabled`, `[data-state]`)
6. **모션은 항상** `prefers-reduced-motion` 미디어쿼리 포함
7. **컴포넌트는 라이브러리 인스턴스 = 코드 컴포넌트 1:1**

---

## 🤖 LLM 에이전트 변환 워크플로우

Figma → 코드 변환 시 다음 순서를 따른다.

```
1. 컴포넌트 식별   — 인스턴스 이름 → 컴포넌트 카탈로그 매핑
2. 변형 매핑       — Variant props → React/Vue props
3. 토큰 추출       — Figma 변수 → Semantic 토큰명
4. 상태 정의       — foundations/state.md 기준 셀렉터 작성
5. 타이포 적용     — Text Style 이름 → 클래스 매핑
6. 모션 적용       — foundations/motion.md §9 우선순위 따르기
7. 검증           — 임의 px/hex 잔존 여부 확인
```

### Figma MCP 호출 매핑

| 작업 | MCP 도구 |
|------|----------|
| 페이지 구조 파악 | `get_metadata` |
| 변수 값 추출 | `get_variable_defs` (노드 선택 필요) |
| 토큰/컴포넌트 검색 | `search_design_system` |
| 코드 생성 컨텍스트 | `get_design_context` |

---

## 📦 소스 메타

| 항목 | 값 |
|------|----|
| Figma 파일 | `2026_DDS_v2_배포용` |
| File Key | `tDGeNJRNR2vCZu5bVdmoNc` |
| 라이브러리 키 | `lk-c82741c9eb3cfc2addd0404224304df5d65a7036ad1f38eeac26f7e660286d91e1723437ace74f6d2a826e6755a0744aa5d72288b5a47a47ff789573d602ab7c` |
| 페이지 ID | `5001:88244` (DDS ver.2.0) |
| 폰트 | Pretendard |
| 모드 | Light (Dark는 Phase 2) |

🔗 [Figma 파일 열기](https://www.figma.com/design/tDGeNJRNR2vCZu5bVdmoNc/2026_DDS_v2_%EB%B0%B0%ED%8F%AC%EC%9A%A9)

---

## 🗺 로드맵

- 🔜 **다크 모드** — 2026 7월~
- 🔜 **UX 라이팅 가이드** (한/영 다국어) — 2026 7~10월
- 🔄 **JSON 코드 연동** (Style Dictionary 등) — W3C Design Tokens 형식 export 완료, Style Dictionary 빌드 파이프라인 작업 예정
- 🔜 **Code Connect** — Figma ↔ React/Vue 1:1 매핑

---

## ⚠️ 알려진 이슈

- ~~`Brand/Secondary/netural`의 `netural` 오타 유지~~ → **v2.0에서 `neutral`로 정정 완료.** Figma 변수 및 토큰 JSON 모두 반영됨. 함께 `transpaernt`→`transparent`, `Interctive`→`Interactive` 오타도 정정.
- `primary_typography`의 `font_family`·`font_family_typeface` 토큰 값이 `"String value"` 플레이스홀더 상태. 실사용 토큰(`font_family_typeface_sans` 등)은 정상이므로, Figma에서 두 토큰에 실제 값을 채우거나 미사용 시 삭제 필요.
- 토큰 값은 W3C Design Tokens 형식 export 파일(`DDS_tokens.w3c.json`)에서 확인 가능. `get_variable_defs`는 노드 선택이 필요해 MCP 경유로는 일부 토큰만 수집되므로, 전체 토큰은 export 파일을 기준으로 함.

---

*최종 갱신: 2026-05-22 · Figma MCP 기반 인덱싱 · 토큰 오타 정정 및 W3C 토큰 export 반영*
