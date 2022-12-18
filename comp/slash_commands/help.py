from aiogram import types
help_command_reply_commands = """
               
<b> 📒 КОМАНДЫ 📒 </b>

<b>Пополнить баланс --> </b> <em> /addbal </em>
<b>Пример: </b> <em> /addbal 1k </em>

<b>Показать балланс --> </b> <em> /ball </em>

<b>Список достижений --> </b> <em> /dost    ⚠️  [НЕ РАБОТАЕТ]  ⚠️ </em>
"""

help_command_reply_games = """
<b> 🎮 ИГРЫ 🎮 </b>


<b>🎰 /rul</b> <em> (Ставка)    ⚠️  [НЕ РАБОТАЕТ]  ⚠️ </em>

<b>♥️/♠️ /xs </b> <em> (Ставка)    ⚠️  [НЕ РАБОТАЕТ]  ⚠️ </em>

<b>🎲 /rand </b> <em> (Ставка)    ⚠️  [НЕ РАБОТАЕТ]  ⚠️ </em>

<b>🛫 /avi </b> <em> (ставка)      ⚠️  [НЕ РАБОТАЕТ]  ⚠️ </em>

"""

async def slash_help(message):
    reply_markup = types.ReplyKeyboardRemove()
    await message.answer(help_command_reply_commands, parse_mode="HTML", reply_markup=reply_markup)
    await message.answer(help_command_reply_games, parse_mode="HTML")