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
from telethon.tl.types import ChannelParticipantsAdmins

from telethon.tl import types

from telethon.utils import get_display_name
plugin_category = "admin"
async def is_admin(event, user_id):
    
    chat = await event.get_chat()
    participants = await event.client.get_participants(chat, filter=ChannelParticipantsAdmins)
    for participant in participants:
        if participant.id == user_id:
            return True
    return False
swear_words = ["كلمة1", "كلمة2", "كلمة3"]  # قائمة الكلمات النابية

@l313l.ar_cmd(
    pattern="قفل_السب$",
    command=("قفل_السب", plugin_category),
    info={
        "header": "قفل الكلمات النابية وحذف الرسائل التي تحتوي على هذه الكلمات.",
        "usage": "{tr}قفل_السب",
    },
)
async def block_swearing(event):
    if not await is_admin(event, event.client.uid):
        return await edit_or_reply(
            event, "⌔∮ أنا لست مشرفا هنا؟!"
        )
    
    chat = await event.get_chat()
    async for admin in event.client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if admin.id == event.client.uid:
            continue
        try:
            await event.client.edit_permissions(chat, admin, send_messages=False)
        except Exception as e:
            return await edit_or_reply(
                event, f"⌔∮ لا يمكن قفل السب بسبب الخطأ التالي: {e}"
            )
    
    await edit_or_reply(event, "⌔∮ تم قفل الكلمات النابية وحذف الرسائل المحتوية عليها.")