#!/bin/bash
set -e

echo "Starting production initialization..."
./scripts/wait-for-db.sh db
./scripts/run-migrations.sh

exec fastapi run app/main.py --host 0.0.0.0 --port 8000 --workers 4