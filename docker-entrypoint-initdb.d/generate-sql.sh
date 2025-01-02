#!/bin/bash
set -e

echo "Current ENVIRONMENT: $ENVIRONMENT"
# source .env.${ENVIRONMENT}

# Ensure the PostgreSQL database is running
wait_for_postgres() {
    until PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -c "\q"; do
        echo "PostgreSQL is not ready yet. Retrying in 2 seconds..."
        sleep 2
    done
}

# Wait for PostgreSQL to be up and running
wait_for_postgres

# Connect to the PostgreSQL server and create schema/initialize data
psql -h localhost -U postgres <<EOF
CREATE USER ${POSTGRES_USER} WITH PASSWORD '${POSTGRES_PASSWORD}';
CREATE DATABASE ${POSTGRES_DB};
GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_USER};
EOF

echo "Database initialized successfully."
