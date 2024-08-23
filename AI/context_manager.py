from .client import OpenAIClient
from .redis import RedisClient
from loguru import logger


class ContextManager:
    def __init__(self, openai_client: OpenAIClient, redis_client: RedisClient):
        self.openai_client = openai_client
        self.redis_client = redis_client

    async def get_response_with_context(self, user_id: int, user_message: str) -> str:
        try:
            context = await self.redis_client.get_context(user_id)

            # Присоединяем сообщение пользователя к контексту
            context.append({"role": "user", "content": user_message})

            # Получаем ответ от OpenAI
            response_text = await self.openai_client.get_response(context)

            # Добавляем ответ ассистента в контекст
            context.append({"role": "assistant", "content": response_text})

            # Сохраняем обновленный контекст в Redis
            await self.redis_client.save_context(user_id, context)

            logger.info(f"Response with context generated for user_id: {user_id}.")
            return response_text
        except Exception as e:
            logger.error(f"Error generating response for user_id {user_id}: {e}")
            raise

    async def clear_context(self, user_id: str):
        try:
            await self.redis_client.clear_context(user_id)
            logger.info(f"Context cleared for user_id: {user_id}.")
        except Exception as e:
            logger.error(f"Error clearing context for user_id {user_id}: {e}")
            raise
