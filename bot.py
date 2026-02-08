import json
import random
import os
from datetime import datetime
from telegram import Bot

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

bot = Bot(token=BOT_TOKEN)

with open("books_data.json", "r", encoding="utf-8") as f:
    books_data = json.load(f)

try:
    with open("posted_questions.json", "r", encoding="utf-8") as f:
        posted = json.load(f)
except:
    posted = {"11": [], "12": []}

def generate_question(book, chapter):
    templates = [
        f"{chapter} অধ্যায়ের মূল ধারণা লেখো।",
        f"{chapter} থেকে একটি গুরুত্বপূর্ণ প্রশ্ন লেখো।",
        f"{chapter} অধ্যায়ের সংক্ষিপ্ত প্রশ্ন তৈরি করো।",
        f"Explain the core idea of {chapter}."
    ]
    return random.choice(templates)

def run_once():
    class_num = random.choice(["11", "12"])
    class_data = books_data[class_num]

    lang = random.choice(list(class_data.keys()))
    subject = random.choice(list(class_data[lang].keys()))
    data = class_data[lang][subject]

    if isinstance(data, list):
        chapter = random.choice(data)
        book = subject
    else:
        book_data = random.choice(data["books"])
        book = book_data["name"]
        chapter = random.choice(book_data["chapters"])

    question = generate_question(book, chapter)

    if question in posted[class_num]:
        return

    posted[class_num].append(question)
    with open("posted_questions.json", "w", encoding="utf-8") as f:
        json.dump(posted, f, ensure_ascii=False, indent=2)

    message = (
        f"📚 Class {class_num}\n"
        f"📖 Book: {book}\n"
        f"📘 Chapter: {chapter}\n"
        f"❓ Question:\n{question}\n\n"
        f"🕒 {datetime.now().strftime('%d-%m-%Y %H:%M')}"
    )

    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    run_once()
