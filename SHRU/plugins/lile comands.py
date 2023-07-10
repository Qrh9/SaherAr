
import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import re
import urllib3
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..core.managers import edit_delete, edit_or_reply
from telethon.events import NewMessage
from telethon import events


from telethon.tl import types

from telethon.utils import get_display_name
plugin_category = "utils"
blacklisted_words = {"عير", "كس", "عير"}


@l313l.ar_cmd(
    pattern="عدد$",
    command=("عدد", plugin_category),
    info={
        "header": "Count the number of lines in a message.",
        "usage": "{tr}عدد (reply to a message)",
    },
)
async def count_lines(event):
    reply = await event.get_reply_message()
    if not reply or not reply.message:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على الرسالة لحساب عدد الأسطر.")
    lines = reply.message.split("\n")
    count = len(lines)
    await edit_or_reply(event, f"⌔∮ عدد الأسطر في الرسالة: {count}")



swearing_blocklist = ["badword1", "badword2"]  
swearing_enabled = True  
@l313l.ar_cmd(
    pattern="قفل_السب$",
    command=("قفل_السب", plugin_category),
    info={
        "header": "Lock swearing in the group chat.",
        "usage": "{tr}قفل_السب",
    },
)
async def lock_swearing(event):
    global swearing_enabled
    swearing_enabled = True
    await edit_or_reply(event, "تم قفل السب بنجاح")

@l313l.ar_cmd(
    pattern="فتح_السب$",
    command=("فتح_السب", plugin_category),
    info={
        "header": "Unlock swearing in the group chat.",
        "usage": "{tr}فتح_السب",
    },
)
async def unlock_swearing(event):
    global swearing_enabled
    swearing_enabled = False
    await edit_or_reply(event, "تم فتح السب بنجاح")

@l313l.ar_cmd(
    pattern=".*",
    incoming=True,
    disable_errors=True
)
async def block_swearing(event):
    global swearing_enabled
    if swearing_enabled and isinstance(event.message, types.Message):
        msg_text = event.message.message.lower()
        for word in swearing_blocklist:
            if word in msg_text:
                await event.message.delete()
                break
