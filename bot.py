import json
import random
import time
from datetime import datetime
from config import BOT_TOKEN, CHANNEL_ID, POST_INTERVAL
from telegram import Bot

bot = Bot(token=BOT_TOKEN)

# Load books and posted questions
with open("books_data.json", "r", encoding="utf-8") as f:
    books_data = json.load(f)

try:
    with open("posted_questions.json", "r", encoding="utf-8") as f:
        posted_questions = json.load(f)
except:
    posted_questions = {"11": [], "12": []}

def generate_question(class_num, book_name, chapter):
    """
    AI-style question generator (simple example)
    """
    templates = [
        f"What is the main concept in {chapter} of {book_name}?",
        f"Explain one important point from {chapter} ({book_name}).",
        f"Write a short answer question from {chapter} of {book_name}.",
        f"Summarize key ideas from {chapter} in {book_name}."
    ]
    return random.choice(templates)

def select_random_chapter(class_num):
    class_data = books_data[class_num]
    language = random.choice(list(class_data.keys()))
    lang_data = class_data[language]
    subject = random.choice(list(lang_data.keys()))
    subject_data = lang_data[subject]

    if isinstance(subject_data, list):
        chapter = random.choice(subject_data)
        book_name = subject
    else:
        book = random.choice(subject_data["books"])
        chapter = random.choice(book["chapters"])
        book_name = book["name"]

    return language, subject, book_name, chapter

def post_to_channel():
    while True:
        class_num = random.choice(["11", "12"])
        language, subject, book_name, chapter = select_random_chapter(class_num)

        question = generate_question(class_num, book_name, chapter)

        # Avoid repeat
        if question in posted_questions[class_num]:
            continue
        posted_questions[class_num].append(question)
        with open("posted_questions.json", "w", encoding="utf-8") as f:
            json.dump(posted_questions, f, ensure_ascii=False, indent=2)

        # Prepare message
        message = f"📚 Class {class_num}\n📝 Book/Subject: {book_name}\n📖 Chapter: {chapter}\n❓ Question: {question}\n🕒 {datetime.now().strftime('%d-%m-%Y %H:%M')}"

        try:
            bot.send_message(chat_id=CHANNEL_ID, text=message)
            print(f"Posted: {question}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(POST_INTERVAL)

if __name__ == "__main__":
    post_to_channel()