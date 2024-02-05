
import asyncio
import os
import contextlib
import random
import sys
from datetime import datetime, timedelta
from asyncio.exceptions import CancelledError
import requests
import heroku3
import httpx
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

@Qrh9.on(events.NewMessage(pattern=r"^\.hello$"))
async def say_hello(event):
    chat_id = event.chat_id
    if not await check_cooldown(chat_id):
        await edit_or_reply(event, "**Wait 5 minutes between each command.**")
        return

    await edit_or_reply(event, "Hello, world!")

