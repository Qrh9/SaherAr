from telethon import events
from SHRU import Qrh9
import html
import os
from SHRU.core.logger import logging
from ..Config import Config


@Qrh9.on(events.NewMessage(pattern=r"^.مميز\?$"))
async def check_vip_membership(event):
    user_id = replied_user.id
    if user_id in Config.Vip_members:
        await event.reply("نعم، أنت عضو مميز!")
    else:
        await event.reply("لا، أنت لست عضو مميز.")