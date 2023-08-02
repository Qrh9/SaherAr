
import asyncio
from telethon.tl import types
from telethon import events
from telethon.tl.functions.channels import GetFullChannelRequest, EditBannedRequest
from ..Config import Config
from ..sql_helper.globals import gvarstatus, addgvar, delgvar
from telethon.errors import UserNotParticipantError
from SHRU import l313l
# Function to get the channel entity
async def get_entity(client, entity):
    if entity.startswith("@"):
        entity = entity[1:]
    try:
        return await client.get_entity(entity)
    except ValueError:
        return None

# Check if protection is enabled for a chat
async def is_protection_enabled(chat_id):
    return gvarstatus(f"protection_enabled_{chat_id}") == "yes"

# Enable protection for a chat
async def enable_protection(chat_id):
    if not await is_protection_enabled(chat_id):
        addgvar(f"protection_enabled_{chat_id}", "yes")
        return True
    return False

# Disable protection for a chat
async def disable_protection(chat_id):
    if await is_protection_enabled(chat_id):
        delgvar(f"protection_enabled_{chat_id}")
        return True
    return False

# Event handler for banning users
# Event handler for banning users
@l313l.on(events.UserBanned)
async def ban_users(event):
    chat_id = event.chat_id
    target_id = event.user_id

    # Check if protection is enabled for the chat
    if not await is_protection_enabled(chat_id):
        return

    # Get the chat entity
    chat = await get_entity(event.client, chat_id)

    # Check if the user is an admin
    try:
        admin_info = await event.client(GetFullChannelRequest(chat=chat, user_id=target_id))
        if admin_info.admin_rights:
            return
    except UserNotParticipantError:
        pass

    # Get the chat participants
    chat_participants = await event.client.get_participants(chat_id)
    banned_count = 0

    # Count the number of banned users in the last 3 actions
    for action in reversed(chat_participants):
        if isinstance(action, types.ChannelParticipantBanned):
            banned_count += 1
        if banned_count >= 3:
            break

    # If the number of banned users is 3 or more, ban the admin
    if banned_count >= 3:
        try:
            await event.client(EditBannedRequest(chat_id, target_id, Config.BANNED_RIGHTS))
        except Exception as e:
            print(e)

# Command to enable protection for the chat
@l313l.on(events.NewMessage(outgoing=True, pattern=r"^.الحماية تفعيل$"))
async def enable_protection_command(event):
    chat_id = event.chat_id
    if await enable_protection(chat_id):
        await event.edit("تم تفعيل الحماية بنجاح في هذه المجموعة.")
    else:
        await event.edit("الحماية مفعلة بالفعل في هذه المجموعة.")

# Command to disable protection for the chat
@l313l.on(events.NewMessage(outgoing=True, pattern=r"^.الحماية اطفاء$"))
async def disable_protection_command(event):
    chat_id = event.chat_id
    if await disable_protection(chat_id):
        await event.edit("تم إطفاء الحماية بنجاح في هذه المجموعة.")
    else:
        await event.edit("الحماية مطفية بالفعل في هذه المجموعة.")

