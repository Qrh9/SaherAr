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

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ..helpers.functions import edit_or_reply

plugin_category = "admin"

swear_words = ["كلمة1", "كلمة2", "كلمة3"]  # قائمة الكلمات النابية

@l313l.on(events.NewMessage)
async def block_swearing(event):
    if not await is_admin(event, event.client.uid):
        return
    
    chat = await event.get_chat()
    if not chat.admin_rights:
        return
    
    sender = await event.get_sender()
    if sender.bot:
        return
    
    message_text = event.message.message
    if any(word in message_text for word in swear_words):
        try:
            await event.delete()
        except Exception as e:
            pass

async def is_admin(event, user_id):
    chat = await event.get_chat()
    participants = await event.client.get_participants(chat, filter=ChannelParticipantsAdmins)
    for participant in participants:
        if participant.id == user_id:
            return True
    return False
