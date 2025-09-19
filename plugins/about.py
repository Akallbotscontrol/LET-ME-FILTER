from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from script import ABOUT_TXT   # text script.py se
from command import ABOUT_BUTTONS   # buttons command.py se

@Client.on_callback_query(filters.regex("about"))
async def about_callback(client, query):
    await query.message.edit_text(
        text=ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup(ABOUT_BUTTONS),
        disable_web_page_preview=True
    )
