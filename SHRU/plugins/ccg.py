from telethon import events
from SHRU import Qrh9
import html
import os
from SHRU.core.logger import logging
from ..Config import Config
@Qrh9.on(admin_cmd(pattern="(مميز؟)"))
async def is_vip(event):
    user_id = event.message.sender_id
    
    if user_id in Config.Vip_members():
        await event.respond('**هذا عضو مميز بالسورس 🫡**')
    else:
        await event.respond('**ليس عضو مميز**')