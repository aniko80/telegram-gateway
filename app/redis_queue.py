import redis
import json
import asyncio
from app.config import REDIS_HOST, REDIS_PORT, N8N_WEBHOOK
from app.webhook_sender import send_to_webhook

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

QUEUE_NAME = "telegram_queue"


async def push_message(data):
    redis_client.rpush(QUEUE_NAME, json.dumps(data))


async def worker():
    while True:
        _, message = redis_client.blpop(QUEUE_NAME)
        data = json.loads(message)

        try:
            await send_to_webhook(data)
        except Exception:
            # retry через 5 секунд
            await asyncio.sleep(5)
            redis_client.rpush(QUEUE_NAME, json.dumps(data))