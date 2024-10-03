#!/bin/bash

# Create database and user if not already present
PGPASSWORD="${POSTGRES_PASSWORD}" psql -U "$POSTGRES_USER" -d postgres -c "CREATE DATABASE IF NOT EXISTS \"${DB_NAME}\";"
PGPASSWORD="${POSTGRES_PASSWORD}" psql -U "$POSTGRES_USER" -d postgres -c "CREATE USER \"${DB_USER}\" WITH PASSWORD '${DB_PASSWORD}';"
PGPASSWORD="${POSTGRES_PASSWORD}" psql -U "$POSTGRES_USER" -d postgres -c "GRANT ALL PRIVILEGES ON DATABASE \"${DB_NAME}\" TO \"${DB_USER}\";"
