# Components

> DDS v2.0 컴포넌트 카탈로그.
> 모든 컴포넌트는 `2026_DDS_v2_배포용` 라이브러리에 게시되어 있으며, Figma 인스턴스 1개 = 코드 컴포넌트 1개 원칙을 따른다.

[← design.md](../design.md)

---

## 📂 카테고리

### Actions
- [Button](./button.md) — 기본 · 아이콘 · 스택 버튼

### Form Inputs
- [Input / Text Field](./input.md) — 텍스트 입력
- [Switch](./switch.md) — 토글 스위치
- [Checkbox](./checkbox.md) — 체크박스
- [Option Group](./option-group.md) — 라디오 · 체크박스 그룹

### Feedback & Overlay
- [Tooltip](./tooltip.md) — 정보 제공 말풍선 (13 방향 변형)

### Data Display
- [Table](./table.md) — 데이터 테이블

### Layout
- [Page Header](./page-header.md) — 페이지 상단 헤더

### Icons
- [Icon System](./icons.md) — 아이콘 카탈로그 및 사용 규칙

---

## 🔑 componentKey 인덱스

코드 매핑(Code Connect)에서 Figma 컴포넌트를 식별하는 키.

| 이름 | 타입 | componentKey | 문서 |
|------|------|--------------|------|
| `button` | set | `fdff8da5b3c2d1f992a124335acbfbd4c7252f7e` | [button.md](./button.md) |
| `Button` | comp | `6fc735282dd1333a73e920e6c292d0f61d74761e` | [button.md](./button.md) |
| `button_48px` | set | `8e2a3a35bd5ca8de9c0e70fe1dfa4204aed0eac8` | [button.md](./button.md) |
| `btn_s_default` | set | `ba398865e4078f4f04c3d7624deed7dceb2853e7` | [button.md](./button.md) |
| `icon button` | set | `c7a26ef430b0d19af0996b7bf101a5b821ed2ebb` | [button.md#8-icon-button](./button.md) |
| `Button Stack` | set | `f0f26be2292c003aef2d3858a771dec0a17eb78f` | [button.md#9-button-stack](./button.md) |
| `Part/Text field placeholder` | set | `a00a00a43688a2051c685eeb8bc2a9014d6f34d9` | [input.md](./input.md) |
| `switch` | set | `0d88397b7d6470701103457e4127e40413ceaa17` | [switch.md](./switch.md) |
| `check-square` | comp | `f9cc1062fadf00fbc6467d6824b90d516efbb4f5` | [checkbox.md](./checkbox.md) |
| `Option group` | set | `ce095fbc9fd90fc9e5154180ba9571c6543b2d57` | [option-group.md](./option-group.md) |
| `Tooltip` | set | `1bea0b81c8247700e26edab9ce5b4242f91b4c01` | [tooltip.md](./tooltip.md) |
| `table` | comp | `efc4dd8d21885f5d81274546d6ee2679c4ab70e9` | [table.md](./table.md) |
| `Page Header` | comp | `c7f1e925dda0381a7e2e61d21b791b4b931af411` | [page-header.md](./page-header.md) |
| `user`, `bell_on`, `more-horizontal`, `check-square`, `message-square` | comp | (각 아이콘) | [icons.md](./icons.md) |
| `Icon placeholder` | set | `8868c045bed192a967b70eacec637ec8ea259a35` | [icons.md](./icons.md) |

---

## ✅ 공통 규칙

모든 컴포넌트 구현 시 반드시 따라야 할 규칙:

1. **컬러** → [foundations/colors.md](../foundations/colors.md) Semantic 토큰만 사용
2. **간격** → [foundations/spacing.md](../foundations/spacing.md) `spacing/*` 토큰만
3. **타이포** → [foundations/typography.md](../foundations/typography.md) Text Style
4. **모서리** → [foundations/radius.md](../foundations/radius.md) `border/radius/*`
5. **상태** → [foundations/state.md](../foundations/state.md) 표준 셀렉터
6. **모션** → [foundations/motion.md](../foundations/motion.md) Duration·Easing 토큰
7. **접근성** → 시맨틱 HTML, `aria-*` 속성, 키보드 네비게이션
8. **변형 = props** → Figma Variant Property ↔ 코드 props 1:1

---

## 📄 컴포넌트 문서 템플릿

새 컴포넌트를 추가할 때 다음 섹션을 따른다.

```
1. 컴포넌트 패밀리   — Figma componentKey 표
2. Anatomy           — 구성 요소 트리
3. Variants          — Figma Variant Property
4. Sizes             — 사이즈 변형 (있다면)
5. States            — 상태별 시각/토큰
6. Props (React)     — 코드 API
7. Tokens 사용 요약  — 어떤 토큰을 어디에 쓰는지
8. Accessibility     — a11y 규칙
9. Do / Don't        — 좋은 사례 / 나쁜 사례
10. Examples         — 코드 예시
```
