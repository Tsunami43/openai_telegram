from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from utils import Config


class UserMiddleware(BaseMiddleware):
    def __init__(self):
        self.admins = Config.ADMINS

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if event.chat.type == "private":
            if (
                event.from_user.id in self.admins
                or event.from_user.username in self.admins
            ):
                return await handler(event, data)
            else:
                await event.reply("<b>You don't have access</b> ⚠️", parse_mode="HTML")
