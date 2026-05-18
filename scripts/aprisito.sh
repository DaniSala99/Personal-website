#!/bin/bash
set -e

echo "🚀 Avviando il dev server..."
cd "$(dirname "$0")/.."
npm run dev > /tmp/astro-dev.log 2>&1 &
DEV_PID=$!

echo "⏳ Aspettando che il server sia pronto..."
for i in {1..30}; do
  if curl -s http://localhost:4321 > /dev/null 2>&1; then
    echo "✨ Server pronto!"
    echo "🌐 Aprendo il browser..."
    if command -v xdg-open > /dev/null; then
      xdg-open http://localhost:4321
    elif command -v open > /dev/null; then
      open http://localhost:4321
    else
      echo "Apri manualmente: http://localhost:4321"
    fi
    break
  fi
  sleep 0.5
done

wait $DEV_PID
