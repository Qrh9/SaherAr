
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

import re
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ..core.logger import logging
from ..helpers.functions import edit_or_reply

plugin_category = "admin"
blacklist = ["عير", "word2", "word3"]  # List of words to be blacklisted
LOGS = logging.getLogger(__name__)

@l313l.ar_cmd(
    pattern="قفل_كلمات$",
    command=("قفل_كلمات", plugin_category),
    info={
        "header": "Track and delete messages containing blacklisted words.",
        "usage": "{tr}قفل_كلمات",
    },
)
async def track_delete_messages(event):
    chat = await event.get_chat()
    if not chat.admin_rights:
        return await edit_or_reply(event, "⌔∮ أنا لست مشرفًا في هذه المجموعة.")
    if not chat.admin_rights.delete_messages:
        return await edit_or_reply(event, "⌔∮ ليس لدي صلاحيات حذف الرسائل في هذه المجموعة.")
    reply = await event.get_reply_message()
    if not reply or not reply.message:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على الرسالة للبدء في تتبع الكلمات.")
    await edit_or_reply(event, "⌔∮ تم تنشيط تتبع الكلمات. سيتم حذف الرسائل التي تحتوي على الكلمات المحظورة.")

@l313l.ar_bot(
    pattern=".*",
    from_users=ChannelParticipantsAdmins,
    func=lambda e: e.is_group
)
async def delete_blacklisted_messages(event):
    if not event.message or not event.message.message:
        return
    message_text = event.message.message
    for word in blacklist:
        if re.search(rf"\b{re.escape(word)}\b", message_text, re.I):
            try:
                await event.client.delete_messages(event.chat_id, event.message.id)
            except Exception as e:
                LOGS.error(f"Error deleting message: {e}")
