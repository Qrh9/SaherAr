import time
from telethon.tl import types
from telethon import events
from SHRU import l313l
# Global variable to keep track of banned members count and time
banned_count = {}
ban_time = 60  # 60 seconds

# Function to check if an admin should be banned
def should_ban_admin(chat_id, admin_id):
    if admin_id in banned_count:
        current_time = time.time()
        last_ban_time = banned_count[admin_id]
        if current_time - last_ban_time <= ban_time:
            return True
        else:
            banned_count[admin_id] = current_time
    else:
        banned_count[admin_id] = time.time()
    return False

@l313l.on(events.NewMessage(pattern=r"\.الحماية تفعيل", outgoing=True))
async def enable_protection(event):
    global ban_time
    ban_time = 60
    await event.edit("تم تفعيل الحماية ضد المشرفين الذين يحظرون 5 أعضاء خلال 60 ثانية.")

@l313l.on(events.NewMessage(pattern=r"\.الحماية اطفاء", outgoing=True))
async def disable_protection(event):
    global ban_time, banned_count
    ban_time = 0
    banned_count = {}
    await event.edit("تم إطفاء الحماية ضد المشرفين.")

@l313l.on(events.NewMessage(outgoing=True))
async def monitor_banned_members(event):
    if not isinstance(event.chat, types.Chat) or not event.chat.admin_rights:
        return

    if event.chat.admin_rights.ban_users:
        admin_id = event.sender_id
        chat_id = event.chat_id

        if should_ban_admin(chat_id, admin_id):
            await l313l.edit_permissions(chat_id, admin_id, ban_rights=types.ChatBannedRights())
            await event.respond("تم حظر المشرف الذي قام بحظر 5 أعضاء خلال 60 ثانية.")
