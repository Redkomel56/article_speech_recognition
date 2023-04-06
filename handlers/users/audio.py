import subprocess
import uuid
from aiogram import types

from loader import dp, bot
import speech_recognition as sr
import os


@dp.message_handler(content_types=types.ContentType.VOICE)
async def bot_start(message: types.Message):
    path = "temp"
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_uuid = uuid.uuid4()

    await bot.download_file(file_path, f"{path}/{file_uuid}.mp3")
    subprocess.call(['ffmpeg', '-i', f"{path}/{file_uuid}.mp3",
                     f"{path}/{file_uuid}.wav"])

    r = sr.Recognizer()
    with sr.AudioFile(f"{path}/{file_uuid}.wav") as source:
        audio_data = r.record(source)
    text = r.recognize_google(audio_data, language='ru-RU', show_all=True)
    text = text['alternative'][0]['transcript']

    os.remove(f"{path}/{file_uuid}.wav")
    os.remove(f"{path}/{file_uuid}.mp3")

    await message.answer(f"<b>Расшифровка сообщения:</b>\n\n{text}")
