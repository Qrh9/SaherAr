import asyncio
import os
import contextlib
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
progs = [6205161271]

@l313l.on(events.NewMessage(incoming=True))
async def reda(event):
    if event.sender_id in progs:
        message_text = event.message.text.strip()

        if message_text == 'منصب؟':
            await event.reply('✔يب منصب')