
import asyncio
import pyrogram
from pyrogram import Client, filters
from driver.filters import command
from pyrogram.types import Message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    BOT_PHOTO,
)


@Client.on_message(command(["يدي","ا","ايديي","ايدي"]) & ~filters.edited)
async def idsd(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    await message.reply_photo(
        photo=f"{BOT_PHOTO}",
        caption=f"""⚜️︙اسمڪ ⇇ {message.from_user.mention}\n\nℹ️︙يوزرڪ ⇇ @{message.from_user.username}\n\n🆔︙ايدِيڪ ⇇ `{message.from_user.id}`\n\n💬︙ايدِي الجـرۆب ⇇ `{message.chat.id}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
                [
                    InlineKeyboardButton("اضف البوت  لمجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],    
            ]
        ),
    )
        
    
