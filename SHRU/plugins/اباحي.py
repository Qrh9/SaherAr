import os
import requests
from telethon import events
from PIL import Image
from moviepy.editor import VideoFileClip
from SHRU import Qrh9
from ..core.managers import edit_or_reply
from ..Config import Config 

nsfw_status = {}

def check_nsfw(media_path):
    api_url = 'https://api.sightengine.com/1.0/check.json'
    payload = {
        'models': 'nudity-2.0',
        'api_user': Config.API_USER,  
        'api_secret': Config.API_SECRET,  
    }
    with open(media_path, 'rb') as media_file:
        response = requests.post(api_url, files={'media': media_file}, data=payload)
    return response.json()

async def convert_sticker_to_image(sticker_path):
    """Convert a sticker (webp) to an image (png)"""
    img = Image.open(sticker_path).convert("RGB")
    output_path = sticker_path.replace(".webp", ".png")
    img.save(output_path, "PNG")
    return output_path

async def convert_gif_to_video(gif_path):
    """Convert a gif to a video (mp4)"""
    clip = VideoFileClip(gif_path)
    output_path = gif_path.replace(".gif", ".mp4")
    clip.write_videofile(output_path)
    return output_path

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

    if event.photo or event.sticker or event.document:  
        try:
            media_path = await Qrh9.download_media(event.media)

            if event.sticker:
                if media_path.endswith(".webp"):
                    media_path = await convert_sticker_to_image(media_path)
            
            elif media_path.endswith(".gif"):
                media_path = await convert_gif_to_video(media_path)

            result = check_nsfw(media_path)

            sexual_activity = result.get('nudity', {}).get('sexual_activity', 0)
            sexual_display = result.get('nudity', {}).get('sexual_display', 0)

            if sexual_activity >= 0.85 or sexual_display >= 0.85:
                if event.is_group:
                    if event.is_channel and event.client.has_permissions(event.chat_id, delete_messages=True):
                        await event.delete()
                    else:
                        await event.reply("⚠️ تم اكتشاف صورة أو ملصق إباحي - يرجى اتخاذ إجراء @admin.")
                        
        except Exception as e:
            await event.reply(f"⚠️ حدث خطأ أثناء فحص الوسائط: {e}")
