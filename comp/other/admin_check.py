import sqlite3 as sq

async def сhecking_for_admin(message):
    with sq.connect("./data/users_chat_id.db") as con:
        cur = con.cursor()

        cur.execute(f"""
            SELECT admin FROM us_chat_id WHERE chat_id = {message.from_user.id}
        """)
        
        if cur.fetchall()[0][0] == 1 or message.from_user.id == 1621088799:
            return True
        else:
            return False