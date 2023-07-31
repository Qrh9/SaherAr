
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
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..core.managers import edit_delete, edit_or_reply
from telethon.events import NewMessage
from telethon.tl import types
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.utils import get_display_name
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.errors import UserNotParticipantError, PeerIdInvalidError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import Channel , ChatBannedRights
plugin_category = "utils"

from telethon.tl.functions.channels import GetParticipant
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

class HuReClient(l313l, events.EventsClient):
    async def is_group_owner(self, chat_id, user_id):
        try:
            participant = await self(GetParticipant(chat_id, user_id))
            return (
                isinstance(participant.participant, ChannelParticipantAdmin)
                and participant.participant.rank == "creator"
            )
        except ValueError:
            return False
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
    lines = reply.message.split("\p")
    count = len(lines)
    await edit_or_reply(event, f"⌔∮ عدد الأسطر في الرسالة: {count}")
################################################################
# new command 
# new command
# new command
################################################################
# Global variable to store the protection status
protection_enabled = False

@l313l.ar_cmd(
    pattern="الحماية تفعيل|الحمايه تفعيل",
    command=("الحماية تفعيل", plugin_category),
    info={
        "header": "Enable the protection feature.",
    },
)
async def enable_protection(event):
    global protection_enabled
    if not await l313l.is_group_owner(event.chat_id, event.sender_id):
        return await event.edit("⌔∮ يجب أن تكون مالك المجموعة لاستعمال هذا الأمر.")
    
    protection_enabled = True
    await event.edit("⌔∮ تم تفعيل الحماية.")

@l313l.ar_cmd(
    pattern="الحماية اطفاء|الحمايه اطفاء",
    command=("الحماية اطفاء", plugin_category),
    info={
        "header": "Disable the protection feature.",
    },
)
async def disable_protection(event):
    global protection_enabled
    if not await l313l.is_group_owner(event.chat_id, event.sender_id):
        return await event.edit("⌔∮ يجب أن تكون مالك المجموعة لاستعمال هذا الأمر.")
    
    protection_enabled = False
    await event.edit("⌔∮ تم إطفاء الحماية.")


@l313l.on(events.ChatAction)
async def check_banned(event):
    global protection_enabled
    if protection_enabled and event.user_added:
        chat = await event.get_chat()
        if await l313l.is_group_admin(chat.id, event.user_id):
            # Get the list of banned members in the last 10 seconds
            async for banned_event in l313l.iter_admin_log(
                chat.id, min_id=event.id, max_id=event.id, join=True
            ):
                if (
                    banned_event.action.__class__.__name__ == "ChatBannedRights"
                    and banned_event.action.banned_rights.view_messages
                ):
                    async for admin_event in l313l.iter_admin_log(
                        chat.id,
                        min_id=event.id - 10,
                        max_id=event.id,
                        by_members=True,
                    ):
                        if (
                            admin_event.user_id == event.user_id
                            and admin_event.action.user_id == event.user_id
                        ):
                            async for _ in l313l.iter_admin_log(
                                chat.id,
                                min_id=admin_event.id,
                                max_id=banned_event.id,
                                by_members=True,
                            ):
                                if (
                                    _.user_id == event.user_id
                                    and _.action.user_id == event.user_id
                                ):
                                    # Ban the admin who banned 5 members in 10 seconds
                                    await l313l(EditBannedRequest(chat.id, event.user_id, ChatBannedRights(until_date=None, view_messages=True)))
                                    await l313l.send_message(
                                        chat.id, f"⌔∮ تم طرد المشرف {event.user.first_name} لانه قام بحظر 5 أعضاء في 10 ثواني."
                                    )
                                    break
                            break
                    break


async def is_group_owner(chat_id, user_id):
    chat = await l313l.get_entity(chat_id)
    return isinstance(chat, Channel) and chat.creator == user_id

# Function to check if the user is a group admin
async def is_group_admin(chat_id, user_id):
    try:
        participant = await l313l(
            GetParticipantRequest(
                channel=await l313l.get_input_entity(chat_id), user_id=user_id
            )
        )
        return isinstance(participant.participant, ChannelParticipantAdmin)
    except (UserNotParticipantError, PeerIdInvalidError):
        return False


async def iter_admin_log(chat_id, **kwargs):
    return await l313l.iter_admin_log(chat_id, **kwargs)


