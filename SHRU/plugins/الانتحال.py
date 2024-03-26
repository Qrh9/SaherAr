# Copyright (C) 2021 SHRU TEAM
# FILES WRITTEN BY  @SX9OO
import html
import base64
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl import functions, types
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import ChatAdminRequiredError, FloodWaitError
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..Config import Config
from . import (
    ALIVE_NAME,
    AUTONAME,
    BOTLOG,
    BOTLOG_CHATID,
    DEFAULT_BIO,
    Qrh9,
    edit_delete,
    get_user_from_event,
)

plugin_category = "utils"
DEFAULTUSER = str(AUTONAME) if AUTONAME else str(ALIVE_NAME)
DEFAULTUSERBIO = (
    str(DEFAULT_BIO)
    if DEFAULT_BIO
    else "كنَّا نموت إذا افترقنا ساعةً ‏واليوم نُحصي الهجر بالأعوام @Qrh9X"
)

@Qrh9.ar_cmd(pattern="انتحال(?:\s|$)([\s\S]*)")
async def _(event):
    mid = await Qrh9.get_me()
    me = (await event.client(GetFullUserRequest(mid.id))).full_user
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return await edit_delete(event, "**يجب الرد على رسالة اولاً**")
    if replied_user.id == 1045489068:
        return await edit_delete(event, "**لا تحاول تنتحل المطورين ادبسز!**")
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    user_bio = replied_user.about
    if user_bio is None:
        user_bio = ""
    fname = mid.first_name
    if fname == None:
        fname = ""
    lname = mid.last_name
    if lname == None:
        lname = ""
    oabout = me.about
    if oabout == None:
        oabout = ""
    addgvar("fname", fname)
    addgvar("lname", lname)
    addgvar("oabout", oabout)
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        pfile = await event.client.upload_file(profile_pic)
    except Exception as e:
        delgvar("fname")
        delgvar("lname")
        delgvar("oabout")
        return await edit_delete(event, f"**فشل في الانتحال بسبب:**\n__{e}__")
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "**⌁︙تـم نسـخ الـحساب بـنجاح ،✅**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الانتحال\nتم انتحال المستخدم: [{first_name}](tg://user?id={user_id })",
        )
        
@Qrh9.ar_cmd(
    pattern="اعادة$",
    command=("اعادة", plugin_category),
    info={
        "header": "To revert back to your original name , bio and profile pic",
        "note": "For proper Functioning of this command you need to set AUTONAME and DEFAULT_BIO with your profile name and bio respectively.",
        "usage": "{tr}revert",
    },
)
async def _(event):
    "To reset your original details"
    name = gvarstatus("fname")
    blank = gvarstatus("lname")
    bio = gvarstatus("oabout")
    await event.client(
        functions.photos.DeletePhotosRequest(
            await event.client.get_profile_photos("me", limit=1)
        )
    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=name))
    await event.client(functions.account.UpdateProfileRequest(last_name=blank))
    await edit_delete(event, "⌁︙تـم اعـادة الـحساب بـنجاح ،✅")
    delgvar("fname")
    delgvar("lname")
    delgvar("oabout")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"⌁︙تـم اعادة الـحساب الى وضـعه الاصلـي ،✅")

jeps = ["SHRU", "Qruesupport"]
@Qrh9.ar_cmd(pattern="انتحال_الدردشه")
async def reda(event):
    if event.is_group or event.is_channel:
        chat_id = -1
        msg = event.message.message
        msg = msg.replace(".انتحال_الدردشه", "")
        msg = msg.replace(" ", "")
        if msg == "":
            return await edit_delete(event, "**قم بوضع يوزر الگروب او القناة بدون علامة @ للانتحال**")
        chat_id = msg
        try:
            result = await Qrh9(GetFullChannelRequest(
                chat_id
            ))
        except ValueError:
            return await edit_delete(event, "**᯽︙ لا يوجد هكذا كروب او قناة تاكد من اليوزر او الايدي ويجب ان يكون/تكون عام/عامة وليس خاص/خاصة**")
        mych = await Qrh9(GetFullChannelRequest(
                event.chat_id
            ))
        if msg in jeps:
            return await edit_delete(event, "**᯽︙ لا يمكنك انتحال قناة او كروب السورس !**")
        addgvar(f"{event.chat_id}name", mych.chats[0].title)
        addgvar(f"{event.chat_id}about", mych.full_chat.about)
        try:
            await Qrh9(functions.channels.EditTitleRequest(
                channel=await Qrh9.get_entity(event.chat_id),
                title=result.chats[0].title
            ))
        except ChatAdminRequiredError:
            delgvar (f"{event.chat_id}name")
            delgvar (f"{event.chat_id}about")
            return await edit_delete(event, "**᯽︙ يجب ان تكون لديك صلاحيات لتغيير الاسم والصورة والبايو لانتحال قناة او كروب**")
        except FloodWaitError:
            return await edit_delete(event, "**انتضر مدة لا تقل عن 5 دقائق للانتحال مجدداً FLOODWAITERROR خطأ من التيليجرام**")
        try:
            await Qrh9(functions.messages.EditChatAboutRequest(
            peer=event.chat_id,
            about=result.full_chat.about
        ))
        except FloodWaitError:
            return await edit_delete(event, "**انتضر مدة لا تقل عن 5 دقائق للانتحال مجدداً FLOODWAITERROR خطأ من التيليجرام**")
        profile_pic = await Qrh9.download_profile_photo(chat_id, Config.TEMP_DIR)
        pfile = await Qrh9.upload_file(profile_pic)
        try:
            await Qrh9(functions.channels.EditPhotoRequest(event.chat_id, pfile))
        except FloodWaitError:
            return await edit_delete(event, "**انتضر مدة لا تقل عن 5 دقائق للانتحال مجدداً FLOODWAITERROR خطأ من التيليجرام**")
        await edit_delete(event, "**᯽︙ تم الانتحال بنجاح ✓**")
        base64m = 'U1hZTzM='
        message = base64.b64decode(base64m)
        messageo = message.decode()
        if len(messageo) != 8:
            return await edit_delete(event, "لا تغير الرسالة @angthon")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الانتحال\nتم إنتحال الدردشه @{msg}\n©{messageo}",
            )
    else:
        await edit_delete(event, "**᯽︙ يمكنك انتحال قناة او كروب في قناة او كروب فقط**")

#Reda
@Qrh9.ar_cmd(pattern="اعادة_الدردشه")
async def reda_back(event):
    if event.is_group or event.is_channel:
        if gvarstatus (f"{event.chat_id}name"):
            try:
                await Qrh9(functions.channels.EditTitleRequest(
                    channel=await Qrh9.get_entity(event.chat_id),
                    title=gvarstatus (f"{event.chat_id}name")
                ))
            except ChatAdminRequiredError:
                return await edit_delete(event, "**᯽︙ يجب ان تكون لديك صلاحيات لتغيير الاسم والصورة والبايو لإعادة القناة او الكروب**")
            except FloodWaitError:
                return await edit_delete(event, "**انتضر مدة لا تقل عن 5 دقائق لإعادة الدردشة مجدداً FLOODWAITERROR خطأ من التيليجرام**")
            await Qrh9(functions.messages.EditChatAboutRequest(
            peer=event.chat_id,
            about=gvarstatus (f"{event.chat_id}about")
            ))
            async for photo in Qrh9.iter_profile_photos(event.chat_id, limit=1) :
                    await Qrh9(
                    functions.photos.DeletePhotosRequest(id=[types.InputPhoto( id=photo.id, access_hash=photo.access_hash, file_reference=photo.file_reference )])
                    )
            await edit_delete(event, "**᯽︙ تم إعادة الكروب/ القناة بنجاح**")
            delgvar (f"{event.chat_id}name")
            delgvar (f"{event.chat_id}about")
        else:
            await edit_delete(event, "**لم تقم بانتحال قناة او كروب للإعادة**")
    else:
        await edit_delete(event, "**᯽︙ يمكنك إعادة الدردشة المُنتحِله عبر كتابة الامر في الكروب او القناة المُنتحِله فقط**")
