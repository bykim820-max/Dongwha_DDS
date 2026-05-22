# Option Group

> 여러 옵션 중 하나(Radio) 또는 여러 개(Checkbox)를 선택하는 그룹 컨테이너.

[← Components](./README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | componentKey |
|------|------|--------------|
| `Option group` | component_set | `ce095fbc9fd90fc9e5154180ba9571c6543b2d57` |

---

## 2. Anatomy

```
[Option Group Wrapper]
├── [Legend / Group Label]  (필수, 그룹 제목)
├── [Helper Text]           (옵션)
├── [Options Container]     (세로 또는 가로)
│   ├── [Option Item]
│   │   ├── [Radio | Checkbox]
│   │   └── [Label]
│   └── ...
└── [Error Text]            (옵션)
```

---

## 3. Variants

| Property | 값 | 의미 |
|----------|-----|------|
| `type` | `radio` · `checkbox` | 단일 선택 / 다중 선택 |
| `orientation` | `vertical` · `horizontal` | 정렬 방향 |
| `state` | `default` · `error` · `disabled` | 그룹 전체 상태 |

---

## 4. Layout

| 옵션 수 | 권장 정렬 |
|---------|-----------|
| 2개 (Yes/No 등) | `horizontal` |
| 3–5개 (짧은 라벨) | `horizontal` 또는 `vertical` |
| 6개 이상 | `vertical` 또는 Select로 변경 검토 |
| 옵션 라벨이 길거나 설명 동반 | `vertical` |

### Spacing

| 위치 | 토큰 |
|------|------|
| Legend ↔ 옵션 첫 줄 | `spacing/8` |
| 세로 옵션 간 갭 | `spacing/8` ~ `spacing/12` |
| 가로 옵션 간 갭 | `spacing/16` ~ `spacing/24` |
| 옵션 ↔ 헬퍼/에러 | `spacing/4` |

---

## 5. States

전체 그룹 단위로 적용:

| 상태 | 표현 |
|------|------|
| `default` | 기본 |
| `error` | Legend 또는 에러 텍스트 빨강, 모든 옵션 보더 빨강 |
| `disabled` | 모든 옵션 비활성 |

개별 옵션 상태(checked/unchecked, hover, focus)는 각 [Checkbox](./checkbox.md) / Radio 컴포넌트의 상태를 따른다.

---

## 6. Props (React)

```tsx
type Option = { value: string; label: string; disabled?: boolean; description?: string };

type OptionGroupProps = {
  type: 'radio' | 'checkbox';
  legend: string;
  options: Option[];
  value: string | string[];            // radio: string, checkbox: string[]
  onChange: (value: string | string[]) => void;
  orientation?: 'vertical' | 'horizontal';
  helperText?: string;
  errorText?: string;
  required?: boolean;
  disabled?: boolean;
  name: string;
};
```

---

## 7. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| Legend Text Style | `body/sm/medium` 또는 `body/md/medium` |
| Legend 색상 | `Color/text/primary` |
| Helper 색상 | `Color/text/tertiary` |
| Error 색상 | `Color/text/danger` |
| 옵션 간 갭 | `spacing/8` ~ `spacing/24` (방향에 따라) |

---

## 8. Accessibility

- **`<fieldset>` + `<legend>`로 그룹화 필수** — 스크린리더가 그룹 컨텍스트 인지
- Radio: `<input type="radio" name="...">` — 같은 `name`으로 그룹 형성
- Checkbox 그룹: `<input type="checkbox">` 다중
- 키보드:
  - Radio 그룹: `Tab` 진입 → `←/↑/→/↓`로 옵션 이동 (자동 선택)
  - Checkbox 그룹: `Tab`으로 각 항목 이동, `Space`로 토글
- 그룹 에러는 `aria-describedby`로 에러 텍스트 연결, `aria-invalid="true"`
- 필수: `aria-required="true"` + Legend에 시각 표식 (`*`)

---

## 9. Do / Don't

✅ **DO**
- Legend는 명사구 ("배송 옵션", "관심 분야")
- 옵션 4개 이하면 Radio 그룹, 5개 이상이면 Select 검토
- "기타" 옵션 + 텍스트 인풋 조합 시 인풋 활성/비활성을 옵션 선택 따라 토글

❌ **DON'T**
- Legend 없이 옵션만 나열
- Radio 그룹인데 `name` 다르게 부여 (그룹 형성 실패)
- 다중 선택인데 Radio 사용
- 가로 정렬 옵션이 화면 폭에 따라 줄바꿈되는데 갭이 어색하게 변할 때 → 그냥 세로로

---

## 10. Examples

```tsx
// 1. Radio 그룹 (단일 선택)
<OptionGroup
  type="radio"
  name="delivery"
  legend="배송 옵션"
  value={delivery}
  onChange={setDelivery}
  options={[
    { value: 'standard', label: '일반 배송 (2–3일)' },
    { value: 'express',  label: '빠른 배송 (당일)' },
    { value: 'pickup',   label: '매장 픽업' },
  ]}
  required
/>

// 2. Checkbox 그룹 (다중 선택)
<OptionGroup
  type="checkbox"
  name="interests"
  legend="관심 분야"
  value={interests}
  onChange={setInterests}
  options={[
    { value: 'design', label: '디자인' },
    { value: 'dev',    label: '개발' },
    { value: 'pm',     label: '프로덕트' },
    { value: 'data',   label: '데이터' },
  ]}
  helperText="여러 개 선택 가능"
/>

// 3. 에러
<OptionGroup
  type="radio"
  name="agreement"
  legend="약관 동의"
  value={agree}
  onChange={setAgree}
  options={[
    { value: 'yes', label: '동의합니다' },
    { value: 'no',  label: '동의하지 않습니다' },
  ]}
  required
  errorText={!agree ? '약관 동의가 필요합니다' : undefined}
/>

// 4. 설명 동반 옵션 (세로 권장)
<OptionGroup
  type="radio"
  name="plan"
  legend="요금제"
  orientation="vertical"
  value={plan}
  onChange={setPlan}
  options={[
    { value: 'free',  label: 'Free',  description: '기본 기능' },
    { value: 'pro',   label: 'Pro',   description: '월 ₩9,900' },
    { value: 'team',  label: 'Team',  description: '월 ₩29,900 / 5인' },
  ]}
/>
```
