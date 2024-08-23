# Telegram Bot with OpenAI and Redis

Этот проект представляет собой Telegram бота, который использует OpenAI для генерации ответов и Redis для хранения контекста беседы. Бот запускается в Docker-контейнере, но также можно установить и запустить его в виртуальном окружении Python.

## Основные особенности

- **Telegram Bot**: Интерфейс для общения с пользователями через Telegram.
- **OpenAI Integration**: Использует OpenAI для обработки и генерации текстов.
- **Redis Context**: Хранение и управление контекстом беседы с использованием Redis.
- **Docker Support**: Легкий запуск и развертывание с помощью Docker.

## Установка и запуск

### Использование Docker

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/Tsunami43/openai_telegram.git
    cd openai_telegram
    ```

2. **Создайте файл `.env` в корневом каталоге проекта:**

    ```env
    open_ai_token=your_openai_token_here
    telegram_bot_token=your_telegram_bot_token_here
    admins=['...', 111]
    redis_port=6379
    redis_url=redis://redis:${redis_port}
    ```

3. **Запустите Docker Compose:**

    ```bash
    docker-compose up --build
    ```

   Docker Compose создаст и запустит контейнеры для вашего бота и Redis. Бот будет доступен через Telegram.

### Использование виртуального окружения

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/Tsunami43/openai_telegram.git
    cd openai_telegram
    ```

2. **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Создайте файл `.env` в корневом каталоге проекта:**

    ```env
    open_ai_token=your_openai_token_here
    telegram_bot_token=your_telegram_bot_token_here
    admins=['...', 111]
    redis_port=6379
    redis_url=redis://localhost:${redis_port}
    ```

5. **Запустите Redis (если не используете Docker):**

    Убедитесь, что Redis запущен на порту 6379. Если Redis не установлен, вы можете установить его, следуя [инструкциям по установке Redis](https://redis.io/download).

6. **Запустите бота:**

    ```bash
    python main.py
    ```

## Конфигурация

В файле `.env` можно настроить следующие параметры:

- `open_ai_token`: Токен доступа к OpenAI API.
- `telegram_bot_token`: Токен вашего Telegram бота.
- `admins`: Список идентификаторов администраторов бота.
- `redis_port`: Порт, на котором Redis будет слушать. Обычно это 6379.
- `redis_url`: URL для подключения к Redis.

## Зависимости

- Python 3.10 или новее
- Docker (для запуска через Docker)
- Redis (можно установить локально или использовать Docker)

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, создайте [issue](https://github.com/Tsunami43/openai_telegram/issues)

---

Удачи с вашим проектом!
