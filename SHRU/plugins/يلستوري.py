from ..core.managers import edit_or_reply
from SHRU import Qrh9
from telethon import events

@Qrh9.on(events.NewMessage(pattern='.قصة'))
async def upload_story(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.media:
            await Qrh9.send_file(Qrh9.username, reply_message.media, caption="تم رفع القصة بواسطة" + reply_message.sender.first_name)
            await edit_or_reply(event,"✅ قصتك تم رفعها بنجاح!")
        else:
            await edit_or_reply(event," يرجى الرد على رسالة تحتوي على فيديو او صوره لرفعها كقصة.")
    else:
        await edit_or_reply(event," يرجى الرد على الرسالة التي تريد رفعها كقصة.")