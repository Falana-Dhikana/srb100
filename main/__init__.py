#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("API_ID", default=7338003139, cast=int)
API_HASH = config("API_HASH", default="AAGiAYUP7dIhX8s383c6jA4roEs0iBA9qdc")
BOT_TOKEN = config("BOT_TOKEN", default=7338003139:AAGiAYUP7dIhX8s383c6jA4roEs0iBA9qdc)
SESSION = config("SESSION", default="BQG17rgAFWtWqO97IIkez_OSad6PDQUXTmSmcfUEevV4O38hPIIuEF52XgYvSyjGGECpcKDuf7mRK9ivAzLcJJPenBxW3StOX4LOxWePqc0rt1UA1MTVeTVgeaINIjJOxAIbXeL95e3i7TOnoXTx8V4SDw2EH04OP085METsKg7A3aIIFfyAEJ1B1IXo9unmLhgIu1Yn9XbDqZzDSNwWd32ba4u7EMrU1IVd8G98HdTwVFY1BbYVYCtSaFF6FSHBtkg1CAmAIki8aKz8PB-e8ELG4gDEdhzQ8R_RphC7pPuvVMX0zJPbu2GQkZWbtnqMViHr5Vdc841ZqZP77C2b8jzIjmZz8QAAAAErSvw7AA")
FORCESUB = config("FORCESUB", default="Genetry")
AUTH = config("AUTH", default=6163696719)
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
