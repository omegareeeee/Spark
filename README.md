# Spark

> TODO: one or two sentences on what Spark does and who it's for.

Spark stores ideas and comments, embeds ideas as vectors, and clusters them so related ideas can be grouped and explored.

## Tech stack

| Layer | Tools |
| --- | --- |
| API | FastAPI, Uvicorn, Pydantic |
| Database | PostgreSQL + [pgvector](https://github.com/pgvector/pgvector), SQLAlchemy, psycopg 3 |
| Migrations | Alembic |
| ML / clustering | NumPy, scikit-learn, UMAP, HDBSCAN, joblib |
| LLMs | OpenAI, Anthropic |
| Tooling | [uv](https://docs.astral.sh/uv/) for dependency management |

## Prerequisites

- Python 3.12 or 3.13 (a C compiler may be needed if `hdbscan` has no prebuilt wheel for your Python version; pinning 3.12 with `uv python pin 3.12` is the easy fix)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Docker](https://docs.docker.com/get-docker/) with Docker Compose (runs Postgres + pgvector)
- An OpenAI API key and an Anthropic API key

## Getting started

### 1. Clone and install

```bash
git clone git@github.com:omegareeeee/Spark.git
cd Spark/backend
uv sync
```

### 2. Start Postgres with Docker Compose

From the repo root:

```bash
docker compose up -d
docker compose ps
```

The database service should show as running (or healthy). Postgres is exposed on `localhost:5433` with user `app`, password `app`, and database `connect`.

The `vector` extension is enabled by the first Alembic migration, so there is nothing else to set up.

To stop or reset it:

```bash
docker compose stop        # stop, keep data
docker compose down        # remove containers, keep data volume
docker compose down -v     # remove containers AND delete all data
```

### 3. Configure environment variables

Create `backend/.env` (it is gitignored, so never commit it):

```dotenv
DATABASE_URL=postgresql+psycopg://app:app@localhost:5433/connect
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

A `backend/.env.example` with placeholder values should be committed so others know what to set.

### 4. Run migrations

```bash
uv run alembic upgrade head
```

The initial migration enables the `vector` extension and creates the schema, including the `vector(384)` embedding column on `ideas`.

### 5. Start the API

```bash
uv run uvicorn app.main:app --reload
```

The API is served at http://localhost:8000 and interactive docs at http://localhost:8000/docs.

> Adjust `app.main:app` if your entry point lives elsewhere.

## Project structure

```
Spark/
├── docker-compose.yml      # Postgres + pgvector
└── backend/
    ├── app/                # FastAPI application (models, routes, DB session)
    ├── migrations/         # Alembic environment and versions
    ├── alembic.ini
    ├── pyproject.toml
    └── .env                # local secrets (gitignored)
```

> TODO: update to match the real layout, and add the frontend if there is one.

## Database migrations

Alembic is the only thing that should create or alter tables. Do not call `Base.metadata.create_all()`.

```bash
# After changing models: generate a migration
uv run alembic revision --autogenerate -m "describe the change"

# Always read the generated file before applying it.
# Watch for unexpected drop_table / drop_column calls.

# Apply
uv run alembic upgrade head

# Roll back one revision
uv run alembic downgrade -1

# Check that models and database agree
uv run alembic check
```

Notes:

- New model modules must be imported in `migrations/env.py`, or autogenerate will not see them and may try to drop their tables.
- Migrations that use `Vector` columns need `import pgvector.sqlalchemy`. This is already in `script.py.mako`.
- Vector indexes (HNSW / IVFFlat) are not detected by autogenerate; add them by hand in a dedicated migration.

## Resetting the dev database

This deletes all data:

```bash
psql postgresql://app:app@localhost:5433/connect \
  -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
uv run alembic upgrade head
```

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `No module named 'psycopg2'` | `DATABASE_URL` must start with `postgresql+psycopg://` so SQLAlchemy uses psycopg 3. |
| `type "vector" does not exist` | The database image must include pgvector (e.g. `pgvector/pgvector:pg16`), and the first migration must run `CREATE EXTENSION IF NOT EXISTS vector` before creating tables. |
| `connection refused` on port 5433 | The container isn't running. Start it with `docker compose up -d` and check `docker compose ps`. |
| `NameError: name 'pgvector' is not defined` in a migration | Add `import pgvector.sqlalchemy` to the migration file. |
| Autogenerate wants to drop your tables | Your models are not imported in `env.py`, or the database has tables from outside Alembic. |
| `zsh: no matches found: uvicorn[standard]` | Quote extras: `uv add "uvicorn[standard]"`. |
| GitHub rejects a push for secrets | Remove the secret from history, rotate the key, and make sure `.env` is in `.gitignore`. |

## Security

- Never commit `.env` or API keys. If a key is ever pushed or exposed, revoke and rotate it immediately.
- Keep `.env.example` limited to placeholder values.

## License

> TODO: add a license.
