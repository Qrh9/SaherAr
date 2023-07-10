import re
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ..core.logger import logging
from ..helpers.functions import edit_or_reply
from SHRU   import l313l
blacklist = ["عير", "كلمة2", "كلمة3"]  # List of words to be blacklisted
LOGS = logging.getLogger(__name__)
plugin_category = "utils"
blacklist_enabled = False
tracked_messages = []

@l313l.ar_cmd(
    pattern="حضر_السب$",
    command=("حضر_السب", plugin_category),
    info={
        "header": "Track and delete messages containing blacklisted words.",
        "usage": "{tr}حضر_السب",
    },
)
async def enable_blacklist_tracking(event):
    global blacklist_enabled
    blacklist_enabled = True
    await edit_or_reply(event, "⌔∮ تم تنشيط تتبع الكلمات السيئة. سيتم حذف الرسائل التي تحتوي على الكلمات المحظورة.")

@l313l.ar_bot(
    pattern=".*",
    from_users=ChannelParticipantsAdmins,
    func=lambda e: e.is_group
)
async def delete_blacklisted_messages(event):
    global blacklist_enabled
    if blacklist_enabled:
        if not event.message or not event.message.message:
            return
        message_text = event.message.message
        for word in blacklist:
            if re.search(rf"\b{re.escape(word)}\b", message_text, re.I):
                try:
                    await event.client.delete_messages(event.chat_id, event.message.id)
                    tracked_messages.append(event.message.id)
                except Exception as e:
                    LOGS.error(f"Error deleting message: {e}")

@l313l.ar_cmd(
    pattern="قفل_السب$",
    command=("قفل_السب", plugin_category),
    info={
        "header": "Stop tracking and deleting messages containing blacklisted words.",
        "usage": "{tr}قفل_السب",
    },
)
async def disable_blacklist_tracking(event):
    global blacklist_enabled, tracked_messages
    blacklist_enabled = False
    for message_id in tracked_messages:
        try:
            await event.client.delete_messages(event.chat_id, message_id)
        except Exception as e:
            LOGS.error(f"Error deleting message: {e}")
    tracked_messages = []
    await edit_or_reply(event, "⌔∮ تم إيقاف تتبع الكلمات السيئة وحذف الرسائل.")

@l313l.ar_cmd(
    pattern="قائمة_السب$",
    command=("قائمة_السب", plugin_category),
    info={
        "header": "View the current blacklist of words.",
        "usage": "{tr}قائمة_السب",
    },
)
async def view_blacklist(event):
    blacklist_text = "\n".join(blacklist)
    await edit_or_reply(event, f"⌔∮ قائمة الكلمات السيئة:\n\n{blacklist_text}")
