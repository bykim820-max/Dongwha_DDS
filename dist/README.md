# dist — 빌드 산출물 (Generated)

> ⚠️ **이 폴더의 토큰 파일(`tokens.*`)은 직접 수정하지 마세요.** `foundations/DDS_tokens_w3c.json`(+ `foundations/motion.md`)에서 자동 생성됩니다.
> 토큰을 바꾸려면 JSON을 수정한 뒤 재생성하세요. 이 README는 생성 파일이 아닙니다.

> 📦 **다른 시스템에서 이 파일을 가져다 쓰시나요?** 넣는 법은 **[START.md §2](../START.md)** 에 세 단계로 있습니다.
> 2027년부터 DDS는 유지 모드이고 **v2.6.0이 최종**입니다. 파일은 동화Lab에서 받습니다.
> Claude Code [dds 플러그인](../plugins/dds/README.md)(`/dds:init`)은 GitHub 보관 저장소가 남아 있는 동안만 동작합니다 → [HANDOVER.md §1.2](../HANDOVER.md)
> 무엇이 바뀌었는지는 → [CHANGELOG.md](../CHANGELOG.md)

## 내가 가진 버전 확인

```bash
head -3 dist/tokens.css
#   DDS v2.6.0 · Design Tokens (생성 파일 — 직접 수정 금지)
```

⚠️ **v2.4.0 이전에 배포된 파일은 내용과 무관하게 헤더가 전부 `v2.0`으로 찍혀 있습니다.**
실제 버전 판별은 [CHANGELOG 판별표](../CHANGELOG.md#먼저-읽어주세요--v240-이전-파일의-버전-표기-오류)를 보세요.

## 재생성

```bash
python3 scripts/build_tokens.py
```

## 산출물

| 파일 | 용도 |
|------|------|
| `tokens.css` | `:root` CSS 변수. **semantic 토큰이 실제 hex/px로 해석된 드롭인 파일.** import 후 `var(--color-bg-primary)` 등을 바로 사용 |
| `tokens.resolved.json` | 평탄화된 `토큰경로 → 최종값` 맵 (407개). 기계 판독·AI 에이전트용 |
| `tokens.tailwind.js` | Tailwind preset. `presets: [require('./dist/tokens.tailwind.js')]` |

## 사용 (개발자)

```css
/* 1. 값이 채워진 토큰 변수 로드 */
@import "./dist/tokens.css";

/* 2. 컴포넌트는 semantic 변수만 참조 */
.btn-primary { background: var(--color-bg-interactive-primary); color: var(--color-text-interactive-inverse); }
```

```js
// tailwind.config.js
module.exports = { presets: [require('./dist/tokens.tailwind.js')] }
```

## 사용 (비디자이너 + AI 에이전트)

에이전트는 **`tokens.resolved.json`** 에서 토큰명 → 실제값을 직접 조회하거나, `tokens.css` 를 그대로 주입해 일관된 컴포넌트를 생성할 수 있습니다.
컬러 값이 Figma에만 있던 종전 구조와 달리, 이제 이 폴더만으로 값이 자급됩니다.

## 알려진 문제

- ~~`typography.primitive.font_family`, `font_family_typeface` → `"String value"` 플레이스홀더~~ → **2026-11-23 정정.** Figma 변수와 토큰 JSON 모두 `Pretendard` (`tokens.css` 영향 없음)
- 토큰 값 · 조합의 알려진 문제(다크 모드 Toast 글자 대비, `text/interactive/secondary` 다크 대비 등)는 → [design.md 알려진 이슈](../design.md)
