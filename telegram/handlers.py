import asyncio
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from AI import redis_client, context_manager

router = Router()


@router.message(Command("start"))
async def handler_start(message: Message):
    full_name = message.from_user.full_name if message.from_user.full_name else "Привет"
    greeting = f"👋 <b>{full_name}</b>!\n\n"
    description = (
        "Я бот, который поможет вам общаться с AI. Вот список команд, которые я поддерживаю:\n\n"
        "⚙️ <b>/start</b> или <b>/info</b> — Показать это сообщение.\n"
        "🧹 <b>/clear</b> — Очистить контекст беседы.\n\n"
        "Просто отправьте мне сообщение, и я постараюсь ответить на ваш запрос!\n"
        "⚠️ Замечание: Пока я генерирую ответ, любые дополнительные сообщения не будут учтены."
    )

    await message.reply(greeting + description, parse_mode="HTML")


@router.message(Command("clear"))
async def handler_clear(message: Message):
    await redis_client.clear_context(message.from_user.id)
    await message.reply("<b>Контекст очищен</b> 🧹", parse_mode="HTML")


@router.message(F.text)
async def handler_request(message: Message):
    loading_message = await message.reply("<b>Идет генерация</b>", parse_mode="HTML")
    try:
        response_task = asyncio.create_task(
            context_manager.get_response_with_context(
                message.from_user.id, message.text.strip()
            )
        )

        k = 0
        while not response_task.done():
            if k == 3:
                new_text = f"<b>{loading_message.text[:-6]}</b>"
                k = 0
            else:
                new_text = f"<b>{loading_message.text} .</b>"
                k += 1
            loading_message = await loading_message.edit_text(
                new_text, parse_mode="HTML"
            )
            await asyncio.sleep(0.3)

        response = await context_manager.get_response_with_context(
            message.from_user.id, message.text.strip()
        )

        # Отправляем сгенерированный ответ
        await loading_message.edit_text(response, parse_mode="Markdown")

    except Exception as e:
        await loading_message.edit_text(
            "<b>Произошла ошибка во время генерации ответа</b> ⚠️", parse_mode="HTML"
        )
        print(f"Error: {e}")
