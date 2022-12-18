import sqlite3 as sq


async def entry_check(message):
    with sq.connect("./data/users_chat_id.db") as con:
        cur = con.cursor()
        cur.execute(f"""
            SELECT chat_id FROM us_chat_id WHERE chat_id = {message.chat.id} 
        """)
        if cur.fetchall() == []:
            return False
        else:
            return True