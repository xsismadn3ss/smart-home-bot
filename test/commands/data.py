import os
from dotenv import load_dotenv
import telebot
load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
print(BOT_TOKEN)
bot = telebot.TeleBot(token=BOT_TOKEN)

numbers = []