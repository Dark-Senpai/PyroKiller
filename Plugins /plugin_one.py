import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from sample_config import Config 

from translation import Dictionary 

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

button = []
#button.append('Support', url="https://t.me/Animes_Encoded_Group")
button.append([InlineKeyboardButton("Support", url="https://t.me/Animes_Encoded_Group")])
# python (c) list 

@pyrogram.Client.on_message(pyrogram.Filters.command(["start", prefix="!"]))
async def start_lady(client, message):
  await client.send_message(
    message.chat.id,
    text=START_TEXT,
    reply_markup=InlineKeyboardMarkup(button)
  )
  
@pyrogram.Client.on_message(pyrogram.Filters.command(["help", prefix="!"]))
async def start_lady(client, message):
  await client.send_message(
    message.chat.id,
    text=ABOUT_TEXT,
    reply_markup=InlineKeyboardMarkup(button)
  )
  




