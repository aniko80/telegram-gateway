import aiohttp
from app.config import N8N_WEBHOOK


async def send_to_webhook(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(N8N_WEBHOOK, json=data) as response:
            if response.status != 200:
                raise Exception("Webhook failed")