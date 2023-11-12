#بربك تخمط هيج كود يا فاشل💀
import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import urllib3
import re 
from telethon import events 
from telethon.tl import types
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, Qrh9
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
from ..Config import Config
import json
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
from telethon.tl.functions.channels import JoinChannelRequest

from telethon import events

@Qrh9.ar_cmd(pattern=r"رفع ستوري $")
async def upload_story(event):
    if not event.reply_to_message:
        await event.edit("رد على صورة أو فيديو لرفعه كقصة")
        return

    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("الرسالة التي رديت عليها لا تحتوي على وسائط")
        return

    media = reply_message.media
    file_id = media.document.file_id
    if media.document.mime_type == "image/jpeg":
        file_type = "photo"
    elif media.document.mime_type == "video/mp4":
        file_type = "video"
    else:
        await event.edit("الوسائط التي رديت عليها غير مدعومة")
        return

    title = event.text[8:] if len(event.text) > 8 else None
    expires_in = event.text[17:] if len(event.text) > 17 else None

    if reply_message.caption:
        title = f"{title} - {reply_message.caption}"

    await edit_or_reply(event, "تم رفع القصة بنجاح")
    await Qrh9.send_file(
        event.chat_id,
        file_id,
        caption=title,
        expires_in=expires_in,
        force_document=False,
        file_type=file_type,
    )
