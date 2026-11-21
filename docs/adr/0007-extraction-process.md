# 7. Extraction strategy

Date: 2026-11-21

## Status

Accepted

## Context

- EIA caps each response at 5,000 rows.
- With the US destination filter (see ADR-0005), one month is roughly 50–100 rows.
- EIA revises data: new months are preliminary and usually revised the following month, annual data is revised within the year, and historical data can be revised at any time (EIA MER revision policy).
- EIA's `total` can be higher than the rows it actually returns (2012-01: 96 of 100, confirmed by paging).


## Decision

- Requests are made per month. Within each month, offset pagination acts as a safety net in case a month ever exceeds 5,000 rows.
- Rows are sorted ascending by the natural key `period` + `originId` + `gradeId`, verified unique on 2025-03 and 2012-01. `destinationId` is not needed because of the US filter (see ADR-0005).
- Completeness: the run fails if a page is truncated or more rows arrive than `total`. If fewer rows arrive than `total`, a warning is logged with both numbers.
- Initial run: full backfill from `2009-01` (EIA's start period).
- Every regular run re-fetches the last 12 months to catch revisions. A full backfill runs once a year to catch older revisions.
- All fetched rows are appended to bronze (see ADR-0001). Nothing is updated or deleted.
- `extraction.py` only contains functions; nothing runs on import. The API key is passed in as an argument. Two entry scripts decide what to fetch: `scripts/backfill.py` (full history) and `scripts/monthly.py` (the last 12 months), with Airflow scheduling both.
- The fetch function returns a list per month. No generator, since each month is small and bounded.

## Alternatives considered

- Offset-paging the whole dataset in one sweep: rows can shift between requests, causing duplicates or gaps.
- Per-month requests without offset: silently truncates if a month ever exceeds 5,000 rows.
- Fetching only new months: misses EIA's revisions.
- Delete-and-replace re-fetched months: loses revision history and conflicts with the insert-only loader.
- Failing when received ≠ `total`: would crash the backfill on months like 2012-01.
- A generator over the whole range: unnecessary, since chunking by month already bounds memory.

## Consequences

- Each month can be retried and logged independently, and truncation cannot pass silently.
- Bronze holds several versions of the same natural key; dbt staging keeps the latest by `loaded_at`.
- Bronze keeps a full revision history, which can be used to measure how far back EIA actually revises and to tune the 12-month window.
- A full backfill is about 210 small requests.
- The sort order depends on the natural key staying unique; this should be enforced later with a primary key or dbt test.
- The 12-month window is based on EIA's general MER revision policy and is provisional until measured.