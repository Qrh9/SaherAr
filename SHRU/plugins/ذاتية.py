from SHRU import Qrh9
from SaherAr.SHRU.utils.decorators import admin_cmd
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
from telethon import events
from SHRU import *
import datetime
from ..core.managers import edit_delete, edit_or_reply


ALSAHER_Asbo3 = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}

@Qrh9.on(admin_cmd(pattern="(جلب الصورة|جلب الصوره|ذاتيه|ذاتية|حفظ)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    ll1ilt = await event.get_reply_message()
    media = await ll1ilt.download_media()
    await bot.send_file(
        "me",
        media,
        caption=f"""
- تم حفظ الوسائط بنجاح ✓
- غير مبري الذمة إذا استخدمت الأمر للابتزاز
- CH: @SXYO3
- Dev: @allnught
  """,
    )
    await event.delete()

@Qrh9.on(admin_cmd(pattern="(الذاتية تشغيل|ذاتية تشغيل)"))
async def reda(event):
    if gvarstatus("savepicforme"):
        return await edit_delete(event, "**᯽︙حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً**")
    else:
        addgvar("savepicforme", "reda")
        await edit_delete(event, "**᯽︙تم تفعيل ميزة حفظ الذاتيات بنجاح ✓**")

@Qrh9.on(admin_cmd(pattern="(الذاتية تعطيل|ذاتية تعطيل)"))
async def reda_disable(event):
    if gvarstatus("savepicforme"):
        delgvar("savepicforme")
        return await edit_delete(event, "**᯽︙تم تعطيل حفظ الذاتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**᯽︙لم تقم بتفعيل حفظ الذاتيات لتعطيلها!**")

def srio(message):
    return (
        message.media_unread and 
        (message.photo or message.video or message.voice or message.audio) and 
        message.sender_id != 6320583148
    )

async def rios(event, caption):
    media = await event.download_media()
    sender = await event.get_sender()
    sender_id = event.sender_id
    date = event.date.strftime("%Y-%m-%d")
    day = ALSAHER_Asbo3[event.date.strftime("%A")]
    await bot.send_file(
        "me",
        media,
        caption=caption.format(sender.first_name, sender_id, date, day),
        parse_mode="markdown"
    )
    os.remove(media)

@Qrh9.on(events.NewMessage(func=lambda e: e.is_private and srio(e) and e.sender_id != bot.uid))
async def save_self_destruct_media(event):
    if gvarstatus("savepicforme"):
        caption = """**
           ✨ غير مبري الذمة إذا استعملته للأبتزاز ✨
✨ تم حفظ الذاتية بنجاح ✓
✨ تم الصنع : @SXYO3
✨ أسم المرسل : [{0}](tg://user?id={1})
✨ تاريخ الذاتية : `{2}`
✨ أرسلت في يوم `{3}`
       ✨ alsaher ✨
        **"""
        await rios(event, caption)
