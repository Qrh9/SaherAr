import asyncio
from telethon.tl import types
from telethon import events
from telethon.tl.functions.channels import GetFullChannelRequest, EditBannedRequest
from ..Config import Config
from ..sql_helper.globals import gvarstatus, addgvar, delgvar
from telethon.errors import UserNotParticipantError
from SHRU import Qrh9
from telethon.tl.types import (ChannelParticipantsAdmins,
                                 ChatAdminRights,
                                   ChatBannedRights,
                                     MessageEntityMentionName,
                                       MessageMediaPhoto)
@Qrh9.on(events.NewMessage())
async def handle_user_banned(event):
    if isinstance(event.action, types.MessageActionChatDeleteUser):
        chat_id = event.chat_id
        target_id = event.action.user_id

        # Check if protection is enabled for the chat
        if not await is_protection_enabled(chat_id):
            return

        # Get the chat entity
        chat = await get_entity(event.client, chat_id)

        # Check if the user is an admin or an exception
        try:
            admin_info = await event.client(GetFullChannelRequest(chat=chat, user_id=target_id))
            if admin_info.admin_rights or target_id in exceptions:
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

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

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
        return None
    return False

# Disable protection for a chat
async def disable_protection(chat_id):
    if await is_protection_enabled(chat_id):
        delgvar(f"protection_enabled_{chat_id}")
        return None
    return False

exceptions = []

# Command to enable protection for the chat
@Qrh9.on(events.NewMessage(outgoing=None, pattern=r"^.الحماية تفعيل$"))
async def enable_protection_command(event):
    chat_id = event.chat_id
    if await enable_protection(chat_id):
        await event.edit("تم تفعيل الحماية بنجاح في هذه المجموعة.")
    else:
        await event.edit("الحماية مفعلة بالفعل في هذه المجموعة.")

# Command to disable protection for the chat
@Qrh9.on(events.NewMessage(outgoing=None, pattern=r"^.الحماية اطفاء$"))
async def disable_protection_command(event):
    chat_id = event.chat_id
    if await disable_protection(chat_id):
        await event.edit("تم إطفاء الحماية بنجاح في هذه المجموعة.")
    else:
        await event.edit("الحماية مطفية بالفعل في هذه المجموعة.")

# Command to add an exception
@Qrh9.on(events.NewMessage(outgoing=None, pattern=r"^.استثناء$"))
async def add_exception(event):
    reply_msg = await event.get_reply_message()
    if reply_msg and reply_msg.sender:
        user_id = reply_msg.sender.id
        if user_id not in exceptions:
            exceptions.append(user_id)
            await event.edit("تم إضافة الشخص إلى قائمة الاستثناء.")
        else:
            await event.edit("الشخص موجود بالفعل في قائمة الاستثناء.")

# Command to remove an exception
@Qrh9.on(events.NewMessage(outgoing=None, pattern=r"^.ازالة_استثناء$"))
async def remove_exception(event):
    reply_msg = await event.get_reply_message()
    if reply_msg and reply_msg.sender:
        user_id = reply_msg.sender.id
        if user_id in exceptions:
            exceptions.remove(user_id)
            await event.edit("تم إزالة الشخص من قائمة الاستثناء.")
        else:
            await event.edit("الشخص غير موجود في قائمة الاستثناء.")

