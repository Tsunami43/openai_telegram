from .client import OpenAIClient
from .redis import RedisClient
from .context_manager import ContextManager

openai_client = OpenAIClient()
redis_client = RedisClient()
context_manager = ContextManager(openai_client, redis_client)
