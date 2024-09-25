from functools import wraps
import aiosqlite
import aiosqlite

def query(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with aiosqlite.connect("bot.db") as conn:
            cursor = await conn.cursor()
            result = await func(conn, cursor, *args, **kwargs)
            await conn.commit()
            await conn.close()
        return result
    return wrapper