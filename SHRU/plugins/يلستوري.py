from ..core.managers import edit_or_reply
from SHRU import Qrh9
from telethon import events

from telethon.sync import TelegramClient
from telethon import functions, types

@Qrh9.on(events.NewMessage(pattern='.قصة'))
async def upload_story(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.media:
            media = types.InputMediaUploadedPhoto(file=await Qrh9.upload_file(reply_message.media))
            result = await Qrh9(functions.stories.SendStoryRequest(
                peer='me',  # Sending the story to yourself
                media=media,
                privacy_rules=[types.InputPrivacyValueAllowAll()]
            ))
            await edit_or_reply(event, "✅ قصتك تم رفعها بنجاح!")
        else:
            await edit_or_reply(event, "❌ يرجى الرد على رسالة تحتوي على وسائط لرفعها كقصة.")
    else:
        await edit_or_reply(event, "❌ يرجى الرد على الرسالة التي تريد رفعها كقصة.")