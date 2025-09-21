from pyrogram import Client, enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Script import script
from plugins.commands import send_start_menu

# === Texts ===
ABOUT_TXT = """<blockquote><b>❍ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/LetmeFilter_bot">LetMeFilter ʙᴏᴛ</a>
❍ ᴄʀᴇᴀᴛᴏʀ : <a href="https://t.me/mr_abhay_k">MR. ABHAY</a>
❍ ʟɪʙʀᴀʀʏ : <a href="https://pyrogram.org/">ᴘʏʀᴏɢʀᴀᴍ</a>
❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
❍ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href="https://t.me/AK_BOTZ_UPDATE">RENDER</a>
❍ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ : ᴠ3 [ᴀᴅᴠᴀɴᴄᴇ]</blockquote>
\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/AK_BOTZ_UPDATE">AK BOTZ UPDATE</a></blockquote>

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍᴇ.</b>"""

SUPPORT_TXT = """ᴛʜᴇsᴇ ᴀʀᴇ ᴍʏ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ. ɪғ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ʀᴇᴘᴏʀᴛ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ
\n<blockquote>ᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href="https://t.me/AK_BOTZ_UPDATE"> ᴀᴋ_ʙᴏᴛᴢ_ᴜᴘᴅᴀᴛᴇ </a> </blockquote>"""

DEVELOPER_TEXT = """
👨‍💻 <b>Developer</b>
\n<blockquote>‣ 👑 CREATER 👑: <a href="https://t.me/AK_BOTZ_UPDATE">✨ MR. ABHAY ✨</a></blockquote>
"""

NETWORK_TEXT = """
🌐 <b>OUR NETWORK</b>

<blockquote>
✨ Explore our network of bots, groups & channels.  
Stay updated with movies, join our community, and never miss an update!
</blockquote>
"""

# === Buttons ===
def network_buttons():
    return [
        [
            InlineKeyboardButton("🎬 Movie Updates", url="https://t.me/YourMovieUpdates"),
            InlineKeyboardButton("🎥 Movie Group", url="https://t.me/YourMovieGroup")
        ],
        [
            InlineKeyboardButton("🛠 Support", url="https://t.me/YourSupportGroup"),
            InlineKeyboardButton("🤖 Bot Updates", url="https://t.me/YourBotUpdates")
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="about")
        ]
    ]

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

# === Handler ===
@Client.on_callback_query(filters.regex("^(about|disclaimer|support|commands|developer|network|start)$"))
async def about_handler(client, query):
    data = query.data

    if data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT,
            reply_markup=InlineKeyboardMarkup(about_buttons()),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
        await query.answer()

    elif data == "disclaimer":
        await query.message.edit_text(
            text=script.DISCLAIMER_TXT,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="about")]]
            ),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
        await query.answer()

    elif data == "support":
        await query.message.edit_text(
            text=SUPPORT_TXT,
            reply_markup=InlineKeyboardMarkup(support_buttons()),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
        await query.answer()

    elif data == "commands":
        await send_start_menu(client, query, is_callback=True)
        await query.answer()

    elif data == "developer":
        await query.message.edit_text(
            text=DEVELOPER_TEXT,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Back", callback_data="about")]]
            ),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
        await query.answer()

    elif data == "network":
        await query.message.edit_text(
            text=NETWORK_TEXT,
            reply_markup=InlineKeyboardMarkup(network_buttons()),
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )
        await query.answer()

    elif data == "start":
        await send_start_menu(client, query, is_callback=True)
        await query.answer()
