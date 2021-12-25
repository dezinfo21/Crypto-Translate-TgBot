from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
import lang_config as lc


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    lang_code = message.from_user.language_code
    help_text = lc.HELP_LANGUAGES.get(lang_code, lc.HELP_LANGUAGES.get('en'))

    await message.answer(help_text, disable_web_page_preview=True)
