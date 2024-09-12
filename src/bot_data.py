import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot

load_dotenv()
Bot_tOKEN = os.getenv("BOT_TOKEN")
bot=AsyncTeleBot(Bot_tOKEN)
temp={}