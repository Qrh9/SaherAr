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

 allowed_users = [5835316914]
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
                await event.reply("نموت عليك سيد")
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    if user_id in allowed_users:
        message_text = event.message.text.strip()
        if message_text == 'شهر الحسين يا ناس':
            if user_id in allowed_users:
                await event.reply("ياا حسين 💔")
@Qrh9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    message_text = event.message.text.strip()
    if user_id in allowed_users and message_text == 'يلا':
        # Replace 'specific_id' with the ID you want to respond to.
        specific_id =6051188407
        
        # Check if the message is from the specific user you want to respond to.
        if user_id == specific_id:
            await event.respond("كل عام وانت بخير سيد 🖤")