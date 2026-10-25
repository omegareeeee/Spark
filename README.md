# Connect Backend: Local Setup

This guide gets the backend running on your machine so you can develop and test the frontend against it. Expect about 10 minutes.

## What you'll have when you're done

- Postgres running locally on port **5433**
- The backend API running locally on port **8000** (TODO: confirm)
- The backend accepting requests from the frontend at `http://localhost:3000`

## Prerequisites

Install these first:

- **Git**
- **Docker** and Docker Compose (for the database)
- **TODO: runtime**, e.g. Node 20+ or Python 3.11+
- An **OpenAI API key** (ask me for the shared dev key, or create your own at https://platform.openai.com/api-keys)

## 1. Clone the repo

```bash
git clone TODO_REPO_URL
cd TODO_REPO_NAME
```

## 2. Configure environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Then open `.env` and set:

| Variable | What it does | Notes |
|---|---|---|
| `DATABASE_URL` | Postgres connection string | Default works with the Docker setup below. Don't change unless you changed the compose file. |
| `OPENAI_API_KEY` | Key used for LLM calls | **Required.** Never commit this. |
| `LLM_MODEL` | Model name | Default `gpt-4o` is fine. |
| `FRONTEND_ORIGIN` | Allowed CORS origin | Must match where your frontend runs. Default is `http://localhost:3000`. |

> `.env` is gitignored. Only `.env.example` is committed.

## 3. Start the database

```bash
docker compose up -d db
```

Check that it's healthy:

```bash
docker compose ps
```

The database listens on host port **5433** (not the default 5432), so it won't clash with a Postgres you may already have installed.

## 4. Install dependencies

```bash
# TODO: replace with the real command, e.g.
# npm install
# pip install -r requirements.txt
```

## 5. Run database migrations

```bash
# TODO: replace with the real command, e.g.
# npm run migrate
# alembic upgrade head
```

## 6. Start the backend

```bash
# TODO: replace with the real command, e.g.
# npm run dev
# uvicorn app.main:app --reload --port 8000
```

You should see the server start on `http://localhost:8000`.

## 7. Verify it works

```bash
curl http://localhost:8000/health
```

TODO: confirm the health route. You should get a `200 OK` response.

## 8. Point the frontend at it

In the frontend's env file, set the API base URL to the backend, for example:

```dotenv
# TODO: use the real variable name your frontend expects
API_URL=http://localhost:8000
```

Then start the frontend as usual. It should be served from `http://localhost:3000`, which is what the backend allows by default. If you run the frontend on a different port, update `FRONTEND_ORIGIN` in the backend `.env` and restart the backend.

## Troubleshooting

**CORS errors in the browser console**
`FRONTEND_ORIGIN` doesn't match the URL in your address bar. It must match exactly, including the port and `http` vs `https`. Restart the backend after changing it.

**`connection refused` on the database**
Make sure the container is running (`docker compose ps`) and that `DATABASE_URL` uses port `5433`.

**Port 5433 already in use**
Something else is using it. Stop that process, or change the host port in `docker-compose.yml` and update `DATABASE_URL` to match.

**LLM calls fail with 401 or "invalid API key"**
Check that `OPENAI_API_KEY` is set in `.env` with no quotes or trailing spaces, then restart the backend.

**Env changes don't take effect**
The backend only reads `.env` on startup. Restart it.

## Resetting your local database

This wipes all local data:

```bash
docker compose down -v
docker compose up -d db
# then re-run migrations (step 5)
```

## Stopping everything

```bash
docker compose down
```

Stop the backend with `Ctrl+C` in its terminal.

## Still stuck?

Message me with the exact error and the command you ran.
