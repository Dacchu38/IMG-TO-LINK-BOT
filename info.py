from os import environ

def str_to_bool(val):
    return str(val).lower() in {"true", "yes", "1", "t", "y"}

# ── ᴀᴠ ʙᴏᴛᴢ ─────────────────────────────
# ᴜᴘᴅᴀᴛᴇs  : https://t.me/AV_BOTz_UPDATE
# ᴏᴡɴᴇʀ    : @AV_OWNER_BOT
# sᴜᴘᴘᴏʀᴛ  : https://t.me/AV_SUPPORT_GROUP
# ᴄʀᴇᴅɪᴛ   : ᴀᴠ ʙᴏᴛᴢ | ᴀᴍᴀɴ ᴠɪsʜᴡᴀᴋᴀʀᴍᴀ
# ────────────────────────────────────────

API_ID = int(environ.get('API_ID', '29388536'))
API_HASH = environ.get('API_HASH', '1795cfeb72fdd9741bbaab5e02c57668')
BOT_TOKEN = environ.get("BOT_TOKEN", "8603670245:AAEKVivPfBB6rKwSJzPdjAT_QCIhUg0ayuU")
PORT = environ.get("PORT", "8080")
START_PIC = environ.get("START_PIC", "https://files.catbox.moe/045zcm.jpg")

# ── ᴀᴠ ʙᴏᴛᴢ ─────────────────────────────
# ᴜᴘᴅᴀᴛᴇs  : https://t.me/AV_BOTz_UPDATE
# ᴏᴡɴᴇʀ    : @AV_OWNER_BOT
# sᴜᴘᴘᴏʀᴛ  : https://t.me/AV_SUPPORT_GROUP
# ᴄʀᴇᴅɪᴛ   : ᴀᴠ ʙᴏᴛᴢ | ᴀᴍᴀɴ ᴠɪsʜᴡᴀᴋᴀʀᴍᴀ
# ────────────────────────────────────────

ADMINS = list(map(int, environ.get("ADMINS", "5912466219").split()))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003888435322"))
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://rai:rai@cluster0.fktwown.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# ── ᴀᴠ ʙᴏᴛᴢ ─────────────────────────────
# ᴜᴘᴅᴀᴛᴇs  : https://t.me/AV_BOTz_UPDATE
# ᴏᴡɴᴇʀ    : @AV_OWNER_BOT
# sᴜᴘᴘᴏʀᴛ  : https://t.me/AV_SUPPORT_GROUP
# ᴄʀᴇᴅɪᴛ   : ᴀᴠ ʙᴏᴛᴢ | ᴀᴍᴀɴ ᴠɪsʜᴡᴀᴋᴀʀᴍᴀ
# ────────────────────────────────────────

AUTH_CHANNEL = list(map(int, environ.get("AUTH_CHANNEL", "").split()))
AUTH_REQ_CHANNEL = list(map(int, environ.get("AUTH_REQ_CHANNELS", "-1002220670718").split()))
FSUB = str_to_bool(environ.get("FSUB", "True"))
AUTH_PICS = environ.get("AUTH_PICS", "https://files.catbox.moe/sg2tnu.jpg")
CHANNEL = environ.get("CHANNEL", "https://t.me/DVITTALBOTZ")
SUPPORT = environ.get("SUPPORT", "https://t.me/DVITTALBOTZ_DISSCUSSION")
APP_URL = environ.get("APP_URL", "https://manual-nikolia-totzvvv-5115e05f.koyeb.app/")

