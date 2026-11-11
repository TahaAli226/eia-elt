create schema if not exists raw; 

create table if not exists raw.crude_oil_imports(
    raw_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    payload jsonb not null,
    loaded_at timestamptz not null default now(),    
    load_id uuid not null
);