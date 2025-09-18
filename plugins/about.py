from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query(filters.regex("^about$"))
async def about_callback(client, query):
    await query.message.edit_text(
        text=(
            "╔════❰ 𝘼𝘽𝙊𝙐𝙏 𝙈𝙀 ❱════╗\n\n"
            "> **My Name :** LUCY BOT\n"
            "> **Creator :** AQUiB\n"
            "> **Library :** Pyrogram\n"
            "> **Language :** Python\n"
            "> **Database :** MongoDB\n"
            "> **Hosted On :** VPS\n"
            "> **Build Status :** v3 [Advance]\n\n\n"
            "> Maintained by - [『 AK_BOTZ_UPDATE 』](https://t.me/AK_BOTZ_UPDATE)\n\n"
            "╚════════════════════╝"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‼️ DISCLAIMER ‼️", callback_data="disclaimer")],
                [
                    InlineKeyboardButton("• SUPPORT •", url="https://t.me/YourSupportGroup"),
                    InlineKeyboardButton("• DEVELOPER •", url="https://t.me/YourUsername")
                ],
                [InlineKeyboardButton("• BACK •", callback_data="home")]
            ]
        ),
        disable_web_page_preview=True  # hyperlink ka preview hide karega
    )
