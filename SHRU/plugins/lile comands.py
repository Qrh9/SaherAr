
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

from telethon.tl.types import ChatBannedRights

@l313l.ar_cmd(
    pattern="قفل_السب$",
    command=("قفل_السب", plugin_category),
    info={
        "header": "لقفل وحذف الرسائل التي تحتوي على كلمات سيئة.",
        "usage": "{tr}قفل_السب",
    },
    groups_only=True,
    require_admin=True,
)
async def lock_bad_words(event):
    chat_id = event.chat_id
    banned_rights = ChatBannedRights(
        until_date=None,
        view_messages=True,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        send_polls=True,
        invite_users=True,
        pin_messages=True,
        change_info=True,
    )
    lock_words = ["كسمك", "فرخ", "نيج"]

    async def lock_and_delete_messages(event):
        if any(word.lower() in event.raw_text.lower() for word in lock_words):
            await event.delete()

    event.client.add_event_handler(
        lock_and_delete_messages, events.NewMessage(incoming=True, chats=[chat_id])
    )
    await event.client.edit_permissions(chat_id, event.client.uid, banned_rights)
    await event.edit("تـم قفل السب بنجـاح!")


@l313l.ar_cmd(
    pattern="فتح_السب$",
    command=("فتح_السب", plugin_category),
    info={
        "header": "لفتح السب والسماح بإرسال الرسائل السيئة.",
        "usage": "{tr}فتح_السب",
    },
    groups_only=True,
    require_admin=True,
)
async def unlock_bad_words(event):
    chat_id = event.chat_id
    banned_rights = ChatBannedRights(
        until_date=None,
        view_messages=True,
        send_messages=False,
        send_media=False,
        send_stickers=False,
        send_gifs=False,
        send_games=False,
        send_inline=False,
        send_polls=False,
        invite_users=False,
        pin_messages=False,
        change_info=False,
    )

    async def lock_and_delete_messages(event):
        pass

    event.client.remove_event_handler(
        lock_and_delete_messages, events.NewMessage(incoming=True, chats=[chat_id])
    )
    await event.client.edit_permissions(chat_id, event.client.uid, banned_rights)
    await event.edit("تـم فتح السب بنجاح!")
