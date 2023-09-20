import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl import types

import requests
import heroku3
from telethon.tl.custom import MessageEntityMentionName
import urllib3
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, Qrh9
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
plugin_category = "utils"

allowed_users = [6320583148]
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'منصبين؟':
            if user_id in allowed_users:
                await event.respond(" ;)")
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'منو فخر العرب؟':
            if user_id in allowed_users:
                await event.respond("الامام علي عليه السلام🤍")
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'تحبوني؟':
            if user_id in allowed_users:
                await event.reply("نموت عليك ")
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'شهر الحسين يا ناس':
            if user_id in allowed_users:
                await event.reply("ياا حسين 💔")

@Qrh9.on(events.NewMessage(pattern=r'\.cci', incoming=True))
async def Qrhis9(event):
    user = event.sender
    if isinstance(user, types.UserFull):
        full_name = user.user.first_name + ' ' + user.user.last_name if user.user.last_name else user.user.first_name
    else:
        full_name = user.first_name + ' ' + user.last_name if user.last_name else user.first_name
        usernames = []

        # Check if the user is mentioned by name in the message
        probable_user_mention_entity = event.message.entities
        if isinstance(probable_user_mention_entity, types.MessageEntityMentionName):
            usernames.append(probable_user_mention_entity)

        # فكرة السيد حسين مطور الجوكر
        async for username in Qrh9.iter_usernames(user.user_id):
            if not any(time in username.username for time in ["11:11"]):
                usernames.append(username.username)

        if not usernames:
            message = f'**Full Name**: {full_name}\n**Usernames**: No valid usernames found'
        else:
            message = f'**Full Name**: {full_name}\n**Usernames**: {", ".join(usernames)}'

        await event.reply(message, parse_mode=None)
    else:
        await event.reply('يرجى الرد على المستخدم...')
