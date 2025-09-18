from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query()
async def about_callback(client, query):
    if query.data == "about":
        await query.message.edit_text(
            text=(
                "╔════❰ 𝘼𝘽𝙊𝙐𝙏 𝙈𝙀 ❱════╗\n\n"
                "○ **My Name :** LET_ME_FILTER\n"
                "○ **Creator :** MR_ABHAY\n"
                "○ **Library :** Pyrogram\n"
                "○ **Language :** Python\n"
                "○ **Database :** MongoDB\n"
                "○ **Hosted On :** RENDER\n"
                "○ **Build Status :** v3 [Advance]\n\n"
                "╚════════════════════╝"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("‼️ DISCLAIMER ‼️", callback_data="disclaimer")],
                    [InlineKeyboardButton("• SUPPORT •", url="https://t.me/AK_BOTZ_SUPPORT")],
                    [InlineKeyboardButton("• DEVELOPER •", url="https://t.me/MR_ABHAY_K")],
                    [InlineKeyboardButton("• BACK •", callback_data="home")]
                ]
            )
        )
