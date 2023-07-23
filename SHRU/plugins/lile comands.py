
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
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..core.managers import edit_delete, edit_or_reply
from telethon.events import NewMessage
from telethon import event
from telethon.tl import types

from telethon.utils import get_display_name
plugin_category = "utils"



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
    lines = reply.message.split("\pخ")
    count = len(lines)
    await edit_or_reply(event, f"⌔∮ عدد الأسطر في الرسالة: {count}")
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
import requests
from ..core.managers import edit_or_reply

allowed_senders = [6205161271,6309878173]

headers = {
    'authority': 'api.hexomate.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://discoverprofile.com',
    'referer': 'https://discoverprofile.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}

api_url = 'https://api.hexomate.com/discoverProfile'

# Define the command handler
@l313l.on(events.NewMessage(pattern="^الحسابات (.+)", incoming=True))
async def discover_social_profiles(event):
    sender_id = event.sender_id
    if sender_id not in allowed_senders:
        return  # Exit if the sender is not allowed

    name_to_search = event.pattern_match.group(1)
    json_data = {
        'source': name_to_search,
        'type': 'name',
        'rescan': False,
    }

    try:
        # Send the POST request to the API
        response = requests.post(api_url, headers=headers, json=json_data).json()

        # Process the response and extract the social media profiles
        profiles = response.get('data', {}).get('profiles', [])
        if profiles:
            result = "**تم العثور على الحسابات التالية:**\n"
            for profile in profiles:
                platform = profile.get('platform', '')
                username = profile.get('username', '')
                result += f"**- {platform}:** `{username}`\n"
        else:
            result = "**لم يتم العثور على حسابات متعلقة بهذا الاسم.**"

    except Exception as e:
        result = f"**حدث خطأ أثناء جلب الحسابات: {e}**"

    await edit_or_reply(event, result)
