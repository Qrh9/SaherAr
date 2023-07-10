
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


@l313l.ar_cmd(
    pattern="اغلاق السب$",
    command=("اغلاق السب", plugin_category),
    info={
        "header": "to lock and delete messages containing bad words.",
        "usage": "{tr}اغلاق السب",
    },
    groups_only=True,
    require_admin=True,
)
async def lock_and_delete_msgs(event):
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
        send_other_messages=False, 
    )
    lock_words = ["كسمك", "فرخ", "نيج"]  

    async def lock_and_delete_messages(event):
        if any(word.lower() in event.raw_text.lower() for word in lock_words):
            await event.delete()

    await event.client(
        NewMessage(
            incoming=True,
            func=lock_and_delete_messages,
            chats=[chat_id]
        )
    )
    await event.client.edit_permissions(chat_id, event.client.uid, banned_rights)
    await event.edit("تـم اغلاق السب بنجـاح!")


