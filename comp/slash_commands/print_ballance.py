import sqlite3 as sq

async def slash_bal(message):
    with sq.connect("./data/ballance.db") as con:
        cur = con.cursor()

        cur.execute(f"SELECT ball FROM ballance WHERE chat_id = {message.chat.id}")
        await message.answer(f"Балланс: {cur.fetchall()[0][0]} АМД")

