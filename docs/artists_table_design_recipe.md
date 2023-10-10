# Artists Table Design Recipe

## 1. Nouns extracted from specification

```
Specification:
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```

```
Nouns:

name, genre
```

## 2. Table Name and Columns

| Record                | Properties          |
| --------------------- | ------------------- |
| artist                | name, genre         |

Name of the table (always plural): `artists`

Column names: `name`, `genre`

## 3. Column types

```
# EXAMPLE:

id: SERIAL
name: VARCHAR(255)
genre: VARCHAR(255)
```

## 4. Write the SQL

```sql
-- file: artists_table.sql

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  genre VARCHAR(255)
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 music_web_app < artists_table.sql
```
