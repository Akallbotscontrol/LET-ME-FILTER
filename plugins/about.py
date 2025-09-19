from pyrogram import Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import Script  # Direct module import to avoid ImportError
from pmfilter import ABOUT_BUTTONS  # buttons list

@Client.on_callback_query()
async def about_callback(client, query):
    # Check if callback is "about"
    if query.data == "about":
        # Send About text with buttons
        await query.message.edit_text(
            text=Script.ABOUT_TXT,
            reply_markup=InlineKeyboardMarkup(ABOUT_BUTTONS),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
    
    # Optional: handle "back" button
    elif query.data == "start":
        # Import start menu function from wherever it is
        from pmfilter import start_menu  # ensure start_menu exists
        await start_menu(query)

    # Optional: handle group_info button
    elif query.data == "group_info":
        from pmfilter import group_buttons, CHANNELS_TEXT  # define in pmfilter
        await query.message.edit_text(
            text=CHANNELS_TEXT,
            reply_markup=InlineKeyboardMarkup(group_buttons),
            parse_mode=enums.ParseMode.HTML
        )

    # Optional: handle source button
    elif query.data == "source":
        from pmfilter import SOURCE_TEXT, source_buttons
        await query.message.edit_text(
            text=SOURCE_TEXT,
            reply_markup=InlineKeyboardMarkup(source_buttons),
            parse_mode=enums.ParseMode.HTML
        )
