from pyrogram import Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# === Texts ===
ABOUT_TEXT = """
<b>🤖 About This Bot</b>

Yaha tumhare bot ka intro, features ya jo bhi info dikhani ho wo daal sakte ho.
"""

DISCLAIMER_TEXT = """
⚠️ <b>Disclaimer</b>
Yaha apna disclaimer daalo.
"""

SUPPORT_TEXT = """
<b>🛠 Support</b>
Yaha support related text daalo.
"""

COMMANDS_TEXT = """
<b>📜 Commands</b>
Yaha commands ki list daalni hai to daal sakte ho.
"""

DEVELOPER_TEXT = """
👨‍💻 <b>Developer</b>
Yaha apna naam, contact ya jo bhi daalna ho.
"""

NETWORK_TEXT = """
🌐 <b>Network</b>
Yaha apna network/channel list daal sakte ho.
"""

# === Buttons ===
def about_buttons():
    return [
        [InlineKeyboardButton("‼️ Disclaimer", callback_data="disclaimer")],
        [InlineKeyboardButton("🛠 Support", callback_data="support")],
        [InlineKeyboardButton("📜 Commands", callback_data="commands")],
        [InlineKeyboardButton("👨‍💻 Developer", callback_data="developer")],
        [InlineKeyboardButton("🌐 Network", callback_data="network")],
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
            text=DISCLAIMER_TEXT,
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
            text=COMMANDS_TEXT,
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
        # Yaha tum apna start menu ya /start ka function call kar sakte ho
        await query.message.edit_text(
            text="🏠 Back to Start Menu",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("About", callback_data="about")]]
            )
        )
