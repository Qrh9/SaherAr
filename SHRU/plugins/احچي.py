"""
SHRU team ©
By Reda
sub Hussein
"""
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment

from SHRU import l313l
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type
from ..helpers.utils import reply_id
import ocrspace

plugin_category = "utils"

#لتخمط الملف اذا انته ابن گحبة انسخ وألصق لسورسك وصيح اني مطور الملف متعوب عليه وشغل ايد

@l313l.ar_cmd(pattern="احجي(?:\s|$)([\s\S]*)",
               command=("احجي", plugin_category),
              )
async def _(event):
    "تحويل الكلام الى نص."
    
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    lan = input_str
    if not lan:
         return await edit_delete(event, "يجب ان تضع اختصار اللغة المطلوبة")
    
    #ted = await edit_or_reply(event, str(lan))
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
    mediatype = media_type(reply)
    if not reply or (mediatype and mediatype not in ["Voice", "Audio"]):
        return await edit_delete(
            event,
            "`قم بالرد على رسالة او مقطع صوتي لتحويله الى نص.`",
        )
    jepevent = await edit_or_reply(event, "`يجري تنزيل الملف...`")
    oggfi = await event.client.download_media(reply, Config.TEMP_DIR)
    await jepevent.edit("`يجري تحويل الكلام الى نص....`")
    r = sr.Recognizer()
    #audio_data = open(required_file_name, "rb").read()
    ogg = oggfi.removesuffix('.ogg')
   
    AudioSegment.from_file(oggfi).export(f"{ogg}.wav", format="wav")
    user_audio_file = sr.AudioFile(f"{ogg}.wav")
    with user_audio_file as source:
         audio = r.record(source)

    
    try:
         text = r.recognize_google(audio, language=str(lan))
    except ValueError:
         return await edit_delete(event, "**لا يوجد كلام في المقطع الصوتي**")
    except BaseException as err:
         return await edit_delete(event, f"**!لا يوجد كلام في هذا المقطع الصوتي\n{err}**")
    end = datetime.now()
    ms = (end - start).seconds
    
    string_to_show = "**يگول : **`{}`".format(
            text
        )
    await jepevent.edit(string_to_show)
    # now, remove the temporary file
    os.remove(oggfi)
    os.remove(f"{ogg}.wav")

langs = {
    'عربي': 'ara',
    'بلغاري': 'bul',
    'صيني مبسط': 'chs',
    'صيني تقليدي ': 'cht',
    'كرواتي': 'hrv',
    'دنماركي': 'dan',
    'الماني': 'dut',
    'انجليزي': 'eng',
    'فنلندي': 'fin',
    'فرنسي': 'fre',
    'الماني': 'ger',
    'يوناني': 'gre',
    'هنغاري': 'hun',
    'كوري': 'kor',
    'ايطالي': 'ita',
    'ياباني': 'jpn',
    'نرويجي': 'nor',
    'بولندي': 'pol',
    'برتغالي': 'por',
    'روسي': 'rus',
    'سلوفيني': 'slv',
    'اسباني': 'spa',
    'سويدي': 'swe',
    'تركي': 'tur',
}

def to_text(pic, api):
    try:
        output = api.ocr_file(open(pic, 'rb'))
    except Exception as e:
        return "حدث الخطأ التالي:\n{e}"
    else:
        if output:
            return output
        else:
            return "حدث خطأ في النضام , حاول مجدداً"
    finally:
        os.remove(pic)

@l313l.ar_cmd(pattern="استخرج(?:\s|$)([\s\S]*)",
               command=("استخرج", plugin_category),
              )
async def _(event):
    reply = await event.get_reply_message()
    lan = event.pattern_match.group(1)
    if not reply:
     return edit_delete(event, "**᯽︙ قم بالرد على الصورة المراد استخراج النص منه**")
    pic_file = await l313l.download_media(reply, Config.TMP_DOWNLOAD_DIRECTORY)
    if not pic_file:
        return await edit_delete(event, "**᯽︙ قم بالرد على صورة**")
    else:
     if not lan:
            api = ocrspace.API()
     else:    
            try:  
             lang = langs[lan.replace(" ", "")]
             api = ocrspace.API(language=lang)
            except BaseException as er:
             return await edit_delete(event, "**᯽︙ !لا يوجد هكذا لغة**")
     await edit_or_reply(event, "**᯽︙ يجري استخراج النص...**")
     await edit_or_reply(event, to_text(pic_file, api))
