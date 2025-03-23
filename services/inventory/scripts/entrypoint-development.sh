#!/bin/bash
set -e

echo "Starting development initialization..."
# ./scripts/run-migrations.sh

exec fastapi dev ../app/main.py --host 0.0.0.0 --port 8000 --reload
