from aiogram import types

from loader import dp
import lang_config as lc


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    lang_code = message.from_user.language_code
    echo_text = lc.ECHO_LANGUAGES.get(lang_code, lc.ECHO_LANGUAGES.get('en'))

    await message.answer(text=echo_text, disable_web_page_preview=True)
