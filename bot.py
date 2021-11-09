import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from sample_config import Config 


if __name__ == "__main__" :
  app = pyrogram.Client(
    'Oh My God 🤯',
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins_dir="Plugins"
  )
  app.run()
