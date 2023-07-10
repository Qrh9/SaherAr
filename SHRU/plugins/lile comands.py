
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
from telethon.tl.types import ChatBannedRights
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

@l313l.ar_cmd(
    pattern="قفل_السب$",
    command=("قفل_السب", plugin_category),
    info={
        "header": "قفل الرسائل التي تحتوي على كلمات غير مرغوب فيها.",
        "usage": "{tr}قفل_السب",
    },
    groups_only=True,
    require_admin=True,
)
async def lock_bad_words(event):
    lock_words = ["كسمك", "فرخ", "نيج"]
    await event.edit("تم قفل السب")

    @events.register(events.NewMessage(incoming=True, chats=event.chat_id))
    async def lock_and_delete_messages(event):
        if event.sender_id == event.client.uid or not event.is_group:
            return

        if any(word.lower() in event.raw_text.lower() for word in lock_words):
            await event.delete()

    await event.client.add_event_handler(lock_and_delete_messages)


@l313l.ar_cmd(
    pattern="فتح_السب$",
    command=("فتح_السب", plugin_category),
    info={
        "header": "إلغاء قفل الرسائل التي تحتوي على كلمات غير مرغوب فيها.",
        "usage": "{tr}فتح السب",
    },
    groups_only=True,
    require_admin=True,
)
async def unlock_bad_words(event):
    await event.edit("تم إلغاء قفل_السب.")
    await event.client.remove_event_handler(lock_and_delete_messages)


async def lock_and_delete_messages(event):
    if event.is_group and event.text.startswith(".قفل_السب"):
        lock_words = ["كسمك", "فرخ", "نيج"]
        sender_id = event.sender_id

        if not await event.client.is_chat_admin(event.chat_id, sender_id):
            await event.reply("ليس لديك صلاحية حذف الرسائل.")
            return

        async for message in event.client.iter_messages(event.chat_id):
            if message.sender_id != event.client.uid and any(word.lower() in message.raw_text.lower() for word in lock_words):
                await message.delete()
