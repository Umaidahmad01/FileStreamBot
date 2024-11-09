from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", "20718334"))
    API_HASH = str(env.get("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "7354750534:AAGWPKjrWZjke9Woh29pp7D6TDJYikbJ2kM"))
    OWNER_ID = int(env.get('OWNER_ID', '7978482443'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL','mongodb+srv://Sukuna:Sukuna123@cluster0.xya73s9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Anime_sub_society"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'society_stream_bot'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', True)
    FORCE_SUB = True if str(FORCE_SUB).lower('-1002132950415 -1001930406310 -1002072642438') == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1002015354644"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002015354644"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "5585016974")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("https://ideological-hally-chuche-7f473a64.koyeb.app/", BIND_ADDRESS))
    URL = "http{anime-sub-society.blogspot.com/2024/11/redirecting-to-your-link-code-credit.html}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



