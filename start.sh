#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-8000}"
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="/tmp/dingkx-slg.log"
PID_FILE="/tmp/dingkx-slg.pid"

if [[ -f "${PID_FILE}" ]] && kill -0 "$(cat "${PID_FILE}")" 2>/dev/null; then
  echo "[dingkx-slg] already running, pid=$(cat "${PID_FILE}")"
  exit 0
fi

cd "${APP_DIR}"
nohup python3 -m http.server "${PORT}" --bind 0.0.0.0 \
  > "${LOG_FILE}" 2>&1 &
echo $! > "${PID_FILE}"

sleep 1
if kill -0 "$(cat "${PID_FILE}")" 2>/dev/null; then
  echo "[dingkx-slg] started ok"
  echo "  pid:  $(cat "${PID_FILE}")"
  echo "  port: ${PORT}"
  echo "  log:  ${LOG_FILE}"
  echo "  dir:  ${APP_DIR}"
else
  echo "[dingkx-slg] start FAILED, last log:"
  tail -n 50 "${LOG_FILE}" || true
  exit 1
fi
