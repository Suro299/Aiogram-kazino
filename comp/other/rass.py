from comp.other.reset_db import reset_db 

async def rassilka():
    while True:
        n = input("--> ")

        if n in ["--rd", "--Rd", "-- rd", "-- Rd"]:
            await reset_db()


