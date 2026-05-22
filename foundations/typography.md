# Typography

> 폰트: **Pretendard** 기본. 한국어 우선, 영문 함께 처리.
> `Semantic Typography` 컬렉션 + Text Styles.

[← design.md](../design.md)

---

## 1. 폰트 패밀리

| 토큰 | 값 |
|------|----|
| `Heading/font family` | Pretendard |
| `Body/font family` | Pretendard |

CSS 폴백:

```css
font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui,
             'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif;
```

---

## 2. Heading 스케일

각 사이즈는 **font size + line height** 변수 쌍 + Text Style로 구성.

| Text Style | 변수 키 | 용도 |
|------------|---------|------|
| `Heading/xs` | `Heading/xs/font size`, `Heading/xs/line height` | 캡션, 라벨 |
| `Heading/sm` | `Heading/sm/font size`, `Heading/sm/line height` | 작은 섹션 타이틀 |
| `Heading/md` | (Text Style only) | 카드 헤더 |
| `Heading/lg` | `Heading/lg/font size`, `Heading/lg/line height` | 모달·페이지 서브 |
| `Heading/xl` | `Heading/xl/font size`, `Heading/xl/line height` | 페이지 타이틀 |
| `Heading/2xl` | `Heading/2xl/font size`, `Heading/2xl/line height` | 디스플레이 |
| `Heading/3xl` | (Text Style only) | 히어로 |
| `Heading/4xl` | `Heading/4xl/font size` | 히어로 (랜딩) |

---

## 3. Body 스케일

| Text Style | 사이즈 | 가중치 |
|------------|--------|--------|
| `body/sm/regular` | sm | regular |
| `body/sm/medium` | sm | medium |
| `body/md/regular` | md | regular **(본문 기본)** |
| `body/md/medium` | md | medium |
| `body/lg/regular` | lg | regular |
| `body/lg/medium` | lg | medium |

공통 변수: `Body/letter spacing`.

---

## 4. Letter Spacing

`primary-Typography` 컬렉션.

| 토큰 | 의미 |
|------|------|
| `letter spacing/loose` | 약간 넓힘 |
| `letter spacing/looser` | 더 넓힘 (대문자·Display용) |

---

## 5. CSS 매핑 예

```css
:root {
  --font-heading: 'Pretendard', system-ui, sans-serif;
  --font-body:    'Pretendard', system-ui, sans-serif;

  /* Heading sizes — 정확한 값은 Figma 변수 패널에서 확인 */
  --heading-xs-font-size:   /* Heading/xs/font size */;
  --heading-xs-line-height: /* Heading/xs/line height */;
  --heading-sm-font-size:   /* Heading/sm/font size */;
  --heading-sm-line-height: /* Heading/sm/line height */;
  --heading-lg-font-size:   /* Heading/lg/font size */;
  --heading-lg-line-height: /* Heading/lg/line height */;
  /* ... xl, 2xl, 3xl, 4xl */

  /* Body sizes */
  --body-sm-font-size:      /* Body/sm/font size */;
  --body-sm-line-height:    /* Body/sm/line height */;
  --body-md-font-size:      /* Body/md/font size */;
  --body-md-line-height:    /* Body/md/line height */;
  --body-lg-font-size:      /* Body/lg/font size */;
  --body-lg-line-height:    /* Body/lg/line height */;
  --body-letter-spacing:    /* Body/letter spacing */;
}

.text-heading-lg {
  font-family: var(--font-heading);
  font-size:   var(--heading-lg-font-size);
  line-height: var(--heading-lg-line-height);
  font-weight: 700;
}

.text-body-md-regular {
  font-family:    var(--font-body);
  font-size:      var(--body-md-font-size);
  line-height:    var(--body-md-line-height);
  letter-spacing: var(--body-letter-spacing);
  font-weight:    400;
}
```

---

## 6. Tailwind 매핑

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        heading: ['Pretendard', 'sans-serif'],
        body:    ['Pretendard', 'sans-serif'],
      },
      fontSize: {
        'heading-xs':  ['var(--heading-xs-font-size)',  { lineHeight: 'var(--heading-xs-line-height)' }],
        'heading-sm':  ['var(--heading-sm-font-size)',  { lineHeight: 'var(--heading-sm-line-height)' }],
        'heading-md':  ['var(--heading-md-font-size)',  { lineHeight: 'var(--heading-md-line-height)' }],
        'heading-lg':  ['var(--heading-lg-font-size)',  { lineHeight: 'var(--heading-lg-line-height)' }],
        'heading-xl':  ['var(--heading-xl-font-size)',  { lineHeight: 'var(--heading-xl-line-height)' }],
        'heading-2xl': ['var(--heading-2xl-font-size)', { lineHeight: 'var(--heading-2xl-line-height)' }],
        'body-sm':     ['var(--body-sm-font-size)',     { lineHeight: 'var(--body-sm-line-height)' }],
        'body-md':     ['var(--body-md-font-size)',     { lineHeight: 'var(--body-md-line-height)' }],
        'body-lg':     ['var(--body-lg-font-size)',     { lineHeight: 'var(--body-lg-line-height)' }],
      },
    },
  },
}
```

---

## 7. 사용 가이드

| 화면 영역 | 권장 스타일 |
|-----------|-------------|
| 페이지 타이틀 (대시보드 헤더) | `Heading/xl` 또는 `Heading/2xl` |
| 섹션 타이틀 | `Heading/lg` |
| 카드 제목 | `Heading/sm` 또는 `Heading/md` |
| 본문 단락 | `body/md/regular` |
| 입력 라벨 | `body/sm/medium` |
| 도움말·캡션 | `body/sm/regular` |
| 버튼 라벨 | `body/sm/medium` 또는 `body/md/medium` |
| 테이블 셀 | `body/sm/regular` |
| 테이블 헤더 | `body/sm/medium` |

---

## 8. 규칙

1. **Text Style 이름을 그대로 클래스로** — `<h2 class="text-heading-lg">` 형태
2. 임의 font-size·line-height 인라인 금지
3. 굵기는 디자인 토큰의 weight 사용 (보통 400 regular / 500 medium / 700 bold)
4. 한국어/영문 혼용 시 줄간격(line-height) 충분히 확보 (한글 1.5+ 권장)
5. 모바일에서 본문은 `16px` 이상 유지 (zoom 방지)
