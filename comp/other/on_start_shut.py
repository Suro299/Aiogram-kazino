import datetime
import time

dt_start = time.time() 

async def on_startup(_):
    dt_for_startup = datetime.datetime.now().strftime("D/Y: [%D, %Y]\nTIME: [%H:%M:%S]\n")
    print(f"=========================\n{dt_for_startup}\nBot Started\n=========================\n\n")
    # await rassilka()

async def on_shutdown(_):
    dt = datetime.datetime.now().strftime("D/Y: [%D, %Y]\nTIME: [%H:%M:%S]\n")
    time_ = f"{round(time.time() - dt_start, 2)}"
    
    if float(time_) >= 60:
        time_ = f"{round((time.time() - dt_start) / 60, 2)} min"
    else:
        time_ = time_ + " sec"

    msg = f"\n=========================\n{dt}\nBot Is Disabled\n\nThe bot was active for {time_}\n=========================\n\n"
    print(msg)
    # await bot.send_message("1621088799", msg)