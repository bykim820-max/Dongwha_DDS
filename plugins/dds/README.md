# dds — Claude Code 플러그인

Dongwha Design System(DDS)을 쓰는 사내 시스템에서 Claude Code가 **프로젝트에 고정된 DDS 버전**의 규칙과 토큰으로 일하게 한다.

## 설치

필요한 것: Claude Code · git · github.com 접속. GitHub 계정은 필요 없다 (공개 저장소).

### 팀 전체 — 프로젝트에 등록 (권장)

시스템 저장소의 담당자가 **프로젝트 폴더에서 한 번** 실행한다. `/dds:init`도 이 단계를 함께 한다.

```bash
claude plugin marketplace add bykim820-max/Dongwha_DDS --scope project
claude plugin install dds@dongwha-dds --scope project
```

프로젝트에 `.claude/settings.json`이 생긴다. **이 파일을 커밋하면** 그 프로젝트를 Claude Code로 여는 팀원은 플러그인 설치를 안내받는다.

```json
{
  "extraKnownMarketplaces": {
    "dongwha-dds": { "source": { "source": "github", "repo": "bykim820-max/Dongwha_DDS" } }
  },
  "enabledPlugins": { "dds@dongwha-dds": true }
}
```

### 나만 — 개인 설치

```bash
claude plugin marketplace add bykim820-max/Dongwha_DDS
claude plugin install dds@dongwha-dds
```

터미널이 낯설면 Claude Code 채팅창에 "DDS 플러그인 설치해줘"와 함께 위 두 줄을 붙여넣어도 된다.

어느 쪽이든 Claude Code를 다시 시작하면 적용된다.

## 쓰는 법

| 할 일 | 명령 |
|---|---|
| 이 프로젝트에 DDS 처음 가져오기 | `/dds:init` (버전 지정: `/dds:init 2.5.0`) |
| 새 버전이 나왔나, 올리면 뭘 해야 하나 | `/dds:check` — 읽기만 한다 |
| 새 버전으로 올리기 | `/dds:upgrade` (버전 지정: `/dds:upgrade 2.6.0`) |
| 화면·컴포넌트 만들기 | 그냥 요청하면 된다. `dds:ui` 스킬이 자동으로 규칙을 적용한다 |

## 어떻게 동작하나

- 프로젝트의 `DDS_VERSION` 파일이 기준이다. 플러그인은 **그 버전의 태그**에서 규칙 문서를 읽는다 — 최신 문서가 아니다.
- 토큰 이름은 **프로젝트의 `tokens.css`에 있는 것만** 쓴다. 더 새 버전에서 추가된 토큰을 쓰다가 화면이 깨지는 일을 막는다.
- 새 버전을 쓰려면 `/dds:upgrade`로 **명시적으로** 올린다. 저절로 바뀌지 않는다.
- **새 버전 알림** — DDS를 쓰는 프로젝트에서 Claude Code를 시작하면, 고정 버전보다 새 버전이 있을 때 화면에 한 줄 알린다. 최신이거나 DDS를 안 쓰는 프로젝트, 네트워크가 안 될 때는 아무것도 뜨지 않는다. 버전 조회는 6시간에 한 번만 한다.
- GitHub(`github.com`, `raw.githubusercontent.com`)에 접속할 수 있어야 한다.

## 플러그인 자체 업데이트

```bash
claude plugin update dds
```

**DDS 새 버전이 나왔다고 플러그인을 업데이트할 필요는 없다.** 플러그인은 DDS 버전을 GitHub 태그에서 직접 확인한다. 플러그인 업데이트는 명령 자체가 바뀌었을 때만 필요하다.

## 플러그인 변경 이력

플러그인 버전은 DDS 버전과 별개다. DDS 변경 이력은 [CHANGELOG.md](../../CHANGELOG.md).

| 버전 | 변경 |
|---|---|
| 1.0.1 | `/dds:init`이 프로젝트 설정(`.claude/settings.json`)에 플러그인을 등록 — 커밋하면 팀원 모두가 받는다 |
| 1.0.0 | 최초 — `/dds:init` · `/dds:check` · `/dds:upgrade` · `dds:ui` · 새 버전 시작 알림 |

## 관련 문서

- [MIGRATION.md](../../MIGRATION.md) — 버전 규칙 · 가져가기 · 갱신 절차 (플러그인 없이 하는 법 포함)
- [CHANGELOG.md](../../CHANGELOG.md) — 버전별 변경 이력
- [AGENTS.md](../../AGENTS.md) — 플러그인이 적용하는 규칙의 원본
