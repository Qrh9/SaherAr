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
async def auto_react(channel_username, reaction_emoji):
    channel = await l313l.get_entity(channel_username)
    async for message in l313l.iter_messages(channel):
        await l313l.send_reaction(message, reaction_emoji)

@l313l.on(events.ChatAction)
async def auto_reaction(event):
    if isinstance(event.action, events.ChatAction.UserJoined):
        reaction_emoji = "❤🔥"  # Change to the desired reaction emoji
        await auto_react("@Qrh9x", reaction_emoji)