# EIA-ELT
ELT pipeline for US energy imports from the EIA API
 Link: https://www.eia.gov/opendata/

## Business context
- **Stakeholder:** a market analyst at SOMO, Iraq's state oil marketing company.
- **Question:** Is Iraq's percentage of US heavy and medium crude imports falling while Canada's rises over the past year?
- **Decisions:** Suggest to management to export more to other countries, and investigate the cause of the decline.
- **Out of scope:** EIA data doesn't include crude prices, so pricing decisions are outside this pipeline's scope.

## Overview
A small data warehouse for EIA data, starting with crude oil imports and designed to add more endpoints:

1. Fetch current and historical data from the API.
2. Validate the data and the schema.
3. Load the raw data into the database as JSON, one document per record, after validation.
4. Build the warehouse layers (raw/staging/marts).
5. Use the marts layer to build the BI reports and dashboards.

## Tools
- **Extraction:** custom Python extractor.
- **Database and loading:** PostgreSQL instead of a dedicated OLAP database, since the dataset is small.
- **Transformation:** dbt.
- **BI:** Superset.
- **Orchestration:** Airflow.
- **Server:** VPS, AWS (S3).

## Decisions
Architecture decisions are recorded as ADRs in [docs/adr](docs/adr/).

## Roadmap

### Extraction
- [ ] Python extractor with pagination and retries
- [ ] Validation with pydantic
- [ ] Lookback window and backfill through the same code

### Loading
- [x] Raw schema from a versioned SQL init script
- [ ] One JSON document per record, with load timestamp

### Transformation
- [ ] dbt staging: flatten, clean, dedup to latest per key
- [ ] dbt marts: star schema, origin level from ID prefix
- [ ] dbt tests, including reconciliation

### BI
- [ ] Superset dashboard on the marts, read-only role

### Orchestration and ops
- [ ] Docker Compose for the full stack
- [ ] Airflow DAG: monthly runs and backfill
- [ ] CI with GitHub Actions
- [ ] Backups with a tested restore

### Later
- [ ] Natural gas imports (second endpoint)
- [ ] Deploy to VPS, raw backups to S3
- [ ] AWS migration