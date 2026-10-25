import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN","http://localhost:3000")

EMBED_MODEL = "text-embedding-3-small"
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")

# Complement scoring: ideas should be related but not identical
SIM_CENTER = 0.55   # tune on your seed data
SIM_WIDTH = 0.15
TOP_K = 3           # matches returned
STORE_K = 5         # matches stored per idea