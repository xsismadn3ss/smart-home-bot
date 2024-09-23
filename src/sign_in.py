from .bot_data import bot, temp

@bot.message_handler(commands=["sign_in"])
async def sign_in(message):
    print("sign in...")
    chatid = message.chat.id
    temp[chatid] = "login"
    print(chatid, type(chatid))
    await bot.reply_to(message,"Ingrese la contraseña del bot")


@bot.message_handler(func=lambda message: temp.get(message.chat.id) == "login")
async def sign_in_form(message):
    chatid = message.chat.id
    print(type(message))
    test_password = "1234"
    test = message.text
    if test == test_password:
        await bot.send_message(chatid, "Bienvenido")
    else:
        await bot.send_message(chatid, "Contraseña incorrecta")