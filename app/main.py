import asyncio
from app.telegram_client import client
from app.redis_queue import worker


async def main():
    await client.start()
    asyncio.create_task(worker())
    print("Gateway started")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())