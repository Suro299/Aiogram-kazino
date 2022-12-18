import sqlite3 as sq
from comp.other.rate_conversion import rate_conversion  

async def replen_withd_bal(message, stavka, rd):
    stavka = await rate_conversion(message)
    if stavka != -1:
        with sq.connect("./data/ballance.db") as con:
            cur = con.cursor()

            cur.execute(f"SELECT ball FROM ballance WHERE chat_id = {message.chat.id}")

            if rd == "+":
                try:
                    cur.execute(f"""
                        UPDATE ballance SET ball = '{int(cur.fetchall()[0][0]) + stavka}' WHERE chat_id = {message.chat.id}
                    """)
                except:
                    pass   

            else:
                try:
                    cur.execute(f"""
                        UPDATE ballance SET ball = '{int(cur.fetchall()[0][0]) - stavka}' WHERE chat_id = {message.chat.id}
                    """)
                except:
                    pass
            cur.execute(f"SELECT ball FROM ballance WHERE chat_id = {message.chat.id}")
            await message.answer(f"Балланс: {cur.fetchall()[0][0]} АМД")
    else:
        await message.reply(f"Что то пошло не так проверте сообщение")
        