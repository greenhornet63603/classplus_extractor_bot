import os
from pyrogram import Client, filters
from pyrogram.types import Message

bot = Client(
    'classplus_bot',
    api_id=int(os.getenv('27400172')),
    api_hash=os.getenv('56d0a75c5f9a9de6beb5452aa63c2d36'),
    bot_token=os.getenv('8204209080:AAHQx2wvrV1yrLoJgrxswYgLBf_mkzXqKHQ')
)

@bot.on_message(filters.command('start'))
async def start_cmd(client, message: Message):
    await message.reply_text('👋 Welcome to Classplus Extractor Bot!')

# You would include /drm, /batch, /txt handlers here

bot.run()
