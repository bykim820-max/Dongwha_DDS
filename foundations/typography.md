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
각 사이즈는 **font size + line height + font weight** 3변수로 구성(전부 `DDS_tokens_w3c.json`에 존재).

| Text Style | px (size / line / weight) | 용도 |
|------------|---------------------------|------|
| `Heading/xs` | 18 / 20 / 600 | 캡션, 라벨 |
| `Heading/sm` | 20 / 24 / 600 | 작은 섹션 타이틀 |
| `Heading/md` | 24 / 30 / 600 | 카드 헤더 |
| `Heading/lg` | 30 / 32 / 600 | 모달·페이지 서브 |
| `Heading/xl` | 32 / 42 / 700 | 페이지 타이틀 |
| `Heading/2xl` | 42 / 48 / 700 | 디스플레이 |
| `Heading/3xl` | 48 / 56 / 700 | 히어로 |
| `Heading/4xl` | 56 / 68 / 700 | 히어로 (랜딩) |

> 타이틀은 **semibold(600)**, 디스플레이(xl 이상)는 **bold(700)**. 전부 본문(400)보다 무거워 위계가 보장된다.

---

## 3. Body 스케일

Body Text Style = **사이즈 토큰(size·line-height) + 굵기 토큰**의 조합. `regular`/`medium`은 굵기 토큰만 바꿔 표현한다.

| Text Style | px (size / line) | 굵기 토큰 |
|------------|------------------|-----------|
| `body/sm/regular` | 12 / 16 | `--font-weight-regular` (400) |
| `body/sm/medium` | 12 / 16 | `--font-weight-medium` (500) |
| `body/md/regular` | 14 / 16 | `--font-weight-regular` (400) **(본문 기본)** |
| `body/md/medium` | 14 / 16 | `--font-weight-medium` (500) |
| `body/lg/regular` | 16 / 18 | `--font-weight-regular` (400) |
| `body/lg/medium` | 16 / 18 | `--font-weight-medium` (500) |

각 사이즈의 기본 굵기 토큰(`--body-{sz}-font-weight`)은 **400(regular)** 이며, `medium`이 필요하면 `--font-weight-medium`로 덮어쓴다.
공통 변수: `--body-letter-spacing`.

### 3.1 굵기(Weight) 토큰

| 토큰 | 값 | 용도 |
|------|----|------|
| `--font-weight-regular` | 400 | 본문 기본 |
| `--font-weight-medium` | 500 | 버튼·라벨·테이블 헤더 강조 |
| `--font-weight-semibold` | 600 | 타이틀(Heading sm~lg) |
| `--font-weight-bold` | 700 | 디스플레이(Heading xl 이상) |

> v2.0: 종전 body 굵기가 200(extra-light)으로 과도하게 얇아 **400(regular)으로 상향**, medium(500) 축을 신설.

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
  font-weight: var(--heading-lg-font-weight);   /* 600 semibold */
}

.text-body-md-regular {
  font-family:    var(--font-body);
  font-size:      var(--body-md-font-size);
  line-height:    var(--body-md-line-height);
  letter-spacing: var(--body-letter-spacing);
  font-weight:    var(--font-weight-regular);   /* 400 */
}

.text-body-md-medium {
  font-family:    var(--font-body);
  font-size:      var(--body-md-font-size);
  line-height:    var(--body-md-line-height);
  letter-spacing: var(--body-letter-spacing);
  font-weight:    var(--font-weight-medium);    /* 500 */
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
2. 임의 font-size·line-height·font-weight 인라인 금지 — 반드시 토큰 사용
3. 굵기는 **굵기 토큰만 사용**: `--font-weight-{regular|medium|semibold|bold}` (400/500/600/700). 본문 기본은 400, 200/300(라이트) 직접 사용 금지
4. 한국어/영문 혼용 시 줄간격(line-height) 충분히 확보 (한글 1.5+ 권장)
5. 모바일에서 본문은 `16px` 이상 유지 (zoom 방지)
