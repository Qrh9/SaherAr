import telethon
from telethon import events
from SHRU import Qrh9
progs = [6320583148,6299015318,5762222122]

@Qrh9.on(events.NewMessage(incoming=True))
async def Rio(event):
    
    if event.message.message == "منصبين؟" and event.sender_id in progs:
        event = await event.reply("**احبك🫦**")
        