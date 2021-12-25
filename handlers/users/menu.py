from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
import lang_config as lc


def get_language_kb():
    kb = types.InlineKeyboardMarkup(row_width=2)
    btns = (
        types.InlineKeyboardButton(
            text=lc.AVAILABLE_LANGUAGES[lang]['text'],
            url=lc.AVAILABLE_LANGUAGES[lang]['link'])
        for lang in lc.AVAILABLE_LANGUAGES.keys()
    )

    kb.add(*btns)

    return kb


@dp.message_handler(state='*', commands=['menu'])
async def bot_menu(message: types.Message):
    lang_code = message.from_user.language_code
    menu_text = lc.CHOOSE_CHANNEL_LANGUAGES.get(lang_code, lc.CHOOSE_CHANNEL_LANGUAGES.get('en'))

    kb = get_language_kb()

    await message.answer(text=menu_text, reply_markup=kb)