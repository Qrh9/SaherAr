from asyncio import sleep

from telethon import functions
from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    InputChatPhotoEmpty,
    MessageMediaPhoto,
)

from SHRU import Qrh9

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID

# =================== STRINGS ============
PP_TOO_SMOL = "`The image is too small`"
PP_ERROR = "`Failure while processing the image`"
NO_ADMIN = "`I am not an admin nub nibba!`"
NO_PERM = "`I don't have sufficient permissions! This is so sed. Alexa play despacito`"
CHAT_PP_CHANGED = "`Chat Picture Changed`"
INVALID_MEDIA = "`Invalid Extension`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

LOGS = logging.getLogger(__name__)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

plugin_category = "admin"
#----


@Qrh9.ar_cmd(
    pattern="تثبيت( بالاشعار|$)",
    command=("تثبيت", plugin_category),
    info={
        "᯽︙ الأسـتخدام": "For pining messages in chat",
        "᯽︙ الشـرح": "reply to a message to pin it in that in chat\
        \n᯽︙ تـحتاج الصلاحـيات لـهذا الأمـر if you want to use in group.",
        "options": {"loud": "To notify everyone without this.it will pin silently"},
        "᯽︙ الأمـر": [
            "{tr}pin <reply>",
            "{tr}pin loud <reply>",
        ],
    },
)
async def pin(event):
    "To pin a message in chat"
    to_pin = event.reply_to_msg_id
    if not to_pin:
        return await edit_delete(event, "᯽︙ يـجب الـرد على الـرسالة التي تـريد تـثبيـتها ", 5)
    options = event.pattern_match.group(1)
    is_silent = bool(options)
    try:
        await event.client.pin_message(event.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"`{str(e)}`", 5)
    await edit_delete(event, "᯽︙ تـم تـثبيـت الـرسالة بـنجـاح ✅", 3)
    if BOTLOG and not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"᯽︙ الـتثبيت\
                \n **᯽︙ تـم بـنجـاح الـتثبيت فـي الدردشـة**\
                \nالـدردشـة: {event.chat.title}(`{event.chat_id}`)\
                \nالـتثبيت: {is_silent}",
        )
#admin plugin for  Qrh9
@Qrh9.ar_cmd(
    pattern="الغاء التثبيت( للكل|$)",
    command=("الغاء التثبيت", plugin_category),
    info={
        "header": "For unpining messages in chat",
        "description": "reply to a message to unpin it in that in chat\
        \nNote : You need proper rights for this if you want to use in group.",
        "options": {"all": "To unpin all messages in the chat"},
        "usage": [
            "{tr}unpin <reply>",
            "{tr}unpin all",
        ],
    },
)
async def pin(event):
    "᯽︙ لإلغاء تثبيت رسائل من المجموعة  ⚠️"
    to_unpin = event.reply_to_msg_id
    options = (event.pattern_match.group(1)).strip()
    if not to_unpin and options != "all":
        return await edit_delete(
            event,
            "᯽︙ يرجى الرد على الرسالة التي تريد تثبيتها استخدم `.الغاء التثبيت للكل`  لالغاء تثبيت جميع الرسائل  📍",
            5,
        )
    try:
        if to_unpin and not options:
            await event.client.unpin_message(event.chat_id, to_unpin)
        elif options == "للكل":
            await event.client.unpin_message(event.chat_id)
        else:
            return await edit_delete(
                event, "᯽︙ يرجى الرد على الرسالة التي تريد تثبيتها استخدم `.الغاء التثبيت للكل`  لالغاء تثبيت جميع الرسائل  📍", 5
            )
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"`{str(e)}`", 5)
    await edit_delete(event, "**⌔ ︙تم الغاء التثبيت بنجاح  ✅**", 3)
    if BOTLOG and not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"**᯽︙ الـغاء التثبيت  ❗️ \
                \n** ᯽︙ تم بنجاح الغاء التثبيـت في الدردشة  ✅ \
                \n⌔︙الدردشـه  🔖 : {event.chat.title}(`{event.chat_id}`)",
        )
#admin plugin for  Qrh9
@Qrh9.ar_cmd(
    pattern="الاحداث( -ر)?(?: |$)(\d*)?",
    command=("الأحداث", plugin_category),
    info={
        "᯽︙ الأسـتخدام": "To get recent deleted messages in group",
        "᯽︙ الشـرح": "To check recent deleted messages in group, by default will show 5. you can get 1 to 15 messages.",
        "flags": {
            "u": "use this flag to upload media to chat else will just show as media."
        },
        "᯽︙ الأمـر": [
            "{tr}undlt <count>",
            "{tr}undlt -u <count>",
        ],
        "examples": [
            "{tr}الأحداث 7",
            "{tr}الأحداث -ر 7 (this will reply all 7 messages to this message",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _iundlt(event):  # sourcery no-metrics
    "To check recent deleted messages in group"
    catevent = await edit_or_reply(event, "᯽︙ يـتم الـبحث عن اخـر الاحداث")
    flag = event.pattern_match.group(1)
    if event.pattern_match.group(2) != "":
        lim = int(event.pattern_match.group(2))
        if lim > 15:
            lim = int(15)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(5)
    adminlog = await event.client.get_admin_log(
        event.chat_id, limit=lim, edit=False, delete=True
    )
    deleted_msg = f"᯽︙ اخـر {lim} رسـائل مـحذوفة فـي الـدردشة :"
    if not flag:
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).users[0]
            _media_type = media_type(msg.old)
            if _media_type is None:
                deleted_msg += f"\n {msg.old.message} \n ᯽︙ تم ارسالها بـواسطة {_format.mentionuser(ruser.first_name ,ruser.id)}"
            else:
                deleted_msg += f"\n {_media_type} \n ᯽︙ ارسلت بـواسطـة {_format.mentionuser(ruser.first_name ,ruser.id)}"
        await edit_or_reply(catevent, deleted_msg)
    else:
        main_msg = await edit_or_reply(catevent, deleted_msg)
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).users[0]
            _media_type = media_type(msg.old)
            if _media_type is None:
                await main_msg.reply(
                    f"{msg.old.message}\n᯽︙ ارسلت بواسطه {_format.mentionuser(ruser.first_name ,ruser.id)}"
                )
            else:
                await main_msg.reply(
                    f"{msg.old.message}\n᯽︙ ارسلت بواسطه {_format.mentionuser(ruser.first_name ,ruser.id)}",
                    file=msg.old.media,
                )
#admin plugin for  Qrh9
# by  @SX9OO
