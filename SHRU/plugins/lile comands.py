
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
blocked_words = ["bad", "inappropriate", "spam"]

@l313l.ar_cmd(
    pattern=r"قفل_السبيفك$",
    command=("قفل_السبيفك", plugin_category),
    info={
        "header": "Locks down the specified words.",
        "usage": "{tr}قفل_السبيفك",
    },
)
async def lock_swear_words(event):
    global blocked_words
    blocked_words = []
    await edit_delete(event, "⌔∮ تم قفل الكلمات بنجاح.", time=5)

@l313l.ar_cmd(
    pattern=r"فتح_السبيفك$",
    command=("فتح_السبيفك", plugin_category),
    info={
        "header": "Unlocks the previously locked words.",
        "usage": "{tr}فتح_السبيفك",
    },
)
async def unlock_swear_words(event):
    global blocked_words
    blocked_words = ["نيج", "عير ", "كس"]
    await edit_delete(event, "⌔∮ تم فتح الكلمات بنجاح.", time=5)

@events.register(events.NewMessage(incoming=True))
async def delete_swear_words(event):
    if event.is_private or not event.message or not event.message.message:
        return
    message_text = event.message.message.lower()
    if any(word in message_text for word in blocked_words):
        await event.delete()
