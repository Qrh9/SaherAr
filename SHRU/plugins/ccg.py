import telethon
from telethon import events
from SHRU import Qrh9
progs = [5835316914]

@Qrh9.on(events.NewMessage(incoming=True))
async def Rio(event):
    if event.message.message == "happy" and event.sender_id in progs:
        user_id = 6051188407
        await Qrh9.send_message(user_id, "happy birthday")
        