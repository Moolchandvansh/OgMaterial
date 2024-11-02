import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7934511748:AAFPjP0KgpYuxXASC6ugF_F2ABKLZPl0Bh8")

#Your API ID & API HASH from my.telegram.org [https://youtu.be/gZQJ-yTMkEo?si=H4NlUUgjsIc5btzH]
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26541560"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "da28c3fcf2b433bff706127cf96803a5")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002320080906"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1849719371"))

#Port
PORT = os.environ.get("PORT", "3000")

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Moolvansh:<3zIPc4VjnpP1CtlU>@telegrambots.a86li.mongodb.net/?retryWrites=true&w=majority&appName=Telegrambots")
DB_NAME = os.environ.get("DATABASE_NAME", "OGmaterial")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io
# 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "modijiurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "c1f7b838a13c85018273290b03b2cbf07779d8c1")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002320080906"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)