# Table

> 행과 열로 구조화된 데이터를 표시. 정렬·필터·페이지네이션·선택 등 인터랙션 지원.

[← Components](./README.md) · [← design.md](../design.md)

---

## 1. 컴포넌트 패밀리

| 이름 | 타입 | componentKey |
|------|------|--------------|
| `table` | component | `efc4dd8d21885f5d81274546d6ee2679c4ab70e9` |

---

## 2. Anatomy

```
[Table Wrapper]
├── [Toolbar]              (옵션: 검색, 필터, 액션 버튼)
├── [Table]
│   ├── [Header Row]
│   │   ├── [Select All Checkbox]   (옵션, 선택 모드)
│   │   ├── [Header Cell × N]
│   │   │   ├── Label
│   │   │   └── Sort Indicator       (정렬 가능 컬럼)
│   │   └── ...
│   ├── [Body Rows]
│   │   ├── [Row]
│   │   │   ├── [Select Checkbox]   (옵션)
│   │   │   ├── [Cell × N]
│   │   │   └── [Row Actions]       (옵션: 우측 점3개 메뉴)
│   │   └── ...
│   ├── [Empty State]               (데이터 없을 때)
│   └── [Loading State]             (스켈레톤)
└── [Footer]                        (옵션: 페이지네이션, 합계)
```

---

## 3. Variants

| Property | 값 | 의미 |
|----------|-----|------|
| `density` | `compact` · `default` · `comfortable` | 행 높이 |
| `bordered` | bool | 셀 보더 표시 |
| `striped` | bool | 짝수 행 배경 |
| `hoverable` | bool | 행 호버 강조 |
| `selectable` | bool | 행 선택 가능 (체크박스) |
| `sticky` | bool | 헤더/첫 열 고정 |

---

## 4. Density

| 밀도 | 행 높이 | 셀 패딩 상하 | 용도 |
|------|---------|--------------|------|
| `compact` | 32px | `spacing/4` | 대량 데이터, 분석 화면 |
| `default` | 48px | `spacing/8` | 일반 |
| `comfortable` | 56px | `spacing/12` | 가독성 우선 |

---

## 5. Cell 정렬

| 데이터 타입 | 정렬 |
|-------------|------|
| 텍스트 | left |
| 숫자 · 통화 · 퍼센트 | right |
| 날짜 | left (또는 right) |
| 상태 배지 · 아이콘 | center 또는 left |
| 액션 (버튼) | right |

---

## 6. States

| 영역 | 상태 | 표현 |
|------|------|------|
| Row | default | 기본 |
| Row | hover | `Color/bg/secondary` (옅게) |
| Row | selected | `Color/bg/info` (옅게) + `Color/border/info` 좌측 2px |
| Row | disabled | `Color/text/disabled` |
| Header | sortable hover | 아이콘 강조 |
| Cell | editable hover | 편집 가능 표시 (아이콘 또는 보더) |
| Empty | — | 일러스트 + 안내 텍스트 + (옵션) 액션 버튼 |
| Loading | — | 스켈레톤 행 (최소 3행) |

---

## 7. Sorting

| 상태 | 아이콘 |
|------|--------|
| 정렬 가능 | ↕ (옅게) |
| 오름차순 | ↑ |
| 내림차순 | ↓ |
| 정렬 불가 | (아이콘 없음) |

- 정렬 기준 컬럼은 헤더에 강조 표시
- 다중 정렬 시 우선순위 번호 표기 (1, 2, …)

---

## 8. Pagination

| 패턴 | 사용 시기 |
|------|-----------|
| Numbered (1, 2, 3, …) | 총 페이지 수가 의미 있을 때 |
| Prev/Next | 단순 탐색 |
| Infinite scroll | 모바일, 피드형 데이터 |
| Load more | 페이지 개념 약한 데이터 |

표시 정보:
- 현재 페이지 / 전체 페이지
- 표시 중 행 범위 (예: "11–20 of 248")
- 페이지당 행 수 선택 (10, 25, 50, 100)

---

## 9. Props (React)

```tsx
type Column<T> = {
  key: string;
  header: string;
  accessor: (row: T) => React.ReactNode;
  align?: 'left' | 'right' | 'center';
  width?: number | string;
  sortable?: boolean;
  sticky?: boolean;
};

type TableProps<T> = {
  columns: Column<T>[];
  data: T[];
  rowKey: (row: T) => string;

  density?: 'compact' | 'default' | 'comfortable';
  bordered?: boolean;
  striped?: boolean;
  hoverable?: boolean;
  selectable?: boolean;
  selectedRowKeys?: string[];
  onSelectChange?: (keys: string[]) => void;

  sortBy?: { key: string; direction: 'asc' | 'desc' };
  onSortChange?: (sort: { key: string; direction: 'asc' | 'desc' }) => void;

  loading?: boolean;
  emptyState?: React.ReactNode;

  pagination?: {
    page: number;
    pageSize: number;
    total: number;
    onPageChange: (page: number) => void;
    onPageSizeChange?: (size: number) => void;
  };

  rowActions?: (row: T) => React.ReactNode;
  onRowClick?: (row: T) => void;
};
```

---

## 10. Tokens 사용 요약

| 영역 | 토큰 |
|------|------|
| Header 배경 | `Color/bg/secondary` |
| Header 텍스트 | `Color/text/primary`, `body/sm/medium` |
| Body Row 배경 | `Color/bg/primary` |
| Striped 배경 | `Color/bg/secondary` (옅게) |
| Row hover 배경 | `Color/bg/tertiary` |
| Row selected 배경 | `Color/bg/info` (옅게) |
| Cell 보더 | `Color/border/secondary` |
| Cell Text Style | `body/sm/regular` (compact) / `body/md/regular` (comfortable) |
| Cell 패딩 | `spacing/4` ~ `spacing/12` (density 따라) |
| Radius | 외부 컨테이너 `border/radius/md` |

---

## 11. Accessibility

- **시맨틱 HTML**: `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th scope="col">`, `<td>`
- 정렬 가능 헤더: `<button>` 안에 `aria-sort="ascending" | "descending" | "none"`
- 행 선택: `aria-selected="true"` + checkbox
- 키보드:
  - `Tab`으로 인터랙티브 셀 간 이동
  - 정렬: `Enter`/`Space`로 헤더 토글
  - 선택: `Space`로 체크박스 토글
- 빈 상태와 로딩 상태도 스크린리더 알림
- 캡션이 필요하면 `<caption>` 사용
- 가로 스크롤 영역은 `tabindex="0"` + `aria-label` 부여

---

## 12. 반응형

| 화면 폭 | 전략 |
|---------|------|
| ≥ 1024px | 풀 테이블 |
| 768–1023px | 일부 컬럼 숨김 (priority 낮은 순) |
| < 768px | **카드 변환** — 행을 카드로, 컬럼을 라벨-값 쌍으로 |

또는:
- 가로 스크롤 (sticky 첫 열) 유지
- 핵심 컬럼만 남기고 나머지는 행 클릭 시 상세 패널

---

## 13. Do / Don't

✅ **DO**
- 헤더는 명확한 명사 ("주문번호", "결제 금액")
- 숫자 컬럼은 우측 정렬 + 단위 일관
- 긴 텍스트는 ellipsis (`...`) + 호버 시 풀 텍스트
- 빈 상태에 다음 액션 제안 ("주문이 없습니다 → 새 주문 만들기")
- 대량 데이터는 페이지네이션 또는 가상 스크롤

❌ **DON'T**
- 모든 셀을 클릭 가능하게 (핵심 1개만)
- 셀 안에 버튼 5개 이상
- 정렬 가능 표시 없이 정렬만 동작
- 행 호버 강조와 selected 강조 색이 비슷
- 컬럼 너무 많아 가로 스크롤이 화면의 2배 이상

---

## 14. Examples

```tsx
// 기본 사용
<Table
  columns={[
    { key: 'id',     header: '주문번호', accessor: r => r.id, sortable: true },
    { key: 'name',   header: '고객명',   accessor: r => r.customerName },
    { key: 'amount', header: '결제금액', accessor: r => `₩${r.amount.toLocaleString()}`, align: 'right', sortable: true },
    { key: 'status', header: '상태',     accessor: r => <Badge>{r.status}</Badge> },
    { key: 'date',   header: '주문일',   accessor: r => formatDate(r.createdAt), sortable: true },
  ]}
  data={orders}
  rowKey={r => r.id}
  selectable
  selectedRowKeys={selected}
  onSelectChange={setSelected}
  sortBy={sort}
  onSortChange={setSort}
  pagination={{ page, pageSize: 25, total, onPageChange: setPage }}
  rowActions={(row) => (
    <IconButton aria-label="더 보기" icon={<MoreHorizontal />} onClick={() => openMenu(row)} />
  )}
  emptyState={
    <EmptyState
      title="주문이 없습니다"
      description="첫 주문을 만들어 보세요"
      action={<Button variant="primary">새 주문</Button>}
    />
  }
/>
```
