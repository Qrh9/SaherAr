#هسه يجي واحد يكلك الملف كتابتي ثق بالله محد مطور كله خمط من سورسات هندية ويعربون ويصيحون من كتابتي ههه

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from .. import Qrh9
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format, get_user_from_event
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "tools"

LOGS = logging.getLogger(__name__)

@Qrh9.ar_cmd(
    pattern="رسالة(?:\s|$)([\s\S]*)",
    command=("رسالة", plugin_category),

    info={
        "header": "To message to person or to a chat.",
        "description": "Suppose you want to message directly to a person/chat from a paticular chat. Then simply reply to a person with this cmd and text or to a text with cmd and username/userid/chatid,",
        "usage": [
            "{tr}رسالة <username/chatid/chatusername> او بالرد على الرسالة",
            "{tr}رسالة <username/userid/chatid/chatusername> <text>",
        ],
        "examples": "{tr}رسالة @SXYO3 حي الله  ان",
    },
)
async def catbroadcast_add(event):
    "To message to person or to a chat."
    user, reason = await get_user_from_event(event)
    reply = await event.get_reply_message()
    if not user:
        return
    if not reason and not reply:
        return await edit_delete(
            event, "• ماذا تريدني ان ارسل للشخص ؟ اكتب معرف الشخص ومن ثم قم الرسالة الذي تريدها •"
        )
    if reply and reason and user.id != reply.sender_id:
        if BOTLOG:
            msg = await event.client.send_message(BOTLOG_CHATID, reason)
            await event.client.send_message(
                BOTLOG_CHATID,
                "• فشل في ارسال رسالتك الى الشخص ❌ •",
                reply_to=msg.id,
            )
        msglink = await event.clienr.get_msg_link(msg)
        return await edit_or_reply(
            event,
            f"• حدث خطأ في الارسال عد المحاولة •",
        )
    if reason:
        msg = await event.client.send_message(user.id, reason)
    else:
        msg = await event.client.send_message(user.id, reply)
    await edit_delete(event, "• تـم ارسال رسالتك بنجاح ✅ •")

@Qrh9.ar_cmd(pattern="ازالة التوجيه")
async def Reda (event):
    if event.message.reply_to_msg_id:
        
        replied_msg = await event.get_reply_message()
        
        if replied_msg.media:
            
            await Qrh9.send_message(event.chat_id, "", file=replied_msg.media)
        else:
            
            await Qrh9.send_message(chat_id=event.chat_id, message=replied_msg.message)
    else:
        await edit_delete(event, "**قم بالرد على رسالة أولاً **")

