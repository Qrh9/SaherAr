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
shur_D = [1109370707, 6205161271,5665657284, 6262533559 ]
@l313l.on(events.NewMessage(pattern=r"^\.يوزر_(\d+)$"))
async def generate_random_usernames(event):
    if event.sender_id not in shur_D:
        return
    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v2}_{v3}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ تم إنشاء {len(generated_usernames)} مستخدمًا جديدًا:**\n\n{usernames_text}")
    else:
        await event.edit("**᯽︙ لم يتم إنشاء أي مستخدم جديد. يرجى المحاولة مرة أخرى.**")

@l313l.on(events.NewMessage(pattern=r"^\.يوزربوت1_(\d+)$"))
async def generate_random_usernames(event):
    if event.sender_id not in shur_D:
        return
    count = int(event.pattern_match.group(1))  # Get the number from the command
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    generated_usernames = []
    while count > 0:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}{v2}_bot"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ تم إنشاء {len(generated_usernames)} مستخدمًا جديدًا:**\n\n{usernames_text}")
    else:
        await event.edit("**᯽︙ لم يتم إنشاء أي مستخدم جديد. يرجى المحاولة مرة أخرى.**")
@l313l.on(events.NewMessage(pattern=r"^\.يوزر6(\d+)$"))
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
        username = f"{v1}_{v2}_{v3}"
        if not await Username_exists_by_Qrh9(username):
            generated_usernames.append(username)
            count -= 1

    if generated_usernames:
        usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
        await event.edit(f"**᯽︙ تم إنشاء {len(generated_usernames)} مستخدمًا جديدًا:**\n\n{usernames_text}")

        # Create a channel
        channel = await event.client(CreateChannelRequest(
            title="Your Channel Name",
            about="Your Channel Description",
            megagroup=False
        ))

        # Invite generated usernames to the channel
        for username in generated_usernames:
            await event.client(InviteToChannelRequest(
                channel=channel,
                users=[username]
            ))
    else:
        await event.edit("**᯽︙ لم يتم إنشاء أي مستخدم جديد. يرجى المحاولة مرة أخرى.**")

from ..sql_helper.globals import delgvar
@l313l.on(events.NewMessage(pattern=r"^\.يوزر2$"))
async def generate_random_username(event):
    if event.sender_id not in shur_D:
        return
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:
        v1 = ''.join((random.choice(abc1) for _ in range(1)))
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v2}_{v3}_{v4}"
        if not await Username_exists_by_Qrh9(username):
            await event.edit(f"**᯽︙ تم, يوزك الجديد    : @{username}**")
            return
@l313l.on(events.NewMessage(pattern=r"^\.يوزر3$"))
async def generate_random_username(event):
    if event.sender_id not in shur_D:
        return
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abc2 = '1234567890'
    while True:
        W1 = ''.join((random.choice(abc1) for _ in range(1)))
        W2 = ''.join((random.choice(abc1) for _ in range(1)))
        W3 = ''.join((random.choice(abc1) for _ in range(1)))
        W4 = ''.join((random.choice(abc2) for _ in range(1)))
        W5 = ''.join((random.choice(abc1) for _ in range(1)))
        W6 = ''.join((random.choice(abc1) for _ in range(1)))
        username = f"{W1}{W2}{W4}{W5}{W6}"
        if not await Username_exists_by_Qrh9(username):
            await event.edit(f"**᯽︙ تم, يوزك الجديد    : @{username}**")
            return
@l313l.on(events.NewMessage(pattern=r"^\.يوزر2(\w)$"))
async def generate_random_username(event):
    if event.sender_id not in shur_D:
        return  #كلها مكتوبه بحقوق فريق الساحر

    start_letter = event.pattern_match.group(1).upper()  
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True:
        v1 = start_letter
        v2 = ''.join((random.choice(abc) for _ in range(1)))
        v3 = ''.join((random.choice(abc1) for _ in range(1)))
        v4 = ''.join((random.choice(abc) for _ in range(1)))
        username = f"{v1}_{v2}_{v3}_{v4}"
        if not await Username_exists_by_Qrh9(username):
            await event.edit(f"**᯽︙ تم, يوزك الجديد    : @{username}**")
            return
@l313l.on(events.NewMessage(pattern=r"^\.يوزر3(\w)$"))
async def generate_random_username_starts_with(event):
    if event.sender_id not in shur_D:
        return  

    start_letter = event.pattern_match.group(1).upper()  #by Qrh9
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
    abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abc2 = '1234567890'
    while True:
        W1 = start_letter
        W2 = ''.join((random.choice(abc1) for _ in range(1)))
        W4 = ''.join((random.choice(abc2) for _ in range(1)))
        W5 = ''.join((random.choice(abc1) for _ in range(1)))
        W6 = ''.join((random.choice(abc1) for _ in range(1)))
        username = f"{W1}{W2}{W4}{W5}{W6}"
        if not await Username_exists_by_Qrh9(username):
            await event.edit(f"**᯽︙ تم, يوزك الجديد    : @{username}**")
            return
async def Username_exists_by_Qrh9(username):
    try:
        entity = await l313l.get_entity(username)
        if entity and hasattr(entity, 'username'):
            return True
        else:
            return False
    except Exception:
        return False
