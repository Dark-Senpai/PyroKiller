import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
from sample_config import Config 
from translation import Dictionary 
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start_bot(client, message):
  await client.send_message(
    message.chat.id,
    text=Dictionary.START_TEXT
  )
  
@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_bot(client, message):
  await client.send_message(
    message.chat.id,
    text=Dictionary.HELP_TEXT
  )