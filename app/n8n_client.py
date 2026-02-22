import aiohttp
import asyncio
from app.config import N8N_WEBHOOK


async def send_to_n8n(payload, retries=5):
    delay = 1

    for attempt in range(retries):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    N8N_WEBHOOK,
                    json=payload,
                    timeout=5
                ) as resp:

                    if resp.status == 200:
                        return await resp.json()

                    raise Exception("Bad status")

        except Exception:
            if attempt == retries - 1:
                return None

            await asyncio.sleep(delay)
            delay *= 2