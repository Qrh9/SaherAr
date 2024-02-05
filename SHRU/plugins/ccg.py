from telethon import events
from SHRU import Qrh9



@Qrh9.on(admin_cmd(pattern="(مميز؟)"))
async def is_vip(event):
    username = event.message.sender.username
    user_id = event.message.sender_id
    
    if username in vip_members or user_id in vip_members.values():
        await event.respond('**هذا عضو مميز بالسورس 🫡**')
    else:
        await event.respond('**ليس عضو مميز**')

