# 3. Init scripts instead of migration tools for raw tables

Date: 2026-11-11

## Status

Accepted

## Context

- In this pipeline dbt manages the pipeline and rebuilds the tables it owns on every run.
- The only tables outside dbt are the raw and log tables.

## Decision

Raw tables will be created with init scripts instead of migration tools like Alembic.

## Consequences

- Simple setup a fresh database comes up fully set up with docker compose up.
- Harder to migrate, but the schema will need little to no migration because the EIA data is stored inside jsonb untouched.
- The init scripts only run on an empty database.