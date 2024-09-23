from .bot_data import bot, temp

@bot.message_handler(commands=["sign_in"])
async def sign_in(message):
    print("sign in...")
    chatid = message.chat.id
    print(chatid, type(chatid))
    await bot.reply_to(message,"Ingrese su usuario")