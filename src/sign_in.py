import os
from data import user_queries
from .bot_data import bot, temp
from .fx.reset_temp import reset_temp
from functools import wraps


def check_register(func):
    @wraps(func)
    async def wrapper(message, *args, **kwargs):
        chatid = message.chat.id
        user = user_queries.get(chat_id=chatid)

        if user is not None:
            await bot.send_message(chatid, "Ya estas registrado")
        else:
            return await func(message, *args, **kwargs)
    return wrapper


@bot.message_handler(commands=["sign_in"])
@check_register
async def sign_in(message):
    print("sign in...")
    chatid = message.chat.id
    msgid = message.message_id
    temp[chatid] = "login"
    temp["msgid"] = msgid
    print(chatid, type(chatid))
    await bot.send_message(chatid, "Ingrese la contraseña del bot")


@bot.message_handler(func=lambda message: temp.get(message.chat.id) == "login")
async def sign_in_form(message):

    chatid = message.chat.id
    print(type(message))
    password = os.getenv("PASSWORD")
    test = message.text
    await reset_temp(chatid)

    if test == password:
        await user_queries.insert(chat_id=chatid)
        await bot.send_message(chatid, "Bienvenido")
        await bot.delete_message(chat_id=chatid, message_id=temp["msgid"] + 1)
        await bot.delete_message(chat_id=chatid, message_id=(temp["msgid"] + 2))
    else:
        await bot.send_message(chatid, "Contraseña incorrecta")
        await bot.delete_message(chat_id=chatid, message_id=temp["msgid"] + 1)
        await bot.delete_message(chat_id=chatid, message_id=(temp["msgid"] + 2))
