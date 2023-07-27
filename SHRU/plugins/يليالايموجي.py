from SHRU import l313l 
import os
from ..helpers.utils import _format
from ..helpers.functions.utube import _mp3Dl, get_yt_video_id, get_ytthumb, ytsearch
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import progress, reply_id

from pydub import AudioSegmen
plugin_category = "fun"
@l313l.ar_cmd(
    pattern="عزل$",
    command=("عزل", plugin_category),
    info={
        "header": "قم بعزل صوت المغني والأغنية من ملف صوتي",
        "usage": "{tr}عزل (بالرد على ملف الصوتي للأغنية)",
    },
)
async def isolate_vocals(event):
    reply = await event.get_reply_message()
    if not reply or not reply.file:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على ملف الصوتي للأغنية.")
    
    audio_file = await reply.download_media()
    
    # فصل صوت المغني (أحفظه في ملف منفصل)
    vocals_file = "vocals_only.mp3"
    os.system(f'ffmpeg -i "{audio_file}" -vn -sn -c:s copy "{vocals_file}"')
    
    # فصل صوت الأغنية (أحفظه في ملف منفصل)
    accompaniment_file = "accompaniment_only.mp3"
    os.system(f'ffmpeg -i "{audio_file}" -acodec copy -map 0:1 "{accompaniment_file}"')
    
    # إرسال الملفين مع التنبيه بأن الملفات منفصلة
    await event.client.send_file(event.chat_id, vocals_file, reply_to=reply)
    await event.client.send_message(event.chat_id, "**⌔∮ هذا ملف صوت المغني فقط (بدون الأغنية).**")
    await event.client.send_file(event.chat_id, accompaniment_file, reply_to=reply)
    await event.client.send_message(event.chat_id, "**⌔∮ هذا ملف صوت الأغنية فقط (بدون المغني).**")
    
    # حذف الملفات المؤقتة
    os.remove(audio_file)
    os.remove(vocals_file)
    os.remove(accompaniment_file)