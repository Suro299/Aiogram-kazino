import sqlite3 as sq
from comp.other.admin_check import сhecking_for_admin

async def users_list(message):
    if await сhecking_for_admin(message):
        with sq.connect("./data/users_chat_id.db") as con:
            cur = con.cursor()
            cur.execute(f"""
                SELECT full_name, chat_id FROM us_chat_id WHERE admin = 0 
            """)
            data = cur.fetchall()

            msg = f"Users  {len(data)}\n\n"
            
            for i in range(len(data)):
                msg += f"{i+1}) {data[i][0]} -- {data[i][1]}\n\n" 
            
            await message.reply(msg)                
    else:
        await message.reply("Недостаточно прав")

