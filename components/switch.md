# Switch

> 즉시 적용되는 ON/OFF 상태를 토글하는 컨트롤.

[← Components](./README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | componentKey |
|------|------|--------------|
| `switch` | component_set | `0d88397b7d6470701103457e4127e40413ceaa17` |

---

## 2. Anatomy

```
[Switch Wrapper]
├── [Track]   ← 트랙 (배경)
└── [Thumb]   ← 둥근 손잡이 (좌→우 슬라이드)

(옵션) + [Label] 우측
```

---

## 3. Variants

| Property | 값 | 의미 |
|----------|-----|------|
| `checked` | bool | 켜짐 / 꺼짐 |
| `disabled` | bool | 비활성 |
| `size` | `sm` · `md` | 사이즈 |

---

## 4. Size

| 사이즈 | 트랙 W×H | Thumb | 이동 거리 |
|--------|----------|-------|-----------|
| `sm` | 32 × 20 | 16 | 12px |
| `md` | 44 × 24 | 20 | 20px |

---

## 5. States & Tokens

| 상태 | Track | Thumb |
|------|-------|-------|
| OFF (default) | `Color/bg/secondary` | white |
| OFF hover | bg 한 단계 어둡게 | — |
| OFF focus-visible | `Color/border/info` outline | — |
| ON (checked) | `Color/bg/interactive/primary` (green 500 = `#14bc62`) | white |
| ON hover | bg 한 단계 어둡게 | — |
| disabled | `Color/bg/disabled` | `Color/bg/secondary` (옅게) |

```css
.switch-track {
  width: 44px; height: 24px;
  border-radius: var(--radius-rounded);
  background: var(--color-bg-secondary);
  transition: background-color var(--motion-duration-quick) var(--motion-easing-standard);
  position: relative;
}
.switch-thumb {
  position: absolute; top: 2px; left: 2px;
  width: 20px; height: 20px;
  background: #fff;
  border-radius: var(--radius-rounded);
  box-shadow: var(--shadow-sm);
  transition: transform var(--motion-duration-quick) var(--motion-easing-spring-snappy);
}
.switch[aria-checked="true"] .switch-track { background: var(--color-bg-interactive-primary); /* green 500 */ }
.switch[aria-checked="true"] .switch-thumb { transform: translateX(20px); }
.switch:focus-visible .switch-track { outline: 2px solid var(--color-border-info); outline-offset: 2px; }
.switch[aria-disabled="true"] .switch-track { background: var(--color-bg-disabled); }
```

---

## 6. Props (React)

```tsx
type SwitchProps = {
  checked: boolean;
  onChange: (checked: boolean) => void;
  label?: string;
  size?: 'sm' | 'md';
  disabled?: boolean;
  'aria-label'?: string;          // label 없을 때 필수
  'aria-describedby'?: string;
};
```

---

## 7. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| Track OFF | `Color/bg/secondary` |
| Track ON | `Color/bg/interactive/primary` (green 500) |
| Track disabled | `Color/bg/disabled` |
| Thumb | `Brand/Secondary/neutral/white` |
| Radius | `border/radius/rounded` |
| 모션 | `duration/quick` + `easing/spring/snappy` |
| Focus | `Color/border/info` outline 2px |

---

## 8. Accessibility

- `<button role="switch" aria-checked={checked}>` 사용 또는 `<input type="checkbox" role="switch">`
- 라벨 없으면 `aria-label` 필수
- 키보드: `Tab` 포커스, `Space` 토글
- 변경 즉시 반영 (적용 버튼 없이) — 그래서 Switch라 부름
- 적용에 시간이 걸리면 loading 상태 표시 (`aria-busy`)
- 햅틱: 토글 시 Light 펄스 (네이티브 환경)

---

## 9. Switch vs Checkbox

| 시나리오 | 사용할 컴포넌트 |
|----------|----------------|
| 즉시 적용되는 설정 (알림 ON/OFF, 다크 모드) | **Switch** |
| 폼 제출 시 값 전달 (약관 동의, 옵션 선택) | **Checkbox** |
| "예/아니오" 명확한 이진 선택 | **Switch** |
| 여러 항목 다중 선택 | **Checkbox** |

---

## 10. Do / Don't

✅ **DO**
- 즉시 적용 (저장 버튼 없이)
- 라벨은 토글의 **대상**을 명사로 ("푸시 알림")
- ON 상태가 명확히 보이도록 색 대비 확보

❌ **DON'T**
- "켜기/끄기" 같은 동사 라벨 (체크박스처럼 들림)
- 적용에 추가 액션 필요한데 Switch 사용
- ON/OFF가 모두 회색 톤이라 구분 안 되게

---

## 11. Examples

```tsx
// 1. 기본
const [enabled, setEnabled] = useState(false);
<Switch label="푸시 알림" checked={enabled} onChange={setEnabled} />

// 2. 라벨 없이 (table cell 등)
<Switch
  aria-label="자동 갱신"
  checked={autoRenew}
  onChange={setAutoRenew}
/>

// 3. 로딩 중 (서버 동기화)
<Switch
  label="2단계 인증"
  checked={mfa}
  onChange={handleToggleMfa}
  disabled={syncing}
/>

// 4. 설명 추가
<div>
  <Switch
    label="마케팅 정보 수신"
    aria-describedby="mkt-desc"
    checked={marketing}
    onChange={setMarketing}
  />
  <p id="mkt-desc" className="text-body-sm-regular text-text-tertiary">
    프로모션·이벤트 안내 메일을 받습니다. 언제든 해지 가능.
  </p>
</div>
```
