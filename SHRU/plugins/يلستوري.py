#بربك تخمط هيج كود يا فاشل💀
from SHRU import Qrh9
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon import events
from telethon import events

@Qrh9.on(admin_cmd(pattern="(رفع ستوري)"))
async def upload_story(event):
    if not event.reply_to_message:
        await event.reply("رد على صورة أو فيديو لرفعه كقصة")
        return

    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.reply("الرسالة التي رديت عليها لا تحتوي على وسائط")
        return

    media = reply_message.media
    file_id = media.document.file_id
    if media.document.mime_type == "image/jpeg":
        file_type = "photo"
    elif media.document.mime_type == "video/mp4":
        file_type = "video"
    else:
        await event.reply("الوسائط التي رديت عليها غير مدعومة")
        return

    await bot.send_file(
        event.chat_id,
        file_id,
        caption=reply_message.caption,
        force_document=False,
        file_type=file_type,
    )
    await event.reply("تم رفع القصة بنجاح")
