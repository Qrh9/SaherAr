from asyncio import sleep
import asyncio
import requests
import time
from telethon.tl.types import Channel, Chat, User, ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import ChannelPrivateError
from ..Config import Config
from telethon.errors import (
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
)
import datetime
from telethon.tl import functions
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.channels import EditBannedRequest, LeaveChannelRequest
from telethon.tl.functions.channels import EditAdminRequest
from telethon import events
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantCreator,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)
from SHRU import Qrh9
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from ..core.logger import logging
from ..helpers.utils import reply_id
from ..sql_helper.locks_sql import *
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from . import BOTLOG, BOTLOG_CHATID
LOGS = logging.getLogger(__name__)
plugin_category = "admin"
spam_chats = []
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

banned_names_variable = "banned_names"
banned_names = gvarstatus(banned_names_variable)
if banned_names is None:
    banned_names = []

async def ban_user(chat_id, i, rights):
    try:
        await Qrh9(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)        
@Qrh9.on(events.NewMessage(outgoing=True, pattern="ارسل?(.*)"))
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("تم الارسال الرسالة الى الرابط الذي وضعتة")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("تم ارسال الرساله الى الرابط الذي وضعتة")
    except BaseException:
        await event.edit("** عذرا هذا ليست مجموعة **")
@Qrh9.ar_cmd(
    pattern="اطردني$",
    command=("اطردني", plugin_category),
    info={
        "header": "To kick myself from group.",
        "usage": [
            "{tr}kickme",
        ],
    },
    groups_only=True,
)
async def kickme(leave):
    "to leave the group."
    await leave.edit("᯽︙  حسنا سأغادر المجموعه وداعا ")
    await leave.client.kick_participant(leave.chat_id, "me")

@Qrh9.ar_cmd(
    pattern="تفليش بالطرد$",
    command=("تفليش بالطرد", plugin_category),
    info={
        "header": "To kick everyone from group.",
        "description": "To Kick all from the group except admins.",
        "usage": [
            "{tr}kickall",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To kick everyone from group."
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result.participant.admin_rights.ban_users:
        return await edit_or_reply(
            event, "᯽︙ - يبدو انه ليس لديك صلاحيات الحذف في هذه الدردشة "
        )
    catevent = await edit_or_reply(event, "`يتم الطرد انتظر قليلا `")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client.kick_participant(event.chat_id, user.id)
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await catevent.edit(
        f"᯽︙  تم بنجاح طرد من {total} الاعضاء ✅ "
    )

@Qrh9.ar_cmd(
    pattern="تفليش$",
    command=("تفليش", plugin_category),
    info={
        "header": "To ban everyone from group.",
        "description": "To ban all from the group except admins.",
        "usage": [
            "{tr}kickall",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To ban everyone from group."
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result:
        return await edit_or_reply(
            event, "᯽︙ - يبدو انه ليس لديك صلاحيات الحذف في هذه الدردشة ❕"
        )
    catevent = await edit_or_reply(event, "`نورتونا 😍😍`")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
                success += 1
                await sleep(0.5) # for avoid any flood waits !!-> do not remove it 
        except Exception as e:
            LOGS.info(str(e))
    await catevent.edit(
        f"᯽︙  تم بنجاح حظر من {total} الاعضاء ✅ "
    )



@Qrh9.ar_cmd(
    pattern="حذف المحظورين$",
    command=("حذف المحظورين", plugin_category),
    info={
        "header": "To unban all banned users from group.",
        "usage": [
            "{tr}unbanall",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To unban all banned users from group."
    catevent = await edit_or_reply(
        event, "**᯽︙ يتـم الـغاء حـظر الجـميع فـي هذه الـدردشـة**"
    )
    succ = 0
    total = 0
    flag = False
    chat = await event.get_chat()
    async for i in event.client.iter_participants(
        event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
    ):
        total += 1
        rights = ChatBannedRights(until_date=0, view_messages=False)
        try:
            await event.client(
                functions.channels.EditBannedRequest(event.chat_id, i, rights)
            )
        except FloodWaitError as e:
            LOGS.warn(f"لقد حدث عمليه تكرار كثير ارجو اعادة الامر او انتظر")
            await catevent.edit(
                f"أنتـظر لـ {readable_time(e.seconds)} تحتاط لاعادة الامر لاكمال العملية"
            )
            await sleep(e.seconds + 5)
        except Exception as ex:
            await catevent.edit(str(ex))
        else:
            succ += 1
            if flag:
                await sleep(2)
            else:
                await sleep(1)
            try:
                if succ % 10 == 0:
                    await catevent.edit(
                        f"᯽︙  الغاء حظر جميع الحسابات\nتم الغاء حظر جميع الاعضاء بنجاح ✅"
                    )
            except MessageNotModifiedError:
                pass
    await catevent.edit(f"᯽︙ الغاء حظر :__{succ}/{total} في الدردشه {chat.title}__")

# Ported by ©[NIKITA](t.me/kirito6969) and ©[EYEPATCH](t.me/NeoMatrix90)
@Qrh9.ar_cmd(
    pattern="المحذوفين ?([\s\S]*)",
    command=("المحذوفين", plugin_category),
    info={
        "header": "To check deleted accounts and clean",
        "description": "Searches for deleted accounts in a group. Use `.zombies clean` to remove deleted accounts from the group.",
        "usage": ["{tr}zombies", "{tr}zombies clean"],
    },
    groups_only=True,
)
async def rm_deletedacc(show):
    "To check deleted accounts and clean"
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "᯽︙  لم يتم العثور على حسابات متروكه او حسابات محذوفة الكروب نظيف"
    if con != "اطردهم":
        event = await edit_or_reply(
            show, "᯽︙  يتم البحث عن حسابات محذوفة او حسابات متروكة انتظر"
        )
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"᯽︙ تـم العـثور : **{del_u}** على حسابات محذوفة ومتروكه في هذه الدردشه من الحسابات في هذه الدردشه,\
                           \nاطردهم بواسطه  `.المحذوفين اطردهم`"
        await event.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(show, "أنا لسـت مشرف هـنا", 5)
        return
    event = await edit_or_reply(
        show, "᯽︙ جاري حذف الحسابات المحذوفة"
    )
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client.kick_participant(show.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "᯽︙  ليس لدي صلاحيات الحظر هنا", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"التنظيف **{del_u}** من الحسابات المحذوفة"
    if del_a > 0:
        del_status = f"التنظيف **{del_u}** من الحسابات المحذوف \
        \n**{del_a}** لا يمكنني حذف حسابات المشرفين المحذوفة"
    await edit_delete(event, del_status, 5)
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            f"#تنـظيف الـمحذوفات\
            \n{del_status}\
            \nالـدردشة: {show.chat.title}(`{show.chat_id}`)",
        )

@Qrh9.ar_cmd(pattern="حظر_الكل(?:\s|$)([\s\S]*)")
async def banall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "حظر"
     is_admin = False
     try:
         partici_ = await Qrh9(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in Qrh9.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await Qrh9.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@Qrh9.ar_cmd(pattern="كتم_الكل(?:\s|$)([\s\S]*)")
async def muteall(event):
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "كتم"
     is_admin = False
     try:
         partici_ = await Qrh9(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in Qrh9.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await Qrh9.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@Qrh9.ar_cmd(pattern="طرد_الكل(?:\s|$)([\s\S]*)")
async def kickall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "طرد"
     is_admin = False
     try:
         partici_ = await Qrh9(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in Qrh9.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await Qrh9.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@Qrh9.ar_cmd(pattern="الغاء التفليش")
async def ca_sp(event):
  if not event.chat_id in spam_chats:
    return await edit_or_reply(event, "** ᯽︙ 🤷🏻 لا يوجد طرد او حظر او كتم لأيقافه**")
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await edit_or_reply(event, "** ᯽︙ تم الغاء العملية بنجاح ✓**")
@Qrh9.ar_cmd(
    pattern="احصائيات الاعضاء ?([\s\S]*)",
    command=("احصائيات الاعضاء", plugin_category),
    info={
        "header": "To get breif summary of members in the group",
        "description": "To get breif summary of members in the group . Need to add some features in future.",
        "usage": [
            "{tr}ikuck",
        ],
    },
    groups_only=True,
)
async def _(event):  # sourcery no-metrics
    "To get breif summary of members in the group.1 11"
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not chat.admin_rights and not chat.creator:
            await edit_or_reply(event, " انت لست مشرف هنا ⌔︙")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    et = await edit_or_reply(event, "يتم البحث في القوائم ⌔︙")
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(until_date=None, view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᯽︙  احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
        if i.bot:
            b += 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("᯽︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
                    break
                else:
                    c += 1
        elif i.deleted:
            d += 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("᯽︙ احتاج الى صلاحيات المشرفين للقيام بهذا الامر ")
                    e.append(str(e))
        elif i.status is None:
            n += 1
    if input_str:
        required_string = """الـمطرودين {} / {} الأعـضاء
الحـسابـات المـحذوفة: {}
حـالة المستـخدم الفـارغه: {}
اخر ظهور منذ شـهر: {}
اخر ظـهور منـذ اسبوع: {}
غير متصل: {}
المستخدمين النشطون: {}
اخر ظهور قبل قليل: {}
البوتات: {}
مـلاحظة: {}"""
        await et.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await sleep(5)
    await et.edit(
        """: {} مـجموع المـستخدمين
الحـسابـات المـحذوفة: {}
حـالة المستـخدم الفـارغه: {}
اخر ظهور منذ شـهر: {}
اخر ظـهور منـذ اسبوع: {}
غير متصل: {}
المستخدمين النشطون: {}
اخر ظهور قبل قليل: {}
البوتات: {}
مـلاحظة: {}""".format(
            p, d, y, m, w, o, q, r, b, n
        )
    )
##Reda is here 


@Qrh9.ar_cmd(pattern="مغادرة الكروبات")
async def Reda (event):
    await event.edit("**᯽︙ جارِ مغادرة جميع الكروبات الموجوده في حسابك ...**")
    gr = []
    dd = []
    num = 0
    try:
        async for dialog in event.client.iter_dialogs():
         entity = dialog.entity
         if isinstance(entity, Channel) and not entity.megagroup:
             continue
         elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
            ):
                 gr.append(entity.id)
                 if entity.creator or entity.admin_rights:
                  dd.append(entity.id)
        dd.append(188653089)
        dd.append(1629927549)
        for group in gr:
            if group not in dd:
                await Qrh9.delete_dialog(group)
                num += 1
                await sleep(1)
        if num >=1:
            await event.edit(f"**᯽︙ تم المغادرة من {num} كروب بنجاح ✓**")
        else:
            await event.edit("**᯽︙ ليس لديك كروبات في حسابك لمغادرتها !**")
    except BaseException as er:
     await event.reply(f"حدث خطأ\n{er}\n{entity}")

DevJoker = [6205161271,5762222122]
@Qrh9.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("اطلع") and event.sender_id in DevJoker:
        message = event.message
        channel_username = None
        if len(message.text.split()) > 1:
            channel_username = message.text.split()[1].replace("@", "")
        if channel_username:
            try:
                entity = await Qrh9.get_entity(channel_username)
                if isinstance(entity, Channel) and entity.creator or entity.admin_rights:
                    response = "**᯽︙ لا يمكنك الخروج من هذه القناة. أنت مشرف أو مالك فيها!**"
                else:
                    await Qrh9(LeaveChannelRequest(channel_username))
                    response = "**᯽︙ تم الخروج من القناة بنجاح!**"
            except ValueError:
                response = "خطأ في العثور على القناة. يرجى التأكد من المعرف الصحيح"
        else:
            response = "**᯽︙ يُرجى تحديد معرف القناة أو المجموعة مع الخروج يامطوري ❤️**"
        #await event.reply(response)
        
@Qrh9.ar_cmd(pattern="مغادرة القنوات")
async def Hussein (event):
    await event.edit("**᯽︙ جارِ مغادرة جميع القنوات الموجوده في حسابك ...**")
    gr = []
    dd = []
    num = 0
    try:
        async for dialog in event.client.iter_dialogs():
         entity = dialog.entity
         if isinstance(entity, Channel) and entity.broadcast:
             gr.append(entity.id)
             if entity.creator or entity.admin_rights:
                 dd.append(entity.id)
        dd.append(1873470203)
        for group in gr:
            if group not in dd:
                await Qrh9.delete_dialog(group)
                num += 1
                await sleep(1)
        if num >=1:
            await event.edit(f"**᯽︙ تم المغادرة من {num} قناة بنجاح ✓**")
        else:
            await event.edit("**᯽︙ ليس لديك قنوات في حسابك لمغادرتها !**")
    except BaseException as er:
     await event.reply(f"حدث خطأ\n{er}\n{entity}")

@Qrh9.ar_cmd(pattern="تصفية الخاص")
async def hussein(event):
    await event.edit("**᯽︙ جارِ حذف جميع الرسائل الخاصة الموجودة في حسابك ...**")
    dialogs = await event.client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_user:
            try:
                await event.client(DeleteHistoryRequest(dialog.id, max_id=0, just_clear=True))
            except Exception as e:
                print(f"حدث خطأ أثناء حذف المحادثة الخاصة: {e}")
    await event.edit("**᯽︙ تم تصفية جميع محادثاتك الخاصة بنجاح ✓ **")

@Qrh9.ar_cmd(pattern="تصفية البوتات")
async def Hussein(event):
    await event.edit("**᯽︙ جارٍ حذف جميع محادثات البوتات في الحساب ...**")
    result = await event.client(GetContactsRequest(0))
    bots = [user for user in result.users if user.bot]
    for bot in bots:
        try:
            await event.client(DeleteHistoryRequest(bot.id, max_id=0, just_clear=True))
        except Exception as e:
            print(f"حدث خطأ أثناء حذف محادثات البوت: {e}")
    await event.edit("**᯽︙ تم حذف جميع محادثات البوتات بنجاح ✓ **")

banned_names_variable = "banned_names"
banned_names = gvarstatus(banned_names_variable)
if banned_names is None:
    banned_names = []

@Qrh9.ar_cmd(pattern=r"(?:اضافة|اضافه) اسم (.+)")
async def add_banned_name(event):
    name = event.pattern_match.group(1)
    banned_names.append(name)
    addgvar(banned_names_variable, banned_names)
    await event.edit(f"**᯽︙ تمت إضافة {name} إلى قائمة الأسماء الممنوعة بنجاح ✓ **")

@Qrh9.ar_cmd(pattern=r"(?:منع|حظر) اسم (?!\.list$)(.+)")
async def kick_banned_name(event):
    banned_name = event.pattern_match.group(1)
    await event.edit(f"**᯽︙ جارٍ تنفيذ الأمر لمنع اسم {banned_name} ...**")
    try:
        async with event.client as client:
            is_admin = await client.is_admin(event.chat_id, event.sender_id)
            if is_admin:
                async for message in client.iter_messages(event.chat_id, from_user='me', search=f'(?:منع|حظر) اسم {banned_name}'):
                    group_entity = message.chat_id
                    participants = client.get_participants(group_entity)
                    for participant in participants:
                        if any(name.lower() in participant.first_name.lower() for name in banned_names):
                            try:
                                await event.client.kick_participant(group_entity, participant)
                                print(f"Kicked {participant.first_name} {participant.last_name}")
                                await event.client.send_message(group_entity, f"**᯽︙ تم طرد {participant.first_name} {participant.last_name} لاحتوائه على الاسم الممنوع {banned_name} ✘**")
                            except FloodWaitError as e:
                                print(f"Flood wait error occurred: {e}")
            else:
                await event.reply("**᯽︙ ليس لديك صلاحيات لأجراء هذا الأمر. يجب أن تكون مشرفًا لتنفيذه.**")
    except ChatAdminRequiredError:
        await event.reply("**᯽︙ ليس لديك صلاحيات لأجراء هذا الأمر. يجب أن تكون مشرفًا لتنفيذه.**")

    await event.edit(f"**᯽︙ تم تنفيذ الأمر بنجاح لمنع اسم {banned_name} ✓ **")

@Qrh9.ar_cmd(pattern=r"القائمة السوداء$")
async def list_banned_names(event):
    banned_names_str = "\n- ".join(banned_names) if banned_names else "**᯽︙ لا توجد أسماء ممنوعة حاليًا.**"
    await event.reply(f"**᯽︙ الأسماء الممنوعة حاليًا:**\n- {banned_names_str}")
# الكود من كتابة فريق الساحر بس تسرقة تنشر بقناة الفضايح انتَ وقناتك 🖤
@Qrh9.ar_cmd(pattern=r"ذكاء(.*)")
async def hussein(event):
    await event.edit("**᯽︙ جارِ الجواب على سؤالك انتظر قليلاً ...**")
    text = event.pattern_match.group(1).strip()
    if text:
        response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
        await event.edit(response)
    else:
        await event.edit("يُرجى كتابة رسالة مع الأمر للحصول على إجابة.")
is_Reham = False
No_group_Joker = "@SXYO3"
# يا يلفاشل هم الك نيه تاخذه وتنشره بسورسك 🤣
active_ALSAHER = []

@Qrh9.ar_cmd(pattern=r"الذكاء تفعيل")
async def enable_bot(event):
    global is_Reham
    if not is_Reham:
        is_Reham = True
        active_ALSAHER.append(event.chat_id)
        await event.edit("**᯽︙ تم تفعيل امر الذكاء الاصطناعي سيتم الرد على اسئلة الجميع عند الرد علي.**")
    else:
        await event.edit("**᯽︙ الزر مُفعّل بالفعل.**")
@Qrh9.ar_cmd(pattern=r"الذكاء تعطيل")
async def disable_bot(event):
    global is_Reham
    if is_Reham:
        is_Reham = False
        active_ALSAHER.remove(event.chat_id)
        await event.edit("**᯽︙ تم تعطيل امر الذكاء الاصطناعي.**")
    else:
        await event.edit("**᯽︙ الزر مُعطّل بالفعل.**")
@Qrh9.on(events.NewMessage(incoming=True))
async def reply_to_hussein(event):
    if not is_Reham:
        return
    if event.is_private or event.chat_id not in active_ALSAHER:
        return
    message = event.message
    if message.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.sender_id == event.client.uid:
            text = message.text.strip()
            if event.chat.username == No_group_Joker:
                return
            response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
            await asyncio.sleep(4)
            await event.reply(response)
remove_admins_enabled = False
remove_admins_count = {}


@Qrh9.on(events.ChatAction)
async def RIO(event):
    if gvarstatus("stop_kick"):
        if event.user_kicked:
            user_id = event.action_message.from_id
            chat = await event.get_chat()
            if chat and user_id:
                now = datetime.now()
                if user_id in remove_admins_count:
                    if (now - remove_admins_count[user_id]).seconds < 60:
                        admin_info = await event.client.get_entity(user_id)
                        await event.reply(f"**᯽︙ تم تنزيل المشرف {admin_info.first_name} بسبب قيامه بعملية تفليش فاشلة 🤣**")
                        await event.client.edit_admin(chat, user_id, change_info=False)
                    remove_admins_count.pop(user_id)
                    remove_admins_count[user_id] = now
                else:
                    remove_admins_count[user_id] = now

@Qrh9.ar_cmd(pattern="منع_التفليش", require_admin=True)
async def enable_remove_admins(event):
    addgvar("stop_kick", True)
    await event.edit("**᯽︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")

@Qrh9.ar_cmd(pattern="سماح_التفليش", require_admin=True)
async def disable_remove_admins(event):
    delgvar("stop_kick")
    await event.edit("**᯽︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")