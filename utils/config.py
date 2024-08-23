from dotenv import load_dotenv

load_dotenv()


import os
import re


def prepare(list_str: str):
    pattern = r"(?:'([^']*)'|(\d+))"
    matches = re.findall(pattern, list_str)

    result = []
    for match in matches:
        if match[0]:  # Если нашли строку
            result.append(match[0])
        elif match[1]:  # Если нашли число
            result.append(int(match[1]))

    return result


TELEGRAM_BOT_TOKEN = os.getenv("telegram_bot_token")
OPEN_AI_TOKEN = os.getenv("open_ai_token")
ADMINS = prepare(os.getenv("admins"))
REDIS_URL = os.getenv("redis_url")
