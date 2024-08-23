from aiogram.filters import BaseFilter
from aiogram.types import Message
from utils import Config


class AdminFilter(BaseFilter):
    chat_type = "private"
    admins = Config.ADMINS

    async def __call__(self, message: Message) -> bool:  # [3]
        return message.chat.type == self.chat_type and (
            message.from_user.id in self.admins
            or message.from_user.username in self.admins
        )
