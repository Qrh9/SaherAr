import requests
from telethon import events
from SHRU import Qrh9
from ..core.managers import edit_or_reply

API_USER = '1816055771'
API_SECRET = 'EnGQHAX2SnQpyDH39rY6AmYSNuRbcGJG'
nsfw_active = True

def check_nsfw(image_path):
    api_url = 'https://api.sightengine.com/1.0/check.json'
    payload = {
        'models': 'nudity-2.0',
        'api_user': API_USER,
        'api_secret': API_SECRET,
    }
    with open(image_path, 'rb') as image_file:
        response = requests.post(api_url, files={'media': image_file}, data=payload)
    return response.json()

@Qrh9.ar_cmd(
    pattern="اباحيه_تفعيل$",
    command=("اباحيه_تفعيل", "utils"),
    info={
        "header": "تفعيل فلتر الصور الإباحية في المجموعة.",
        "usage": "{tr}اباحيه_تفعيل"
    }
)
async def enable_nsfw(event):
    global nsfw_active
    nsfw_active = True
    await edit_or_reply(event, "⌔∮ تم تفعيل فلتر الصور الإباحية.")

@Qrh9.ar_cmd(
    pattern="اباحيه_تعطيل$",
    command=("اباحيه_تعطيل", "utils"),
    info={
        "header": "تعطيل فلتر الصور الإباحية في المجموعة.",
        "usage": "{tr}اباحيه_تعطيل"
    }
)
async def disable_nsfw(event):
    global nsfw_active
    nsfw_active = False
    await edit_or_reply(event, "⌔∮ تم تعطيل فلتر الصور الإباحية.")

@Qrh9.on(events.NewMessage(incoming=True))
async def check_for_nsfw(event):
    if not nsfw_active:
        return

    if event.photo:
        try:
            image_path = await Qrh9.download_media(event.photo)
            
            result = check_nsfw(image_path)

            if result['nudity']['raw'] > 0.85:
                if event.is_group:
                    if event.is_channel:
                        await event.delete()  
                    else:
                        await event.reply("⚠️ صورة إباحية - @admin يرجى اتخاذ إجراء.")
        except Exception as e:
            await event.reply(f"⚠️ حدث خطأ أثناء فحص الصورة: {e}")
