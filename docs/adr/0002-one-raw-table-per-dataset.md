# 1. One raw table per dataset

Date: 2026-11-10

## Status

Accepted

## Context

The EIA API offers multiple datasets that include crude oil, gas and other energy data with each dataset having different units, volumes, lookback windows and backfill dates. 

## Decision

One raw table per dataset with the extractor deciding where to put each dataset by an explicit config for each dataset.

## Consequences

- Each table will have its own dbt tests and validations.
- Can delete or update the entire table without touching the other tables.
- Each new dataset needs a config and a new table in the init script.