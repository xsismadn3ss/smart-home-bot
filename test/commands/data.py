import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
bot = AsyncTeleBot(BOT_TOKEN)

numbers = {}
