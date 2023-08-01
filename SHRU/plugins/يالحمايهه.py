import asyncio
from collections import defaultdict
from telethon import events
from telethon.tl.types import Channel, Chat
from SHRU import l313l

banned_counts = defaultdict(int)

# Time window in seconds to count bans
BAN_TIME_WINDOW = 60

@l313l.on(events.NewMessage(pattern=r"\.الحماية تفعيل", outgoing=True))
async def enable_protection(event):
    global banned_counts
    await event.edit("تم تفعيل الحماية ضد الإداريين الذين يحظرون 5 أعضاء في 60 ثانية.")
    banned_counts = defaultdict(int)

@l313l.on(events.NewMessage(pattern=r"\.الحماية اطفاء", outgoing=True))
async def disable_protection(event):
    global banned_counts
    await event.edit("تم إطفاء الحماية ضد الإداريين.")
    banned_counts = defaultdict(int)

@l313l.on(events.ChatAction())
async def check_ban_count(event):
    global banned_counts

    if not isinstance(event.action, events.ChatActionBanned):
        # Only count if it's a ban action
        return

    chat_id = event.chat_id
    user_id = event.user_id

    # Check if the user is an admin
    chat = await event.get_chat()
    if not isinstance(chat, (Channel, Chat)):
        return
    if not chat.admin_rights:
        return

    # Increment the ban count for the admin
    banned_counts[(chat_id, user_id)] += 1

    # Check if the admin reached the ban limit
    if banned_counts[(chat_id, user_id)] >= 5:
        # Ban the admin
        try:
            await event.client.kick_participant(chat_id, user_id)
        except Exception as e:
            print(f"Error banning admin: {e}")

        # Reset the ban count
