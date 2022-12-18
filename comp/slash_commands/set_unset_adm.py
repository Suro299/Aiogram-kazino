import sqlite3 as sq
import time 

from comp.other.admin_check import сhecking_for_admin


async def set_adm(chat_id):
    with sq.connect("./data/users_chat_id.db") as con:
        cur = con.cursor()

        cur.execute(f"""
            UPDATE us_chat_id
            SET admin = 1
            WHERE chat_id = {chat_id};
        """)


async def unset_adm(chat_id):
    with sq.connect("./data/users_chat_id.db") as con:
        cur = con.cursor()

        cur.execute(f"""
            UPDATE us_chat_id
            SET admin = 0
            WHERE chat_id = {chat_id};
        """)



async def set_unset_administrator(message, bot):
    if await сhecking_for_admin(message):
        if len(message.text.split(" ")) == 3:
            mess = message.text.split(" ")[1::]

            with sq.connect("./data/users_chat_id.db") as con:
                cur = con.cursor()

                cur.execute(f"""
                    SELECT full_name, chat_id, admin FROM us_chat_id WHERE chat_id = "{mess[0]}" 
                """)
                user_data = cur.fetchall()[0] 
                
                if (str(user_data[1]) != "1621088799" or str(message.from_user.id) == "1621088799") or str(message.from_user.id) == str(user_data[1]):
                    if mess[1] == "1":

                        if user_data[2] == 0:
                            await set_adm(user_data[1])
                            msg_for_set_adm = f"<b>{user_data[0]}</b> Назначен Админинистратором\n\n\n<b>Админимтратор:</b> {message.from_user.first_name}\n\n<b>Ползователь:</b> {user_data[0]}\n<b>Id:</b> {user_data[1]}\n<b>Время:</b> {time.ctime()}" 
                            await message.reply(msg_for_set_adm, parse_mode="HTML")
                            await bot.send_message(user_data[1], msg_for_set_adm, parse_mode="HTML")
    
                        else:
                            await message.reply(f"<b>{user_data[0]}</b> Уже Является Администратором", parse_mode="HTML")

                    elif mess[1] == "0":
                    
                        if user_data[2] == 1:
                            await unset_adm(user_data[1])
                            msg_for_unset_adm = f"Администратор <b>{user_data[0]}</b> был снят с поста администратора\n\n\n<b>Админимтратор:</b> {message.from_user.first_name}\n\n<b>Ползователь:</b> {user_data[0]}\n<b>Id:</b> {user_data[1]}\n<b>Время:</b> {time.ctime()}"
                            await message.reply(msg_for_unset_adm, parse_mode="HTML")
                            await bot.send_message(user_data[1], msg_for_unset_adm, parse_mode="HTML")
                        else:
                            await message.reply("<b> Данный пользователь не является администратором </b>", parse_mode="HTML")

                    else:
                        await message.reply("/adm (id) (set/unset [0,1]) ")
                else:
                    await message.reply("Нельзя изменить роль этого пользователя")

  
        else:
            await message.reply("/adm (id) (set/unset [0,1]) ")
    else:
        await message.reply("Недостаточно прав")