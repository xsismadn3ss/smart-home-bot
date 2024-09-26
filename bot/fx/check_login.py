from data import user_queries
from bot.bot_data import bot
from functools import wraps

def login_required(func):
    @wraps(func)
    async def wrapper(message, *args, **kwargs):
        chatid = message.chat.id
        user = await user_queries.get(chat_id=chatid)

        if user is None:
            await bot.send_message(chatid, "Necesitas iniciar sesión...")
        else:
            return await func(message, *args, **kwargs)
    return wrapper