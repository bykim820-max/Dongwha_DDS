# Tooltip

> 정보 제공 목적의 텍스트 표시 UI. 호버 또는 포커스 시에 보조 설명을 노출.

[← Components](./README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | componentKey | 노드 |
|------|------|--------------|------|
| `Tooltip` | component_set | `1bea0b81c8247700e26edab9ce5b4242f91b4c01` | `5129:1521` |

**Tooltip_Base** (말풍선 본체) + **Tooltip** (Arrow 포함 전체)로 구성.

---

## 2. Anatomy

```
[Tooltip] (Direction에 따라 Arrow 위치 결정)
├── [Arrow]               (옵션, "none" Direction이면 생략)
└── [Tooltip_Base]        (말풍선 본체)
    ├── [Text]            (필수)
    ├── [Action Link]     (Action 변형일 때)
    └── [Close Icon]      (Closed 변형일 때)
```

---

## 3. Property1 (Tooltip_Base 변형)

| 변형 | 설명 |
|------|------|
| `Default` | 텍스트만 표시 |
| `Action` | 텍스트 + 하단 액션 링크 ("더 알아보기" 등) |
| `Closed` | 텍스트 + 우측 닫기(X) 아이콘 |

---

## 4. Direction (방향, 13종)

| 그룹 | 값 |
|------|----|
| **Above** (위쪽) | `Above Left` (기본), `Above Center`, `Above Right` |
| **Below** (아래쪽) | `Below Left`, `Below Center`, `Below Right` |
| **Start** (좌측) | `Start Top`, `Start Middle`, `Start bottom` |
| **End** (우측) | `End Top`, `End Middle`, `End bottom` |
| **none** | 화살표 없이, 너비 `260px` 고정 |

---

## 5. Tooltip_Base 스타일

| 속성 | 값 |
|------|----|
| 배경색 | `rgba(0, 0, 0, 0.85)` |
| 테두리 반경 | `4px` (= `border/radius/md`) |
| 그림자 | `0px 4px 4px rgba(0,0,0,0.25)`, `0px 0px 8px rgba(0,0,0,0.15)` |
| 내부 여백 | `10px` |
| 내부 요소 간격 | `10px` (Closed, Action 타입) |
| 최대 너비 | `240px` (none 변형은 `260px` 고정) |
| 줄바꿈 | 기본 `whitespace-nowrap`, 여러 줄 허용 시 `white-space: normal` |

---

## 6. 텍스트 스타일

| 요소 | 폰트 | 굵기 | 크기 | 줄간격 | 색상 |
|------|------|------|------|--------|------|
| 본문 텍스트 | Pretendard | Light (300) | 14px | 1.25 | `#FFFFFF` |
| Action 링크 | Pretendard | Bold (700) | 14px | 1.25 | `#E5E5E5` |

---

## 7. Arrow 스펙

| 속성 | 값 |
|------|----|
| 크기 | `36 × 8px` |
| 내부 꺾쇠 크기 | `16 × 16px` |
| 꺾쇠 배경색 | `#000000` |
| 꺾쇠 테두리 반경 | `2px` |
| 꺾쇠 회전 | `45deg` |

### 방향별 변환

| 방향 | 변환 |
|------|------|
| Above (위) | 기본 (아래를 향해 꺾임) |
| Below (아래) | `-scale-y-100` |
| Start (좌측) | `rotate-90` + `-scale-y-100` |
| End (우측) | `rotate-90` |

---

## 8. Props (React)

```tsx
type TooltipProps = {
  content: React.ReactNode;
  direction?:
    | 'above-left' | 'above-center' | 'above-right'
    | 'below-left' | 'below-center' | 'below-right'
    | 'start-top'  | 'start-middle' | 'start-bottom'
    | 'end-top'    | 'end-middle'   | 'end-bottom'
    | 'none';
  variant?: 'default' | 'action' | 'closed';
  actionLabel?: string;             // variant="action"일 때
  onActionClick?: () => void;
  onClose?: () => void;             // variant="closed"일 때
  open?: boolean;                   // 제어형
  defaultOpen?: boolean;
  trigger?: 'hover' | 'focus' | 'click' | 'manual';
  delayMs?: number;                 // 호버 지연 (기본 200ms)
  maxWidth?: number;                // 기본 240px
  children: React.ReactElement;     // 앵커 요소
};
```

---

## 9. 모션

| 단계 | 모션 |
|------|------|
| 등장 | `opacity 0→1` + `scale(0.96)→1`, `duration/quick`, `easing/decelerate` |
| 호버 지연 | 마우스 진입 후 **200ms** 후 표시 (즉시 표시는 산만함) |
| 퇴장 | `opacity 1→0`, `duration/instant`, `easing/accelerate` |

---

## 10. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| 배경 | `rgba(0,0,0,0.85)` (전용, Semantic 외) |
| 본문 텍스트 | `#FFFFFF` (`Brand/Secondary/netural/white`) |
| Action 텍스트 | `Primitive/neutral/200` (`#E5E5E5`) |
| Radius | `border/radius/md` |
| 내부 여백 | 10px (커스텀) |
| 최대 너비 | 240px (none: 260px) |
| Text Style | `Body2_14_regular` / `Body2_14_bold` (legacy 토큰) |

---

## 11. Accessibility

- **호버 + 키보드 포커스** 모두에서 표시 — 키보드만으로도 접근 가능해야 함
- 앵커 요소에 `aria-describedby={tooltipId}` 연결
- `Closed` 변형 닫기 아이콘은 `aria-label="닫기"` 필수
- `Esc` 키로 닫기 가능
- 마우스가 Tooltip 위로 이동해도 유지 (특히 Action 변형)
- 배경 대비: `rgba(0,0,0,0.85)` + 흰색 텍스트 → WCAG AA 충족
- 모바일에서는 호버가 없으므로 탭으로 표시, 외부 영역 탭 시 닫힘
- 자동 사라짐 금지 (Closed 변형 제외) — 사용자가 정보 읽을 시간 확보

---

## 12. 사용 시나리오

| 시나리오 | Property1 | Direction |
|----------|-----------|-----------|
| 단순 정보 (인라인) | `Default` | `none` |
| 위에서 내려오는 안내 | `Default` | `Above Center` |
| 닫기 가능한 안내 | `Closed` | `Above Left` |
| 액션 포함 (학습 안내) | `Action` | `Above Left` |
| 입력 필드 우측 도움말 | `Default` | `Start Middle` |
| 아이콘 버튼 라벨 | `Default` | `Below Center` |

---

## 13. Do / Don't

✅ **DO**
- 짧고 명확한 문장 (한 줄, 60자 이내 권장)
- 핵심 정보는 본문에 두고 Tooltip은 보조
- 트리거 요소 근처에 배치 (시선 이동 최소화)
- 키보드 포커스에서도 표시

❌ **DON'T**
- 중요 정보를 Tooltip에만 두기 (호버 불가 환경 존재)
- 인터랙티브 요소(버튼·링크)를 Tooltip 안에 다수 배치 → Popover로 전환 검토
- 5단어 미만 라벨에 Tooltip 남용 — 라벨을 더 명확하게 쓰자
- 너무 길어서 줄바꿈이 3줄 이상 → Modal 또는 Popover 전환

---

## 14. Examples

```tsx
// 1. 아이콘 버튼 라벨
<Tooltip content="더 보기" direction="below-center">
  <IconButton aria-label="더 보기" icon={<MoreHorizontal />} />
</Tooltip>

// 2. 입력 필드 도움말
<Tooltip
  content="영문, 숫자, 특수문자 포함 8자 이상"
  direction="start-middle"
>
  <Input type="password" label="비밀번호" />
</Tooltip>

// 3. 학습 안내 (Action 변형)
<Tooltip
  variant="action"
  content="새로운 차트 보기가 추가됐어요"
  actionLabel="더 알아보기"
  onActionClick={openGuide}
  direction="above-left"
>
  <ChartIcon />
</Tooltip>

// 4. 닫기 가능한 안내 (Closed)
<Tooltip
  variant="closed"
  content="여기를 눌러 빠르게 검색하세요"
  onClose={dismissOnboarding}
  direction="above-right"
>
  <SearchTrigger />
</Tooltip>
```
