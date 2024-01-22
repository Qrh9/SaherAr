from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from SHRU import Qrh9

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from . import BOTLOG, BOTLOG_CHATID, extract_time, get_user_from_event

plugin_category = "admin"

# =================== CONSTANT ===================
NO_ADMIN = "**᯽︙  عذرا انا لست مشرف في المجموعة ❕**"
NO_PERM = "**᯽︙ يبـدو انه ليس لديك صلاحيات كافية هذا حزين جدا 🥱♥**"

joker_t8ed = "https://telegra.ph/file/12dc3b4b1b92b9d9c0d68.jpg"
joker_unt8ed = "https://telegra.ph/file/12dc3b4b1b92b9d9c0d68.jpg"
@Qrh9.ar_cmd(
    pattern="تقييد_مؤقت(?:\s|$)([\s\S]*)",
    command=("تقييد_مؤقت", plugin_category),
    info={
        "header": "To stop sending messages permission for that user",
        "description": "Temporary mutes the user for given time.",
        "Time units": {
            "s": "seconds",
            "m": "minutes",
            "h": "Hours",
            "d": "days",
            "w": "weeks",
        },
        "usage": [
            "{tr}tmute <userid/username/reply> <time>",
            "{tr}tmute <userid/username/reply> <time> <reason>",
        ],
        "examples": ["{tr}tmute 2d to test muting for 2 days"],
    },
    groups_only=True,
    require_admin=True,
)
async def tmuter(event):  # sourcery no-metrics
    "لكـتم شخص لمدة معينة"
    await event.delete()
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if not reason:
        return await event.edit("᯽︙ انـت لم تقـم بـوضـع وقـت مع الامـر")
    reason = reason.split(" ", 1)
    hmm = len(reason)
    cattime = reason[0].strip()
    reason = "".join(reason[1:]) if hmm > 1 else None
    ctime = await extract_time(event, cattime)
    if not ctime:
        return
    if user.id == event.client.uid:
        return await event.edit(f"᯽︙ عـذرا لا يمـكننـي حـظر نفـسي ")
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await event.client.send_file(
                event.chat_id,
                joker_t8ed,
                caption=f"᯽︙ تم تقييد المستخدم {_format.mentionuser(user.first_name ,user.id)} بنجاح ✅\n ᯽︙السبب  : {reason}\n ** ᯽︙ مدة الكتم : **`{cattime}`",
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#الكتـم المؤقـت\n"
                    f"**المستخدم : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**الدردشـه : **{event.chat.title}(`{event.chat_id}`)\n"
                    f"**مدة الـكتم : **`{cattime}`\n"
                    f"**السـبب : **`{reason}``",
                )
        else:
            await event.client.send_file(
                event.chat_id,
                joker_t8ed,
                caption=f"**᯽︙ تم تقييد المستخدم {_format.mentionuser(user.first_name ,user.id)} بنجاح ✓** \n** ᯽︙ مدة الكتم : **`{cattime}`",
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#الـكتم المـؤقت\n"
                    f"**المستخدم : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**الدردشه : **{event.chat.title}(`{event.chat_id}`)\n"
                    f"** مـدة الكتـم : **`{cattime}`",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await event.edit("**يبدو ان كتم الشخص تم الغائه**")
    except UserAdminInvalidError:
        return await event.edit(
            "** يبـدو أنك لسـت مشرف في المجموعة او تحاول كتم مشـرف هنا**"
        )
    except Exception as e:
        return await event.edit(f"`{str(e)}`")


@Qrh9.ar_cmd(
    pattern="حظر_مؤقت(?:\s|$)([\s\S]*)",
    command=("حظر_مؤقت", plugin_category),
    info={
        "header": "To remove a user from the group for specified time.",
        "description": "Temporary bans the user for given time.",
        "Time units": {
            "s": "seconds",
            "m": "minutes",
            "h": "Hours",
            "d": "days",
            "w": "weeks",
        },
        "usage": [
            "{tr}tban <userid/username/reply> <time>",
            "{tr}tban <userid/username/reply> <time> <reason>",
        ],
        "examples": ["{tr}tban 2d to test baning for 2 days"],
    },
    groups_only=True,
    require_admin=True,
)
async def tban(event):  # sourcery no-metrics
    "لحـظر شخص مع وقـت معيـن"
    catevent = await edit_or_reply(event, "᯽︙ يتـم  الـحظر مؤقـتا أنتـظر **")
    user, reason = await get_user_from_event(event, catevent)
    if not user:
        return
    if not reason:
        return await catevent.edit("᯽︙ يبدو انك لم تقم بوضع وقت مع الامر **")
    reason = reason.split(" ", 1)
    hmm = len(reason)
    cattime = reason[0].strip()
    reason = "".join(reason[1:]) if hmm > 1 else None
    ctime = await extract_time(catevent, cattime)
    if not ctime:
        return
    if user.id == event.client.uid:
        return await catevent.edit(f"᯽︙ عذرا لا يمكنني كتم نفسـي")
    await catevent.edit("᯽︙ تـم حـظره مـؤقـتا")
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, view_messages=True),
            )
        )
    except UserAdminInvalidError:
        return await catevent.edit(
            "᯽︙ ** يبـدو أنك لسـت مشرف في المجموعة او تحاول كتم مشـرف هنا**"
        )
    except BadRequestError:
        return await catevent.edit(NO_PERM)
    # Helps ban group join spammers more easily
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await catevent.edit(
            "᯽︙ ** لـيس لدي صلاحيـات الحذف لكن سيبقى محظور ❕**"
        )
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await catevent.edit(
            f"**المستخدم {_format.mentionuser(user.first_name ,user.id)}** /n **تـم حظره بنـجاح ✅**\n"
            f"مـدة الحـظر {cattime}\n"
            f"السـبب:`{reason}`"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الـحظر المـؤقت\n"
                f"**المستخدم : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**الدردشـه : **{event.chat.title}(`{event.chat_id}`)\n"
                f"**مـدة الحـظر : **`{cattime}`\n"
                f"**السـبب : **__{reason}__",
            )
    else:
        await catevent.edit(
            f"** الـمستخدم {_format.mentionuser(user.first_name ,user.id)} \n **تـم حظره بنـجاح ✅** \n"
            f"**مـدة الحـظر** {cattime}\n"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الـحظر المـؤقت\n"
                f"**المستخدم : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**المستخدم : **{event.chat.title}(`{event.chat_id}`)\n"
                f"**مـدة الحـظر : **`{cattime}`",
            )

@Qrh9.ar_cmd(
    pattern="تقييد(?:\s|$)([\s\S]*)",
    command=("تقييد", plugin_category),
    info={
        "header": "لتقييد المستخدم في المجموعة بدون مدة زمنية",
        "description": "يقوم بتقييد المستخدم في المجموعة بدون تحديد مدة زمنية.",
        "usage": [
            "{tr}تقييد <userid/username/reply>",
            "{tr}تقييد <userid/username/reply> <reason>",
        ],
        "examples": ["{tr}تقييد @username لأسباب مختلفة"],
    },
    groups_only=True,
    require_admin=True,
)
async def T8ed_Joker(event):
    await event.delete()
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if user.id == event.client.uid:
        return await event.edit("عذرًا، لا يمكنني تقييد نفسي.")
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=None, send_messages=True),
            )
        )
        if reason:
            await event.client.send_file(
                event.chat_id,
                joker_t8ed,
                caption=f"تم تقييد المستخدم {_format.mentionuser(user.first_name ,user.id)} بنجاح ✅.\nالسبب: {reason}",
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#تقييد المستخدم\n"
                    f"**المستخدم: **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**الدردشة: **{event.chat.title}(`{event.chat_id}`)\n"
                    f"**السبب: **`{reason}`",
                )
        else:
            await event.client.send_file(
                event.chat_id,
                joker_t8ed,
                caption=f"᯽︙تم تقييد المستخدم بنجاح ✓ : {_format.mentionuser(user.first_name ,user.id)} ",
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#تقييد المستخدم\n"
                    f"**المستخدم: **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**الدردشة: **{event.chat.title}(`{event.chat_id}`)",
                )
    except UserIdInvalidError:
        return await event.edit("يبدو أن تقييد هذا المستخدم تم إلغاؤه.")
    except UserAdminInvalidError:
        return await event.edit("يبدو أنك لست مشرفًا في المجموعة أو تحاول تقييد مشرف هنا.")
    except Exception as e:
        return await event.edit(f"`{str(e)}`")
@Qrh9.ar_cmd(
    pattern="الغاء تقييد(?:\s|$)([\s\S]*)",
    command=("الغاء تقييد", plugin_category),
    info={
        "header": "لالغاء التقيد المستخدم في المجموعة ",
        "description": "يقوم بالغاء المستخدم في المجموعة.",
        "usage": [
            "{tr}الغاء تقييد <userid/username/reply>",
            "{tr}الغاء تقييد <userid/username/reply> <reason>",
        ],
        "examples": ["{tr}الغاء تقييد @username لأسباب مختلفة"],
    },
    groups_only=True,
    require_admin=True,
)
async def cancel_t8ed(event):
    await event.delete()
    user, _ = await get_user_from_event(event)
    if not user:
        return
    if user.id == event.client.uid:
        return await event.client.send_message(event.chat_id, "عذرًا، لا يمكنك إلغاء تقييد نفسك.")
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=None, send_messages=False),
            )
        )
        await event.client.send_file(
            event.chat_id,
            joker_unt8ed,
            caption=f"**᯽︙ تم الغاء تقييد المستخدم {_format.mentionuser(user.first_name, user.id)} بنجاح ✅.**"
        )
    except UserIdInvalidError:
        return await event.client.send_message(event.chat_id, "يبدو أن التقييد على هذا المستخدم تم إلغاؤه بالفعل.")
    except UserAdminInvalidError:
        return await event.client.send_message(event.chat_id, "يبدو أنك لست مشرفًا في المجموعة أو تحاول إلغاء تقييد مشرف هنا.")
    except Exception as e:
        return await event.client.send_message(event.chat_id, f"`{str(e)}`")