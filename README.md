# Playing around with [pydbzengine](https://github.com/memiiso/pydbzengine)

## Quickstart

Create a venv and activate:
```
python -m venv .venv
source .venv/bin/activate
```

Install pydbzengine:
```
pip install "git+https://github.com/memiiso/pydbzengine.git"
```

Deploy a PostgreSQL DB:
```
docker compose up -d
```

Run the pydbzengine-based test script
```
py test.py
```

Run psql:
```
docker exec -it mydb psql -U postgres -d mydb
```

Create a table + do something:
```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- INSERT
INSERT INTO users (name, email) VALUES ('Hans', 'hans@example.com');
INSERT INTO users (name, email) VALUES ('Maria', 'maria@example.com');

-- UPDATE
UPDATE users SET name = 'Hans-Peter' WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 2;
```

And see the magic (=Debezium catches the updates)
