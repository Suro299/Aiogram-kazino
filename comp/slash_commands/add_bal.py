from comp.other.rate_conversion import rate_conversion
from comp.other.replen_withd_bal import replen_withd_bal



async def slash_addball(message):
    if len(message.text.split(" ")) == 2:
        new_ballance = await rate_conversion(message)
        if new_ballance != -1:
            if new_ballance <= 5000:
                await replen_withd_bal(message, new_ballance, "+")
            else:
                await message.answer("Максимум 5000")
        else:
            await message.answer("/addball (Сколько хотите добавить)\n\nПример:\n/addball 1k")
    else:
        await message.answer("/addball (Сколько хотите добавить)\n\nПример:\n/addball 1k")
