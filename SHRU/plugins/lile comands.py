
import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import urllib3
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..core.managers import edit_delete, edit_or_reply
from telethon.events import NewMessage
from telethon import events
from ..helpers.functions import edit_delete
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


locked_words = ["كس"]
blocked_messages = {}

@l313l.ar_cmd(
    pattern="قفل_السبيفك$",
    command=("قفل_السبيفك", plugin_category),
    info={
        "header": "Lock messages containing specific words.",
        "usage": "{tr}قفل_السبيفك",
    },
)
async def lock_spam(event):
    global blocked_messages
    chat_id = event.chat_id
    blocked_messages[chat_id] = True
    await edit_or_reply(event, "⌔∮ تم قفل رسائل السبام.")

@l313l.ar_cmd(
    pattern="فتح_السبيفك$",
    command=("فتح_السبيفك", plugin_category),
    info={
        "header": "Unlock messages containing bad words.",
        "usage": "{tr}فتح_السبيفك",
    },
)
async def unlock_spam(event):
    global blocked_messages
    chat_id = event.chat_id
    blocked_messages.pop(chat_id, None)
    await edit_or_reply(event, "⌔∮ تم فتح رسائل السبام.")

@l313l.ar_bot_cmd(incoming=True)
async def block_spam(event):
    global blocked_messages
    chat_id = event.chat_id
    if chat_id in blocked_messages:
        message = event.message
        text = message.message.lower()
        for word in locked_words:
            if word in text:
                await message.delete()
                break
