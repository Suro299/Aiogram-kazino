import asyncio

async def rate_conversion(message):
    await asyncio.sleep(0)
    try: 
        stavka = int(message.text.split(" ")[1])
        return stavka

    except:
        try:
            return int(message.text.split(" ")[1].lower().replace("k", "000"))
        except:
            return -1
            
