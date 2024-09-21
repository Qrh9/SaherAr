import os
import requests
from telethon import events
from SHRU import Qrh9
from ..core.managers import edit_or_reply
from ..Config import Config

nsfw_status = {}
scanned_files = set()

def check_nsfw(image_path):
    api_url = 'https://api.sightengine.com/1.0/check.json'
    payload = {
        'models': 'nudity-2.0',
        'api_user': Config.API_USER,
        'api_secret': Config.API_SECRET,
    }
    with open(image_path, 'rb') as image_file:
        response = requests.post(api_url, files={'media': image_file}, data=payload)
    return response.json()

@Qrh9.ar_cmd(
    pattern="اباحيه_تفعيل$",
    command=("اباحيه_تفعيل", "utils"),
    info={
        "header": "تفعيل فلتر الصور الإباحية في الكروب.",
        "usage": "{tr}اباحيه_تفعيل"
    }
)
async def enable_nsfw(event):
    chat_id = event.chat_id
    nsfw_status[chat_id] = True
    await edit_or_reply(event, "⌔∮ تم تفعيل فلتر الصور الإباحية في هذا الكروب.")

@Qrh9.ar_cmd(
    pattern="اباحيه_تعطيل$",
    command=("اباحيه_تعطيل", "utils"),
    info={
        "header": "تعطيل فلتر الصور الإباحية في الكروب.",
        "usage": "{tr}اباحيه_تعطيل"
    }
)
async def disable_nsfw(event):
    chat_id = event.chat_id
    nsfw_status[chat_id] = False
    await edit_or_reply(event, "⌔∮ تم تعطيل فلتر الصور الإباحية في هذا الكروب.")

@Qrh9.on(events.NewMessage(incoming=True))
async def check_for_nsfw(event):
    chat_id = event.chat_id

    if not nsfw_status.get(chat_id, False):
        return

    if event.photo or event.gif or event.sticker:
        file_id = event.file.id

        if file_id in scanned_files:
            return

        try:
            image_path = await Qrh9.download_media(event.media)
            result = check_nsfw(image_path)

            scanned_files.add(file_id)

            sexual_activity = result.get('nudity', {}).get('sexual_activity', 0)
            sexual_display = result.get('nudity', {}).get('sexual_display', 0)

            if sexual_activity >= 0.85 or sexual_display >= 0.85:
                if event.is_group:
                    if event.is_channel and event.client.has_permissions(event.chat_id, delete_messages=True):
                        await event.delete()
                    else:
                        await event.reply("⚠️ تم اكتشاف محتوى غير لائق - يرجى اتخاذ إجراء @admin.")

        except Exception as e:
            await event.reply(f"⚠️ حدث خطأ أثناء فحص الملف: {e}")
