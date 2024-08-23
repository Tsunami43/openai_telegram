import aioredis
from loguru import logger
from utils import Config


class RedisClient:
    def __init__(self):
        self.redis_url = Config.REDIS_URL

    async def _get_client(self):
        return await aioredis.from_url(self.redis_url, decode_responses=True)

    async def save_context(self, user_id: int, context: list):
        try:
            client = await self._get_client()
            await client.set(f"context:{user_id}", str(context))
            await client.close()
            logger.info(f"Context saved for user_id: {user_id}.")
        except Exception as e:
            logger.error(f"Error saving context for user_id {user_id}: {e}")
            raise

    async def get_context(self, user_id: int) -> list:
        try:
            client = await self._get_client()
            context = await client.get(f"context:{user_id}")
            await client.close()
            logger.info(f"Context retrieved for user_id: {user_id}.")
            return eval(context) if context else []
        except Exception as e:
            logger.error(f"Error retrieving context for user_id {user_id}: {e}")
            raise

    async def clear_context(self, user_id: int):
        try:
            client = await self._get_client()
            await client.delete(f"context:{user_id}")
            await client.close()
            logger.info(f"Context cleared for user_id: {user_id}.")
        except Exception as e:
            logger.error(f"Error clearing context for user_id {user_id}: {e}")
            raise
