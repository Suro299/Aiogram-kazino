from aiogram import Bot, Dispatcher, executor, types
import config
import time
import asyncio
import datetime
import sqlite3 as sq

from comp.other.reset_db import reset_db 

from comp.slash_commands.start import slash_start



bot = Bot(config.TELEGRAM_TOKEN)
dp = Dispatcher(bot)

dt_start = time.time() 

async def on_startup(_):
    dt_for_startup = datetime.datetime.now().strftime("D/Y: [%D, %Y]\nTIME: [%H:%M:%S]\n")
    print(f"=========================\n{dt_for_startup}\nBot Started\n=========================\n\n")
    # await rassilka()

async def on_shutdown(_):
    dt = datetime.datetime.now().strftime("D/Y: [%D, %Y]\nTIME: [%H:%M:%S]\n")
    time_ = f"{round(time.time() - dt_start, 2)}"
    
    if float(time_) >= 60:
        time_ = f"{round((time.time() - dt_start) / 60, 2)} min"
    else:
        time_ = time_ + " sec"

    msg = f"\n=========================\n{dt}\nBot Is Disabled\n\nThe bot was active for {time_}\n=========================\n\n"
    print(msg)
    # await bot.send_message("1621088799", msg)


# /rd
# =====================================================
@dp.message_handler(commands="rd")
async def rd(message: types.Message):
    if message.from_user.id == 1621088799:
        await reset_db()
        await message.reply("Дб обнавленно")

    else:
        await message.reply("Недостаточно прав")
# =====================================================


# /adm
# =====================================================
# @dp.message_handler(commands="adm")
# async def administrator(message: types.Message):
#     if message.from_user.id == 1621088799:
#         msg = message.text.split(" ")[1::]
#         if len(msg) == 2:
#             pass
#             with sq.connect("./data/users_chat_id.db") as con:
#                 cur = con.cursor()

#                 cur.execute(f"""
#                     SELECT full_name, chat_id FROM us_chat_id WHERE admin = 0 
#                 """)
#                 print(cur.fetchall())
#         else:
#             await message.reply("/adm (id) (set/unset [0,1]) ")
#     else:
#         await message.reply("Недостаточно прав")
# =====================================================


# /start
# =====================================================
@dp.message_handler(commands="start")
async def start(message: types.Message):
    print("as")
    await slash_start(message)
# =====================================================




if __name__ == "__main__":
    # from comp.other.rass import rassilka
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
