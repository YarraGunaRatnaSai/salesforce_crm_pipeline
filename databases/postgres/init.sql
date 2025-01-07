CREATE USER integration_admin WITH ENCRYPTED PASSWORD 'password';
CREATE DATABASE integration_data;
GRANT ALL PRIVILEGES ON DATABASE integration_data TO integration_admin;

\c integration_data;

CREATE TABLE metadata (
    id SERIAL PRIMARY KEY,
    key VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
