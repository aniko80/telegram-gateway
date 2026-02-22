import asyncio
from pyrogram import idle
from app.bot import app
from app.worker import worker


async def main():
    await app.start()
    asyncio.create_task(worker())
    await idle()
    await app.stop()


if __name__ == "__main__":
    asyncio.run(main())