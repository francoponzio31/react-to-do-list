-- create dbs
CREATE DATABASE api_db;

-- create user
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_user
        WHERE  usename = 'db_admin') THEN

        CREATE ROLE db_admin LOGIN PASSWORD 'db_admin';
    END IF;
END
$$;

GRANT ALL PRIVILEGES ON DATABASE api_db TO db_admin;

-- create tables
\connect api_db;

CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    text TEXT,
    done BOOLEAN DEFAULT FALSE
);