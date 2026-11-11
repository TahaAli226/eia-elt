# 4. UTC instead of local time

Date: 2026-11-11

## Status

Accepted

## Context

Timestamps come from Postgres now(), Airflow, AWS all of them use UTC by default  

## Decision

Timestamps are stored as timestamptz column in the raw tables using UTC time and converted to local time only for display

## Consequences

- Comparing between tools will be easier since they all have the same timeline 
- When reading raw data we must remember that the time is set to UTC