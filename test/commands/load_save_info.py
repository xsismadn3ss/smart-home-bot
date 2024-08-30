from .data import bot
from .data import numbers
from telebot.async_telebot import AsyncTeleBot

@bot.message_handler(commands=["save_data"])
async def save_number(message):
    print("ask info")
    chat_id = message.chat.id
    numbers[chat_id] = 'waiting_for_number'
    await bot.send_message(chat_id, "Ingresa un numero para guardar")


@bot.message_handler(func=lambda message: numbers.get(message.chat.id)== 'waiting_for_number')
async def process_number(message):
    try:
        print("saving info...")
        numero = int(message.text)
        await bot.send_message(message.chat.id, f"Numero {numero} guardado exitosamente")
        numbers[message.chat.id] = None
    except ValueError:
        await bot.send_message(message.chat.id, "Por favor envia un número valido")


@bot.message_handler(commands=["get_numbers"])
async def load_numbers(message):
    try:
        print("loading info...")
        msg = ""
        for i in numbers:
            msg += f"{i}\n"
        await bot.reply_to(message, msg)
    except Exception as e:
        await bot.send_message(message.chat.id, "Aún no hay información guardada")