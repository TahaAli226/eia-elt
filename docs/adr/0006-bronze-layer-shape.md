# 6. Bronze layer shape

Date: 2026-11-20

## Status

Accepted

## Context

The Bronze layer is the source of truth anything down-stream can be rebuilt from it, EIA API sends all data as strings, but we still need to catch the bad data early. 

## Decision

- Keep the original data type, validate shape and numeric-ness at fetch time.
- Nulls are the one non-numeric value allowed through, dbt decides if it's zero or unknown.
- Keeping all fields for normalizing into dimensions down-stream.

## Consequences

- Preserving the data exactly how the API sends it makes it easier to rebuild everything down-stream.
- Type conversion needs to happen down-stream.
- Rejected: converting types at fetch. Bronze won't match the source, and a wrong conversion would require re-fetching.
- Rejected: no validation at fetch. Bad data would show down-stream, which would result in not knowing the source of it straight away.