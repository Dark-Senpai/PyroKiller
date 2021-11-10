import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
from sample_config import Config 
from translation import Dictionary 
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
# best of lists work.
button = []
#button.append('Support', url="https://t.me/Animes_Encoded_Group")
button.append([InlineKeyboardButton("Support", url="https://t.me/Animes_Encoded_Group")])
# python (c) list 

@pyrogram.Client.on_message(pyrogram.Filters.command(["start", prefix="!"]))
async def start_lady(client, message):
  await client.send_message(
    message.chat.id,
    text=Dictionary.START_TEXT,
    reply_markup=InlineKeyboardMarkup(button)
  )
  
@pyrogram.Client.on_message(pyrogram.Filters.command(["help", prefix="!"]))
async def help_lady(client, message):
  await client.send_message(
    message.chat.id,
    text=Dictionary.HELP_TEXT
  )
  
@pyrogram.Client.on_message(pyrogram.Filters.command(["about", prefix="!"]))
async def about_lady(client, message):
  await client.send_message(
    message.chat.id,
    text=Dictionary.ABOUT_TEXT
  )