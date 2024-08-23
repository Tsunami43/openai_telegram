from openai import AsyncOpenAI
from utils import Config
from loguru import logger


class OpenAIClient:
    def __init__(self):
        self.client = AsyncOpenAI(
            # This is the default and can be omitted
            api_key=Config.REDIS_URL,
            timeout=30,
        )

    async def get_response(self, messages: list) -> str:
        try:
            chat_completion = await self.client.chat.completions.create(
                messages=messages,
                model="gpt-3.5-turbo",
            )
            logger.info("Received response from OpenAI.")
            return chat_completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error during OpenAI API call: {e}")
            raise

    # async def get_response_stream(self, messages: list) -> str:
    #     stream = await self.client.chat.completions.create(
    #         model="gpt-4",
    #         messages=messages,
    #         stream=True,
    #     )
    #     async for chunk in stream:
    #         print(chunk.choices[0].delta.content or "", end="")
