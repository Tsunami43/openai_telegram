from loguru import logger
from utils import Config
from aiogram import Bot, Dispatcher
from .middlewares import UserMiddleware
from .handlers import router

bot = Bot(Config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
dp.message.outer_middleware(UserMiddleware())


async def run():
    try:

        await bot.delete_webhook(drop_pending_updates=True)
        dp.include_router(router)

        bot_info = await bot.get_me()
        logger.info(f"Starting bot @{bot_info.username}[{bot_info.id}]")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as exc:
        logger.critical(exc)
        raise
    finally:
        logger.info("Stopping bot")
        await bot.session.close()
