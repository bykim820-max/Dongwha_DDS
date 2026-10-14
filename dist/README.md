# dist — 빌드 산출물 (Generated)

> ⚠️ **이 폴더의 파일은 직접 수정하지 마세요.** `foundations/DDS_tokens_w3c.json`(+ `foundations/motion.md`)에서 자동 생성됩니다.
> 토큰을 바꾸려면 JSON을 수정한 뒤 재생성하세요.

> 📦 **다른 시스템에서 이 파일을 가져다 쓰시나요?** Claude Code를 쓴다면 **[dds 플러그인](../plugins/dds/README.md)** 의 `/dds:init`이 가장 쉽습니다. 직접 하려면 → **[MIGRATION.md](../MIGRATION.md)**
> 버전 고정해서 받는 법, 새 버전이 나왔을 때 갱신하는 절차, 버전별 대응표가 있습니다.
> 무엇이 바뀌었는지는 → [CHANGELOG.md](../CHANGELOG.md)

## 내가 가진 버전 확인

```bash
head -3 dist/tokens.css
#   DDS v2.5.0 · Design Tokens (생성 파일 — 직접 수정 금지)
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
| `tokens.resolved.json` | 평탄화된 `토큰경로 → 최종값` 맵 (372개). 기계 판독·AI 에이전트용 |
| `tokens.tailwind.js` | Tailwind preset. `presets: [require('./dist/tokens.tailwind.js')]` |

## 사용 (개발자)

```css
/* 1. 값이 채워진 토큰 변수 로드 */
@import "./dist/tokens.css";

/* 2. 컴포넌트는 semantic 변수만 참조 */
.btn-primary { background: var(--color-bg-interactive-primary); color: #fff; }
```

```js
// tailwind.config.js
module.exports = { presets: [require('./dist/tokens.tailwind.js')] }
```

## 사용 (비디자이너 + AI 에이전트)

에이전트는 **`tokens.resolved.json`** 에서 토큰명 → 실제값을 직접 조회하거나, `tokens.css` 를 그대로 주입해 일관된 컴포넌트를 생성할 수 있습니다.
컬러 값이 Figma에만 있던 종전 구조와 달리, 이제 이 폴더만으로 값이 자급됩니다.

## 알려진 미완 토큰

- `typography.primitive.font_family`, `font_family_typeface` → `"String value"` 플레이스홀더.
  실사용 토큰(`--font-heading`, `--font-body` = Pretendard)은 정상이므로 영향 없음. Figma에서 값 입력 또는 삭제 권장.
