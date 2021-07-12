DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY
    tag VARCHAR(255),
    description text
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    id INT REFERENCES merchants(id),
    date VARCHAR(255),
    amount INT
    tag_id INT REFERENCES tags(id)
);
