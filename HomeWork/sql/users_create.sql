CREATE TABLE IF NOT EXISTS users(
id SERIAL PRIMARY KEY,
name VARCHAR(24) NOT NULL,
email VARCHAR(24) NOT NULL UNIQUE
);