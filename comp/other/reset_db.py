import asyncio
import sqlite3 as sq


async def reset_db():
    with sq.connect("./data/ballance.db") as con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS ballance")
        cur.execute("""CREATE TABLE IF NOT EXISTS ballance (
            full_name TEXT NOT NULL,
            chat_id TEXT NOT NULL,
            ball INTEGER NOT NULL DEFAULT 0
        )""")


    # 0 - user
    # 1 - administrator
    with sq.connect("./data/users_chat_id.db") as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS us_chat_id")
        cur.execute("""CREATE TABLE IF NOT EXISTS us_chat_id (
            reg_date TEXT NOT NULL,
            full_name TEXT NOT NULL,
            chat_id TEXT NOT NULL,
            admin INTEGER NOT NULL DEFAULT 0
        )""")

    with sq.connect("./data/xax_qan.db") as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS xax_qan")
        cur.execute("""CREATE TABLE IF NOT EXISTS xax_qan (
            full_name TEXT NOT NULL,
            chat_id TEXT NOT NULL,
            Ruletka TEXT NOT NULL DEFAULT "0 0 0",
            Random TEXT NOT NULL DEFAULT "0 0 0",
            Xs TEXT NOT NULL DEFAULT "0 0 0",
            obsh_win INTEGER NOT NULL DEFAULT 0,
            obsh_loss INTEGER NOT NULL DEFAULT 0,
            obsh INTEGER NOT NULL DEFAULT 0
        )""")
    await asyncio.sleep(0)