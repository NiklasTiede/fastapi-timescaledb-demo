CREATE TABLE call_records (
    id SERIAL PRIMARY KEY,
    caller VARCHAR(200) NOT NULL,
    word_count INT NOT NULL,
    call_started_at TIMESTAMPTZ NOT NULL,
    call_ended_at TIMESTAMPTZ NOT NULL
);

CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;


SELECT create_hypertable('call_records', 'call_started_at');
