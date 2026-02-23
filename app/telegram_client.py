from telethon import TelegramClient, events
from telethon.sessions import StringSession
from app.config import TG_API_ID, TG_API_HASH, TG_SESSION_STRING
from app.redis_queue import push_message

client = TelegramClient(
    StringSession(TG_SESSION_STRING),
    TG_API_ID,
    TG_API_HASH
)


@client.on(events.NewMessage)
async def handler(event):
    message_data = {
        "chat_id": event.chat_id,
        "sender_id": event.sender_id,
        "text": event.raw_text
    }

    await push_message(message_data)