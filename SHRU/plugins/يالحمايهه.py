
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
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..core.managers import edit_delete, edit_or_reply
from telethon.events import NewMessage
from telethon.tl import types
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.utils import get_display_name
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.errors import UserNotParticipantError, PeerIdInvalidError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import Channel , ChatBannedRights
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
    lines = reply.message.split("\p")
    count = len(lines)
    await edit_or_reply(event, f"⌔∮ عدد الأسطر في الرسالة: {count}")
################################################################
# new command 
# new command
# new command
################################################################
# Global variable to store the protection status


plugin_category = "admin"

PROTECTION_ENABLED = False
BAN_THRESHOLD = 5
BAN_TIME_WINDOW = 10 * 60  
banned_users = {}  


@l313l.ar_cmd(
    pattern=r"الحماية تفعيل",
    command=("الحماية تفعيل", plugin_category),
    info={
        "header": "Enable automatic kick for admins who ban multiple members in a short time.",
        "usage": "{tr}الحماية تفعيل",
    },
)
async def enable_protection(event):
    if not await is_admin(event, event.sender_id):
        return await edit_or_reply(
            event,
            "⌔∮ يجب أن تكون مشرفًا في المجموعة لاستخدام هذا الأمر.",
        )
    global PROTECTION_ENABLED
    PROTECTION_ENABLED = True
    await edit_or_reply(event, "⌔∮ تم تفعيل الحماية بنجاح.")


@l313l.ar_cmd(
    pattern=r"الحماية اطفاء",
    command=("الحماية اطفاء", plugin_category),
    info={
        "header": "Disable automatic kick for admins who ban multiple members in a short time.",
        "usage": "{tr}الحماية اطفاء",
    },
)
async def disable_protection(event):
    if not await is_admin(event, event.sender_id):
        return await edit_or_reply(
            event,
            "⌔∮ يجب أن تكون مشرفًا في المجموعة لاستخدام هذا الأمر.",
        )
    global PROTECTION_ENABLED
    PROTECTION_ENABLED = False
    await edit_or_reply(event, "⌔∮ تم إيقاف الحماية بنجاح.")


async def is_admin(event, user_id):
    user = await event.get_chat_member(event.chat_id, user_id)
    return user.status in ["administrator", "creator"]


@l313l.on(events.NewMessage)
async def check_banned_members(event):
    global banned_users
    if not PROTECTION_ENABLED:
        return

    chat_id = event.chat_id
    user_id = event.sender_id
    ban_time = event.date.timestamp()

    if not await is_admin(event, user_id):
        return

    if chat_id not in banned_users:
        banned_users[chat_id] = {}
        banned_users[chat_id][user_id] = ban_time
    else:
        banned_users[chat_id][user_id] = ban_time

        
        now = event.date.timestamp()
        kicked_users = [
            user
            for user, time in banned_users[chat_id].items()
            if now - time <= BAN_TIME_WINDOW
        ]
        if len(kicked_users) >= BAN_THRESHOLD:
            async for user in l313l.iter_participants(chat_id):
                if user.id in kicked_users:
                    try:
                        await l313l.kick_participant(chat_id, user.id)
                        del banned_users[chat_id][user.id]
                    except Exception as e:
                        print(f"حصل خطأ اثناء طرد هذا الدودكي {user.id}: {e}")
                else:
                    banned_users[chat_id][user.id] = now



