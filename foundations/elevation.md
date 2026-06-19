# Elevation

> 깊이(z축)로 위계를 표현한다. **"선 대신 깊이"** — 테두리로 가두기보다 면을 띄워 분리.
> 부드러운 카드 느낌은 **연한 다층 그림자 + 큰 radius**에서 나온다.

[← design.md](../design.md) · [← Motion §6](./motion.md)

---

## 1. 의미 레벨

shadow 값을 직접 쓰지 말고 **의미 레벨 토큰**을 쓴다.

| 토큰 | 매핑 | 용도 |
|------|------|------|
| `--elevation-flat` | none | 평면. 배경 색(`bg/secondary`)으로만 분리 |
| `--elevation-raised` | `shadow/sm` | **카드 기본** (리스트 아이템·패널) |
| `--elevation-overlay` | `shadow/md` | 팝오버·드롭다운·hover lift |
| `--elevation-sticky` | `shadow/md` | sticky 헤더/툴바 (스크롤 시 분리감) |
| `--elevation-modal` | `shadow/lg` | 모달·바텀시트 |
| `--elevation-top` | `shadow/xl` | 풀스크린 오버레이·토스트 |

```css
.card       { box-shadow: var(--elevation-raised); }
.card:hover { box-shadow: var(--elevation-overlay); }   /* hover 시 한 단계 상승 */
.modal      { box-shadow: var(--elevation-modal); }
.appbar.is-stuck { box-shadow: var(--elevation-sticky); }
```

---

## 2. 깊이 + Radius 조합

깊이는 **모서리 둥글기와 함께** 부드러움을 만든다. 떠 있는 면일수록 radius를 키운다.

| 레벨 | radius 권장 |
|------|-------------|
| flat / inline | `border/radius/md` (4) |
| raised (카드) | `border/radius/lg`~`xl` (8~12) |
| modal / sheet | `border/radius/xl`~`2xl` (12~16) |
| 바텀시트 상단 | `2xl` (상단 모서리만) |

> 권장 카드: **`border/radius/xl`(12) + `--elevation-raised`**, 테두리는 생략하거나 아주 연하게(`border/secondary`).

---

## 3. 원칙

| 원칙 | 의미 |
|------|------|
| **선 대신 깊이** | 분리는 그림자·여백·배경으로. 테두리는 최후의 수단 |
| **레벨은 의미** | 위로 뜰수록 사용자 주의·임시성↑ (모달 > 카드 > 평면) |
| **절제** | 한 화면에 강한 그림자 남발 금지. 대부분 raised, 강조만 위로 |
| **상태로 상승** | hover/active 시 한 단계 위 elevation으로 "반응" |

---

## 4. Do / Don't

✅ **DO**
- 의미 레벨 토큰(`--elevation-*`)만 사용
- 카드 기본 = raised, hover 시 overlay로 한 단계 상승
- 떠 있는 면일수록 radius↑
- 그림자 + 큰 radius + 최소 테두리로 부드러운 면

❌ **DON'T**
- shadow 원시값 직접 인라인
- 모든 요소에 강한 그림자 (깊이 인플레이션)
- 테두리 + 강한 그림자 동시 남발 (둘 중 하나)
- 네온/컬러 글로우 그림자 (→ [디자인 금지 규칙](../design.md#-디자인-금지-규칙-anti-patterns))

---

## 5. Tokens 요약

| 영역 | 토큰 |
|------|------|
| 깊이 레벨 | `--elevation-{flat,raised,overlay,sticky,modal,top}` |
| 원시 그림자 | `--shadow-{sm,md,lg,xl}` (직접 사용 지양) |
| 동반 radius | `border/radius/{md,lg,xl,2xl}` |
