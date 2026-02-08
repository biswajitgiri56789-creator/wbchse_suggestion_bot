import os
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

print("TOKEN:", "OK" if BOT_TOKEN else "MISSING")
print("CHANNEL:", CHANNEL_ID)

bot = Bot(token=BOT_TOKEN)

bot.send_message(
    chat_id=CHANNEL_ID,
    text="✅ Test message from GitHub Actions bot"
)

print("Message sent")
