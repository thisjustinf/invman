#!/bin/bash
set -e

echo "Starting staging initialization..."
./scripts/wait-for-db.sh db
./scripts/run-migrations.sh

exec uvicorn app.main:app --host 0.0.0.0 --port 8000