# Page Header

> 페이지 최상단에 위치하는 헤더. 페이지 정체성 · 뒤로가기 · 주요 액션 · 부가 정보를 일관되게 표시.

[← Components](./README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | componentKey |
|------|------|--------------|
| `Page Header` | component | `c7f1e925dda0381a7e2e61d21b791b4b931af411` |

---

## 2. Anatomy

```
[Page Header]
├── [Breadcrumb]         (옵션, 위)
├── [Top Row]
│   ├── [Back Button]    (옵션, 상세 페이지)
│   ├── [Title Group]
│   │   ├── [Title]      (필수)
│   │   └── [Badge / Status] (옵션)
│   └── [Actions]        (옵션: 버튼, 메뉴)
├── [Description]        (옵션, 부가 설명)
└── [Sub Navigation]     (옵션: Tabs)
```

---

## 3. Variants

| Property | 값 | 의미 |
|----------|-----|------|
| `size` | `sm` · `md` · `lg` | 헤더 높이 / 타이틀 크기 |
| `hasBack` | bool | 뒤로가기 버튼 표시 |
| `hasBreadcrumb` | bool | 브레드크럼 표시 |
| `hasTabs` | bool | 하단 탭 네비게이션 |
| `sticky` | bool | 스크롤 시 고정 |

---

## 4. Size

| 사이즈 | Title Text Style | Description | 상하 패딩 | 용도 |
|--------|------------------|-------------|-----------|------|
| `sm` | `Heading/sm` | `body/sm/regular` | `spacing/16` | 모달 헤더, 좁은 페이지 |
| `md` | `Heading/lg` | `body/md/regular` | `spacing/24` | 일반 페이지 (기본) |
| `lg` | `Heading/xl` 또는 `Heading/2xl` | `body/lg/regular` | `spacing/32` | 랜딩 · 대시보드 메인 |

---

## 5. Layout

### 5.1 기본 (좌우 정렬)

```
[← 뒤로]  [페이지 제목] [Badge]                  [버튼] [버튼] [···]
[부가 설명 텍스트]
```

### 5.2 브레드크럼 포함

```
홈 / 주문 / 주문번호 #12345
[← 뒤로]  [주문번호 #12345] [결제완료]            [환불] [영수증 다운로드]
2026-05-21 14:32 결제 · 김부영 고객
```

### 5.3 탭 포함

```
[설정]                                            [저장]
프로필 · 알림 · 보안 · 결제 · 멤버
─────────────────────────────────────────────────
```

---

## 6. Sticky Behavior

`sticky: true`일 때:

- `position: sticky; top: 0`
- 스크롤 임계점(예: 80px) 지나면:
  - 헤더 높이 축소 (`md` → `sm`)
  - 그림자 추가 (`shadow/sm`)
  - 배경 불투명도 100% 보장 (반투명 금지)
- 모션: `duration/base` + `easing/standard`
- Description은 sticky 상태에서 숨김

---

## 7. Props (React)

```tsx
type PageHeaderProps = {
  title: string;
  description?: string;
  badge?: React.ReactNode;
  breadcrumb?: { label: string; href?: string }[];
  back?: { label?: string; onClick: () => void } | { href: string };
  actions?: React.ReactNode;     // <Button> 또는 <ButtonStack>
  tabs?: React.ReactNode;        // <Tabs>
  size?: 'sm' | 'md' | 'lg';
  sticky?: boolean;
  alignment?: 'left' | 'center'; // 기본 left
};
```

---

## 8. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| 배경 | `Color/bg/primary` |
| 하단 보더 (sticky 시) | `Color/border/secondary` |
| Title 색상 | `Color/text/primary` |
| Description 색상 | `Color/text/tertiary` |
| Breadcrumb 색상 | `Color/text/tertiary` (구분자: `/`) |
| Title Text Style | `Heading/sm` · `Heading/lg` · `Heading/xl`/`2xl` |
| 상하 패딩 | `spacing/16` ~ `spacing/32` |
| Title ↔ Description 갭 | `spacing/4` ~ `spacing/8` |
| Title ↔ Actions 갭 | `spacing/16` (최소) |
| Description ↔ Tabs 갭 | `spacing/16` |
| Shadow (sticky) | `shadow/sm` |

---

## 9. Accessibility

- `<header>` 시맨틱 엘리먼트 사용
- 페이지 제목은 `<h1>` (페이지당 1개)
- 브레드크럼은 `<nav aria-label="Breadcrumb">` + `<ol>` 구조, 마지막 항목 `aria-current="page"`
- 뒤로가기 버튼: `<button>` (또는 `<a>` if href) + `aria-label="이전 페이지로"`
- 탭: `role="tablist"`, 개별 탭 `role="tab"` + `aria-selected`
- Sticky 시 키보드 스크롤이 가려지지 않도록 z-index 관리

---

## 10. Do / Don't

✅ **DO**
- Title은 명사구로 페이지 정체성을 명확히 ("주문 목록", "프로필 설정")
- Actions는 우측, 가장 중요한 액션은 가장 우측
- Description은 1–2줄로 간결하게
- 모바일에서는 Actions를 아이콘 메뉴로 축소
- Breadcrumb는 3단계 이하

❌ **DON'T**
- Title에 "페이지", "화면" 같은 군더더기 ("주문 목록 페이지")
- Action 버튼 5개 이상 나열 — 메뉴(`···`)로 그룹화
- Description에 본문 콘텐츠 다 욱여넣기
- Sticky 헤더가 화면의 30% 이상 차지

---

## 11. Examples

```tsx
// 1. 기본
<PageHeader
  title="주문 목록"
  description="전체 주문 내역을 관리하세요"
  actions={<Button variant="primary" iconBefore={<Plus />}>새 주문</Button>}
/>

// 2. 상세 페이지 (뒤로가기 + Badge)
<PageHeader
  back={{ onClick: router.back }}
  title="주문 #12345"
  badge={<Badge variant="success">결제완료</Badge>}
  description="2026-05-21 14:32 · 김부영 고객"
  actions={
    <ButtonStack>
      <Button variant="tertiary">환불</Button>
      <Button variant="secondary" iconBefore={<Download />}>영수증</Button>
    </ButtonStack>
  }
/>

// 3. 브레드크럼 + 탭
<PageHeader
  breadcrumb={[
    { label: '홈',     href: '/' },
    { label: '설정',   href: '/settings' },
    { label: '프로필' },
  ]}
  title="설정"
  tabs={
    <Tabs value={tab} onChange={setTab}>
      <Tab value="profile">프로필</Tab>
      <Tab value="notif">알림</Tab>
      <Tab value="security">보안</Tab>
      <Tab value="billing">결제</Tab>
    </Tabs>
  }
  sticky
/>

// 4. 대시보드 (lg)
<PageHeader
  size="lg"
  title="안녕하세요, 부영님 👋"
  description="이번 주 새로운 주문 23건이 있습니다"
  actions={
    <Button variant="primary" size="lg" iconBefore={<Sparkles />}>
      AI 분석 보기
    </Button>
  }
/>
```
