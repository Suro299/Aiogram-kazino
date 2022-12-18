from aiogram import Bot, Dispatcher, executor, types
import config

from comp.other.reset_db import reset_db 

from comp.slash_commands.set_unset_adm import set_unset_administrator as s_adm

from comp.other.entry_check import entry_check 
import comp.other.on_start_shut as on_start_shut

from comp.slash_commands.user_list import users_list as s_user_list
from comp.slash_commands.admin_list import admin_list as s_admins_list
from comp.slash_commands.start import slash_start as s_start
from comp.slash_commands.help import slash_help as s_help
from comp.slash_commands.print_ballance import slash_bal as s_bal
from comp.slash_commands.add_bal import slash_addball


bot = Bot(config.TELEGRAM_TOKEN)
dp = Dispatcher(bot)

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


# /ul
# =====================================================
@dp.message_handler(commands=["ul", "Ul", "userlist", "uslist"])
async def users_list(message: types.Message):
    if await entry_check(message):
        await s_user_list(message)
    else:
        await message.reply("Аккаунт не найден --> /start")
# =====================================================

# /al
# =====================================================
@dp.message_handler(commands=["al", "Al", "adminlist", "alist", "Alist"])
async def admin_list(message: types.Message):
    if await entry_check(message):
        await s_admins_list(message)
    else:
        await message.reply("Аккаунт не найден --> /start")
# =====================================================



# /adm
#=====================================================
@dp.message_handler(commands=["adm", "Adm"])
async def adm(message: types.Message):
    if await entry_check(message):
        await s_adm(message, bot)
    else:
        await message.reply("Аккаунт не найден --> /start")
#=====================================================


# /start
# =====================================================
@dp.message_handler(commands="start")
async def start(message: types.Message):
    await s_start(message, bot)
# =====================================================


# /help
# =====================================================
@dp.message_handler(commands=["help", "Help", "!"])
async def help(message: types.Message):
    if await entry_check(message):
        await s_help(message)
    else:
        await message.reply("Аккаунт не найден --> /start")
# =====================================================


# /bal
# =====================================================
@dp.message_handler(commands=["bal", "Bal", "ball", "Ball", "ballance", "Ballance"])
async def help(message: types.Message):
    if await entry_check(message):
        await s_bal(message)
    else:
        await message.reply("Аккаунт не найден --> /start")
# =====================================================


# /addbal
# =====================================================
@dp.message_handler(commands=["addbal"])
async def help(message: types.Message):
    if await entry_check(message):
        await slash_addball(message)
    else:
        await message.reply("Аккаунт не найден --> /start")
# =====================================================





if __name__ == "__main__":
    # from comp.other.rass import rassilka 

    executor.start_polling(dp, on_startup=on_start_shut.on_startup, on_shutdown=on_start_shut.on_shutdown)
