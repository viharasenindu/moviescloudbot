import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(20675514)
API_HASH = '5a82ce3aa5e5345af178278f6536744d'
BOT_TOKEN = '5514369553:AAGF693VbOxnv56L1hh96O25WMt3ZPszVUk'

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [5739535897]
CHANNELS = [-1001646992718]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = -1001552415260
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = 'mongodb+srv://mihiran:nithya98@D@cluster0.ejhjaqc.mongodb.net/?retryWrites=true&w=majority)'
DATABASE_URI = ''
DATABASE_NAME = 'mangodb'
COLLECTION_NAME = 'Telegram_files'
OMDB_API_KEY = c78ed305

# Messages
default_start_msg = """
Hello 👋 I'm Movies & TV Series bot 
★ Here you can search files in Inline mode as well as PM
★ Use the below buttons to search files or send me the name of file to search
Enjoy 😊
"""
START_MSG = environ.get('START_MSG', default_start_msg)

BUTTON = environ.get("BUTTON",False)
FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
