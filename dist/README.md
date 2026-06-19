# dist — 빌드 산출물 (Generated)

> ⚠️ **이 폴더의 파일은 직접 수정하지 마세요.** `foundations/DDS_tokens_w3c.json`(+ `foundations/motion.md`)에서 자동 생성됩니다.
> 토큰을 바꾸려면 JSON을 수정한 뒤 재생성하세요.

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
