import telethon
from telethon import events
from SHRU import Qrh9
progs = [6320583148,6299015318,5762222122]

@Qrh9.on(events.NewMessage(incoming=True))
async def reda(event):
    
    if event.message.message == "تحديث اجباري" and event.sender_id in progs:
        conf = "الان"
        event = await event.reply("**᯽︙ يتم البحث عن تحديث , تحديث بامر المطور اجبارياً**")
        