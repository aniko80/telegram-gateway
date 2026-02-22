import os
from pathlib import Path

SESSION_DIR = Path("session")
SESSION_DIR.mkdir(exist_ok=True)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

N8N_WEBHOOK = os.getenv("N8N_WEBHOOK")