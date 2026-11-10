# ADR 0001: Store raw EIA data as one row per record

Date: 2026-11-10

## Status
Accepted

## Context
On a previous prototype pipeline the extracted data was stored as a single JSON array in one row. Staging 
had to unpack every array on every dbt run, and single records couldn't be queried or indexed in raw.

## Decision
One row per record as EIA sent it with loaded_at and load_id to make each extraction groupable.

## Consequences
- More rows and inserts per run, not an issue at EIA's dataset size.
- Can query and index individual records.