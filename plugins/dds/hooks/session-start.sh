#!/usr/bin/env bash
# DDS 새 버전 알림 (SessionStart)
#
# DDS를 쓰는 프로젝트를 열면, 프로젝트에 고정된 버전보다 새 버전 태그가 있을 때 화면에 한 줄 알린다.
# 조용히 넘어가는 경우: DDS를 안 쓰는 프로젝트 · 이미 최신 · 네트워크 실패 · DDS 저장소 자체.
# 어떤 경우에도 세션 시작을 막지 않는다 — 항상 exit 0.

DDS_REPO="${DDS_REPO:-https://github.com/bykim820-max/Dongwha_DDS.git}"
CACHE="${TMPDIR:-/tmp}/dds-latest-version"
CACHE_MINUTES=360
dir="${CLAUDE_PROJECT_DIR:-$PWD}"

cd "$dir" 2>/dev/null || exit 0

# DDS 저장소 자체에서는 알리지 않는다
[ -f VERSION ] && [ -f plugins/dds/.claude-plugin/plugin.json ] && exit 0

# 프로젝트 안의 파일 찾기 — git 저장소면 git이 아는 파일만, 아니면 얕게 탐색
find_files() {
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    git ls-files --cached --others --exclude-standard -- "*$1" 2>/dev/null | head -5
  else
    find . -maxdepth 5 \( -name node_modules -o -name .git -o -name dist -o -name build \) -prune -o -name "$1" -print 2>/dev/null | head -5
  fi
}

current=""
legacy=""
vfile="$(find_files DDS_VERSION | head -1)"
if [ -n "$vfile" ]; then
  current="$(tr -d ' \r\n' < "$vfile" | sed 's/^v//')"
else
  for t in $(find_files tokens.css); do
    header="$(head -5 "$t" 2>/dev/null)"
    v="$(printf '%s' "$header" | grep -oE 'DDS v[0-9]+\.[0-9]+\.[0-9]+' | head -1 | sed 's/DDS v//')"
    if [ -n "$v" ]; then current="$v"; break; fi
    printf '%s' "$header" | grep -qE 'DDS v2\.0 ' && { legacy="$t"; break; }
  done
fi

# DDS를 안 쓰는 프로젝트
[ -z "$current" ] && [ -z "$legacy" ] && exit 0

# 레거시 파일 — v2.4.0 이전 파일은 헤더가 전부 v2.0이라 실제 버전을 모른다
if [ -n "$legacy" ]; then
  cat <<JSON
{"systemMessage": "DDS 버전 기록이 없습니다 ($legacy 헤더가 v2.0으로 표기된 구버전 파일). /dds:check 로 실제 버전과 새 버전을 확인하세요.",
 "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "이 프로젝트의 DDS 토큰 파일($legacy)은 v2.4.0 이전에 배포된 파일이다. 헤더가 내용과 무관하게 v2.0으로 찍혀 있어 실제 버전을 알 수 없다. UI 작업 시 토큰 이름은 이 파일에 있는 것만 쓴다. 사용자가 DDS 버전을 물으면 /dds:check 를 권한다."}}
JSON
  exit 0
fi

# 최신 버전 — 6시간 캐시, 없으면 태그 조회
latest=""
if [ -f "$CACHE" ] && [ -n "$(find "$CACHE" -mmin -$CACHE_MINUTES 2>/dev/null)" ]; then
  latest="$(cat "$CACHE" 2>/dev/null)"
fi
if [ -z "$latest" ]; then
  latest="$(GIT_TERMINAL_PROMPT=0 git ls-remote --tags --refs "$DDS_REPO" 'v*' 2>/dev/null \
    | sed -n 's#.*refs/tags/v\([0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\)$#\1#p' \
    | sort -t. -k1,1n -k2,2n -k3,3n | tail -1)"
  [ -z "$latest" ] && exit 0
  printf '%s' "$latest" > "$CACHE" 2>/dev/null
fi

# 최신이면 조용히
[ "$current" = "$latest" ] && exit 0
newest="$(printf '%s\n%s\n' "$current" "$latest" | sort -t. -k1,1n -k2,2n -k3,3n | tail -1)"
[ "$newest" != "$latest" ] && exit 0

cat <<JSON
{"systemMessage": "DDS v$latest 이 나왔습니다 (이 프로젝트: v$current). /dds:check 로 무엇이 바뀌었는지 확인하세요.",
 "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "이 프로젝트는 DDS v$current 에 고정되어 있고, 새 버전 v$latest 이 있다. UI 작업 시 토큰 이름은 프로젝트 tokens.css에 있는 것만 쓴다 — 새 버전 문서에만 있는 토큰을 쓰지 않는다. 사용자가 원하면 /dds:check(영향 분석) · /dds:upgrade(올리기)를 안내한다. 사용자가 묻지 않았는데 업그레이드를 진행하지 않는다."}}
JSON
exit 0
