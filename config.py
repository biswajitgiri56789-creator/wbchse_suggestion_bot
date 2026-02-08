import os

# Telegram Bot Token (from GitHub Secrets)
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Telegram Channel ID (numeric, from GitHub Secrets)
CHANNEL_ID = os.environ.get("CHANNEL_ID")

# Post interval (seconds) – optional, default 1 hour
POST_INTERVAL = int(os.environ.get("POST_INTERVAL", 3600))
