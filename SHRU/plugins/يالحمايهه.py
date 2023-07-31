
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

from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.utils import get_display_name
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.errors import UserNotParticipantError, PeerIdInvalidError

from telethon.tl.types import Channel , ChatBannedRights
plugin_category = "admin"
from SHRU import l313l

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper.locks_sql import get_locks, is_locked, update_lock
from ..utils import is_admin
from . import BOTLOG, get_user_from_event

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
