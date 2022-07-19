
import asyncio
import pyrogram
from pyrogram import Client, filters
from driver.filters import command
from pyrogram.types import Message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_NAME,
    BOT_PHOTO,
)



@Client.on_message(filters.command(BOT_NAME))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""**اي قلبي 🤍😻**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("Ξ𝗜𝗧𝗛𝗢𝗡™ ايثون", url=f"https://t.me/EITHON1"),
            ]
         ]
     )
  )
    
    
    
@Client.on_message(command(["بوت", "وت"]) & ~filters.edited)
async def nammes(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    await message.reply_photo(
        photo=f"{BOT_PHOTO}",
        caption=f"""اسمي {BOT_NAME} الكيوت 🌝♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
                [
                    InlineKeyboardButton("اصنع بوتك", url=f"https://t.me/EITHON1/819"),
                ],    
            ]
        ),
    )
    

    
