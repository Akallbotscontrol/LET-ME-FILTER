from pyrogram import Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import Script  # Repo ka Script file (yahi se Disclaimer aur Commands ka text aayega)
from plugins.pmfilter import start_menu  # Tumhare start.py ya pmfilter me defined hona chahiye


# === Texts ===
ABOUT_TEXT = """
<b>🤖 About This Bot</b>

Yaha tumhare bot ka intro, features ya jo bhi info dikhani ho wo daal sakte ho.
"""

SUPPORT_TEXT = """
<b>🛠 Support</b>
Yaha support related text daalo.
"""

DEVELOPER_TEXT = """
👨‍💻 <b>Developer</b>
Yaha apna naam, contact ya jo bhi daalna ho.
"""

NETWORK_TEXT = """
🌐 <b>Network</b>
Yaha apna network/channel list daal sakte ho.
"""


# === Buttons Layout ===
def about_buttons():
    return [
        [InlineKeyboardButton("‼️ Disclaimer", callback_data="disclaimer")],
        [
            InlineKeyboardButton("🛠 Support", callback_data="support"),
            InlineKeyboardButton("📜 Commands", callback_data="commands")
        ],
        [
            InlineKeyboardButton("👨‍💻 Developer", callback_data="developer"),
            InlineKeyboardButton("🌐 Network", callback_data="network")
        ],
        [InlineKeyboardButton("⬅️ Back", callback_data="start")]
    ]


def support_buttons():
    return [
        [InlineKeyboardButton("🤖 Bot Support Group", url="https://t.me/YourSupportGroup")],
        [
            InlineKeyboardButton("🤖 Bot Updates", url="https://t.me/YourBotUpdates"),
            InlineKeyboardButton("🎬 Movie Updates", url="https://t.me/YourMovieUpdates")
        ],
        [InlineKeyboardButton("⬅️ Back", callback_data="about")]
    ]


# === Callback Handler ===
@Client.on_callback_query()
async def about_handler(client, query):
    data = query.data

    if data == "about":
        await query.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=InlineKeyboardMarkup(about_buttons()),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )

    elif data == "disclaimer":
        await query.message.edit_text(
            text=Script.DISCLAIMER_TXT,  # repo se uthaya
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="about")]]),
            parse_mode=enums.ParseMode.HTML
        )

    elif data == "support":
        await query.message.edit_text(
            text=SUPPORT_TEXT,
            reply_markup=InlineKeyboardMarkup(support_buttons()),
            parse_mode=enums.ParseMode.HTML
        )

    elif data == "commands":
        await query.message.edit_text(
            text=Script.CMD_TXT,  # repo se uthaya
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="about")]]),
            parse_mode=enums.ParseMode.HTML
        )

    elif data == "developer":
        await query.message.edit_text(
            text=DEVELOPER_TEXT,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="about")]]),
            parse_mode=enums.ParseMode.HTML
        )

    elif data == "network":
        await query.message.edit_text(
            text=NETWORK_TEXT,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="about")]]),
            parse_mode=enums.ParseMode.HTML
        )

    elif data == "start":
        # Yaha tumhara actual start menu function call hoga
        await start_menu(query)
