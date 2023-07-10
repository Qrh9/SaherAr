
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
from ..helpers.functions import edit_delete
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


plugin_category = "utils"
blacklisted_words = [عير]

@l313l.ar_cmd(
    pattern="قفل_السب$",
    command=("قفل_السب", plugin_category),
    info={
        "header": "Add words to a blacklist.",
        "description": "Add the specified word(s) to the blacklist. Messages containing these words will be deleted.",
        "usage": "{tr}قفل_السب <word(s)>",
        "examples": ["{tr}قفل_السب fuck", "{tr}قفل_السب fuck\nsex"],
    },
    groups_only=True,
    require_admin=True,
)
async def lock_words(event):
    global blacklisted_words
    words = event.pattern_match.group(1).split("\n")
    for word in words:
        word = word.strip()
        if word:
            blacklisted_words.append(word.lower())
    await edit_or_reply(event, "⌔∮ تم قفل الكلمات بنجاح.")

@l313l.ar_cmd(
    pattern="فتح_السب$",
    command=("فتح_السب", plugin_category),
    info={
        "header": "Remove words from the blacklist.",
        "description": "Remove the specified word(s) from the blacklist.",
        "usage": "{tr}فتح_السب <word(s)>",
        "examples": ["{tr}فتح_السب fuck", "{tr}فتح_السب fuck\nsex"],
    },
    groups_only=True,
    require_admin=True,
)
async def unlock_words(event):
    global blacklisted_words
    words = event.pattern_match.group(1).split("\n")
    for word in words:
        word = word.strip()
        if word and word.lower() in blacklisted_words:
            blacklisted_words.remove(word.lower())
    await edit_or_reply(event, "⌔∮ تم فتح الكلمات بنجاح.")

@l313l.ar_bot_cmd(incoming=True)
async def delete_spam(event):
    global blacklisted_words
    message = event.message
    text = message.message.lower()
    for word in blacklisted_words:
        if word in text:
            await message.delete()
            break
