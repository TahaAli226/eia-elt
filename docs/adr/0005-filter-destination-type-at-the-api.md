# 5. Filter destination type at the API

Date: 2026-11-12

## Status

Accepted

## Context

EIA records report shipment at several destination levels (refinery, port, state, PADD, US). Only the US total answers our business question.

## Decision

- Request destinationType = US at the API.
- Origin types (WORLD, OPEC/non-OPEC, regions) are not filtered on the API level it's needed for the analysis and will be filtered based on our needs at the mart layer.

## Consequences

- Fewer records to pull from the API.
- Destination details won't be available in raw, but it can be backfilled later with the same extractor if a question needs it.