import re
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ..core.logger import logging
from ..helpers.functions import edit_or_reply 
from SHRU import l313l
blacklist = ["عير", "word2", "word3"]  # List of words to be blacklisted
LOGS = logging.getLogger(__name__)
plugin_category = "admin"
@l313l.ar_cmd(
    pattern="قفل_كلمات$",
    command=("قفل_كلمات", plugin_category),
    info={
        "header": "Track and delete messages containing blacklisted words.",
        "usage": "{tr}قفل_كلمات",
    },
)
async def track_delete_messages(event):
    chat = await event.get_chat()
    if not chat.admin_rights:
        return await edit_or_reply(event, "⌔∮ أنا لست مشرفًا في هذه المجموعة.")
    if not chat.admin_rights.delete_messages:
        return await edit_or_reply(event, "⌔∮ ليس لدي صلاحيات حذف الرسائل في هذه المجموعة.")
    reply = await event.get_reply_message()
    if not reply or not reply.message:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على الرسالة للبدء في تتبع الكلمات.")
    await edit_or_reply(event, "⌔∮ تم تنشيط تتبع الكلمات. سيتم حذف الرسائل التي تحتوي على الكلمات المحظورة.")

@l313l.ar_bot(
    pattern=".*",
    from_users=ChannelParticipantsAdmins,
    func=lambda e: e.is_group
)
async def delete_blacklisted_messages(event):
    if not event.message or not event.message.message:
        return
    message_text = event.message.message
    for word in blacklist:
        if re.search(rf"\b{re.escape(word)}\b", message_text, re.I):
            try:
                await event.client.delete_messages(event.chat_id, event.message.id)
            except Exception as e:
                LOGS.error(f"Error deleting message: {e}")
