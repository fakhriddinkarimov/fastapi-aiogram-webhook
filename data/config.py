from environs import Env
import hashlib


# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
WEB_DOMAIN = env.str("WEB_DOMAIN")  # webhook uchun domen

token_hash = hashlib.md5(BOT_TOKEN.encode())

WEBHOOK_PATH = "/bot/" + token_hash.hexdigest()
WEBHOOK_URL = WEB_DOMAIN + WEBHOOK_PATH
