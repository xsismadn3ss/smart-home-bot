from .bot_data import bot, temp

@bot.message_handler(commands=["sign_in"])
async def sign_in(message):
    print("sign in...")
    chatid = message.chat.id
    msgid = message.message_id
    temp[chatid] = "login"
    temp["msgid"] = msgid
    print(chatid, type(chatid))
    await bot.send_message(chatid,"Ingrese la contraseña del bot")


@bot.message_handler(func=lambda message: temp.get(message.chat.id) == "login")
async def sign_in_form(message):
    chatid = message.chat.id
    print(type(message))
    test_password = "1234"
    test = message.text
    if test == test_password:
        await bot.delete_message(chat_id=chatid, message_id=temp["msgid"] + 1)
        await bot.delete_message(chat_id=chatid, message_id=(temp["msgid"]  + 2))
        await bot.send_message(chatid, "Bienvenido")
    else:
        await bot.delete_message(chat_id=chatid, message_id=temp["msgid"] + 1)
        await bot.delete_message(chat_id=chatid, message_id=(temp["msgid"] + 2))
        await bot.send_message(chatid, "Contraseña incorrecta")