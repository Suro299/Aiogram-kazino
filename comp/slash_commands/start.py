import time
import sqlite3 as sq
from comp.keyboard_buttons.help_kb import kb_help_for_start

    
async def slash_start(message):
    with sq.connect("./data/ballance.db") as con:
        cur = con.cursor()
        try:
            cur.execute(f"""
                DELETE FROM ballance WHERE chat_id = {message.from_user.id}
            """)
        except:
            pass

        cur.execute(f"""
            INSERT INTO ballance (full_name, chat_id)
            VALUES("{message.from_user.first_name},{message.from_user.last_name}", "{message.from_user.id}");
        """)
    #=========================================================================

    with sq.connect("./data/users_chat_id.db") as con:
        cur = con.cursor()

        try:
            cur.execute(f"""
                DELETE FROM us_chat_id WHERE chat_id = {message.from_user.id}
            """)
        except:
            pass
        

        cur.execute(f"""
            INSERT INTO us_chat_id (reg_date, full_name, chat_id)
            VALUES("{time.ctime()}", "{message.from_user.first_name},{message.from_user.last_name}", "{message.from_user.id}");
        """)
    #=========================================================================

    with sq.connect("./data/xax_qan.db") as con:
        cur = con.cursor()
        try:
            cur.execute(f"""
                DELETE FROM xax_qan WHERE chat_id = {message.from_user.id}
            """)
        except:
            pass

        cur.execute(f"""
            INSERT INTO xax_qan (full_name, chat_id)
            VALUES("{message.from_user.first_name},{message.from_user.last_name}", "{message.from_user.id}");
        """)
    #=========================================================================
    await message.answer("<b>Аккаунт создан</b>", parse_mode="HTML")
    await message.answer("Что бы узнать как использовать бота -> /help", reply_markup=kb_help_for_start)