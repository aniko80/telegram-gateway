import json
import asyncio
from app.redis_client import redis_client, QUEUE_NAME
from app.n8n_client import send_to_n8n
from app.bot import app


async def worker():
    while True:
        event = await redis_client.brpop(QUEUE_NAME, timeout=5)

        if not event:
            continue

        payload = json.loads(event[1])

        response = await send_to_n8n(payload)

        if not response:
            # возвращаем обратно в очередь
            await redis_client.lpush(QUEUE_NAME, json.dumps(payload))
            await asyncio.sleep(2)
            continue

        await execute_action(response)


async def execute_action(response):
    action = response.get("action")

    if action == "reply":
        await app.send_message(
            response["chat_id"],
            response["text"]
        )

    if action == "vote":
        await app.vote_poll(
            response["chat_id"],
            response["message_id"],
            [response["option_index"]]
        )