import os
import json
from pyrogram import Client, filters
from dotenv import load_dotenv
from app.redis_client import redis_client, QUEUE_NAME

load_dotenv()

app = Client(
    name=os.getenv("TG_NAME"),
    api_id=int(os.getenv("TG_API_ID")),
    api_hash=os.getenv("TG_API_HASH"),
    phone_number=os.getenv("TG_PHONE_NUMBER"),
    workdir="session"
)


@app.on_message(filters.all)
async def handle_message(client, message):
    payload = {
        "chat_id": message.chat.id,
        "message_id": message.id,
        "text": message.text,
        "is_poll": bool(message.poll)
    }

    await redis_client.lpush(QUEUE_NAME, json.dumps(payload))