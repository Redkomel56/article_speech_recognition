from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Этот бот поможет тебе расшифровать голосовые сообщения.\n\nПросто перешли сообщение и в ответ ты получишь расшифровку")
