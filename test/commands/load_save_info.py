from .data import bot
from .data import numbers

@bot.message_handler(commands=["save_data"])
def save_number(message):
    print("ask info")
    chat_id = message.chat.id
    bot.send_message(chat_id, "Ingresa un numero para guardar")
    bot.register_next_step_handler(message, process_number)


def process_number(message):
    try:
        print("saving info...")
        numero = int(message.text)
        numbers.append(numero)
        bot.send_message(message.chat.id, f"Numero {numero} guardado exitosamente")
    except ValueError:
        bot.send_message(message.chat.id, "Por favor envia un número valido")


@bot.message_handler(commands=["get_numbers"])
def load_numbers(message):
    try:
        print("loading info...")
        msg = ""
        for i in numbers:
            msg += f"{i}\n"
        bot.reply_to(message, msg)
    except Exception as e:
        bot.send_message(message.chat.id, "Aún no hay información guardada")