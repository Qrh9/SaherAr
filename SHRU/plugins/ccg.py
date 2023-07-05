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
allowed_users = [1497929447, 5755529173, 6205161271]

@l313l.on(events.NewMessage(pattern=r"ccg"))
async def send_id_command(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        await event.respond("ايدي")
