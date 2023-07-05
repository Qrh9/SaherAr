import asyncio
from telethon import events, utils
from telethon.tl.types import InputMediaDice
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
channel_username = '@Qrh9x'
emoji = '❤️🔥'  # Heart on fire emoji

@l313l.on(events.NewMessage(chats=channel_username))
async def react_to_channel_messages(event):
    # React to the message with the heart on fire emoji
    await event.reply(emoji, parse_mode='emoji')
