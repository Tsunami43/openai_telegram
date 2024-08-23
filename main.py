import asyncio
from loguru import logger
import os, sys
from telegram import bot

logger.add(
    sys.stderr, format="{time} {level} {message}", filter="sub.module", level="INFO"
)
if not os.path.exists("logs"):
    os.makedirs("logs")
logger.add(
    "logs/file_{time}.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="5 MB",
)
import asyncio


async def main():
    logger.info("Starting project...")
    await bot.run()
    logger.info("Ending project...")


if __name__ == "__main__":
    asyncio.run(main())
# end main
