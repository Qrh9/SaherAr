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

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
@l313l.on(events.NewMessage(chats='@Qrh9X'))
async def handle_new_message(event):
    message = event.message
    sender = await event.get_sender()

    # تحقق مما إذا كان المرسل هو مستخدم عادي وليس بوت أو حساب آخر
    if not sender.bot:
        # الايموجيات التفاعلية التي ترغب في تفعيلها للمستخدمين
        emojis = ["🍓"]

        # إضافة الايموجيات التفاعلية إلى الرسالة
        for emoji in emojis:
            await message.add_reaction(emoji)
