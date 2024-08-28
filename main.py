import telebot
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(token=BOT_TOKEN)
print("bot initialized")

numbers = []


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Hola, bienvenido!!!")


@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(
        message,
        "Este es un bot de prueba hecho en telegram\n\nEjecuta comandos presionando el boton de menu o con '/[comando]'",
    )


@bot.message_handler(commands=["hour"])
def send_time(message):
    import datetime

    now = datetime.datetime.now()
    print("sending time")
    bot.reply_to(message, f"Son las {now.hour}:{now.minute}")


@bot.message_handler(commands=["save_data"])
def save_number(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Ingresa un numero para guardar")
    bot.register_next_step_handler(message, process_number)


def process_number(message):
    try:
        numero = int(message.text)
        numbers.append(numero)
        bot.send_message(message.chat.id, f"Numero {numero} guardado exitosamente")
    except ValueError:
        bot.send_message(message.chat.id, "Por favor envia un número valido")


@bot.message_handler(commands=["get_numbers"])
def load_numbers(message):
    try:
        msg = ""
        for i in numbers:
            msg += f"{i}\n"
        bot.reply_to(message, msg)
    except Exception as e:
        bot.send_message(message.chat.id, "Aún no hay información guardada")


# reapeat message
@bot.message_handler(func=lambda message: True)
def repeat(message):
    print("replying")
    bot.reply_to(message, f"{message.text}")


bot.polling()
