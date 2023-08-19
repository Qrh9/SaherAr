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
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
from telethon.tl.functions.channels import JoinChannelRequest

# List of user IDs who can use these commands
shur_D = [6309878173, 6320583148, 6295913543, 6205161271]

# Store the timestamp of the last command execution
last_execution_time = {}

# Lock to prevent concurrent command execution
command_lock = asyncio.Lock()

# Delay in seconds between sending messages
DELAY_BETWEEN_MESSAGES = 5

async def send_delayed_messages(chat_id, messages):
    for index, message in enumerate(messages, start=1):
        await asyncio.sleep(DELAY_BETWEEN_MESSAGES)
        await l313l.send_message(chat_id, f"{index}- {message}")

@l313l.on(events.NewMessage(pattern=r"^\.(three|forth|botuser|five|sixth)_(\d+)$"))
async def generate_random_usernames(event):
    if event.sender_id not in shur_D:
        return

    command_name = event.pattern_match.group(1)
    count = int(event.pattern_match.group(2))

    async with command_lock:
        if last_execution_time.get(event.sender_id):
            elapsed_time = event.date - last_execution_time[event.sender_id]
            await event.reply(f"You should wait for {elapsed_time.seconds} seconds until the previous command is done.")
            return
        last_execution_time[event.sender_id] = event.date

        generated_usernames = []
        # Generate usernames here

        if generated_usernames:
            await event.edit(f"**᯽︙ Done creating {len(generated_usernames)} users.**")
            await send_delayed_messages(event.chat_id, generated_usernames)
            last_execution_time.pop(event.sender_id)
        else:
            await event.edit("**᯽︙ No users were generated. Please try again.**")
            last_execution_time.pop(event.sender_id)


async def Username_exists_by_Qrh9(username):
    try:
        entity = await l313l.get_entity(username)
        if entity and hasattr(entity, 'username'):
            return True
        else:
            return False
    except Exception:
        return False
@l313l.on(events.NewMessage(pattern=r"^\.three_(\d+)$"))
async def generate_random_usernames(event):
    if event.sender_id not in shur_D:
        return

    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v2}_{v3}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ done creating {len(generated_usernames)} users**\n\n{usernames_text}")
@l313l.on(events.NewMessage(pattern=r"^\.forth_(\d+)$"))
async def generate_random_usernames(event):
    if event.sender_id not in shur_D:
        return

    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}{v2}_{v1}{v3}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ done creating {len(generated_usernames)} users**\n\n{usernames_text}")
@l313l.on(events.NewMessage(pattern=r"^\.botuser_(\d+)$"))
async def generate_random_usernames(event):
    if event.sender_id not in shur_D:
        return
    count = int(event.pattern_match.group(1))  # اذا تخمط انت فرخ😆
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v2}_bot"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ done creating {len(generated_usernames)} users**\n\n{usernames_text}")
    

@l313l.on(events.NewMessage(pattern=r"^\.five_(\d+)$"))
async def generate_random_usernames(event):
    if event.sender_id not in shur_D:
        return

    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v1}_{v1}_{v2}_{v1}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ done creating {len(generated_usernames)} users**\n\n{usernames_text}")
@l313l.on(events.NewMessage(pattern=r"^\.sixth_(\d+)$"))
async def generate_random_usernames(event):
    if event.sender_id not in shur_D:
        return

    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc1) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v1}_{v1}_{v3}_{v1}_{v1}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ done creating {len(generated_usernames)} users**\n\n{usernames_text}")