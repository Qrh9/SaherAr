import os
from telethon import functions 
import subprocess
from SHRU.helpers.functions.functions import translate
from datetime import datetime
from ALSAHER import get_string



from gtts import gTTS


from SHRU import Qrh9


from ..core.managers import edit_delete, edit_or_reply

from . import deEmojify, reply_id


@Qrh9.ar_cmd(pattern="test(?:\s|$)([\s\S]*)")
async def reda(event):
    tr = translate("انا عراقي", lang_tgt="fa").replace("\ N", "\n")
    await edit_or_reply(event, tr)
    result = await Qrh9(functions.users.GetFullUserRequest(
        id='earthlink_telecommunications'
    ))
    await event.reply(result.stringify())



@Qrh9.ar_cmd(pattern="تكلم(?:\s|$)([\s\S]*)")

async def _(event):

    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str

    elif "|" in input_str:
        lan, text = input_str.split("|")

    else:

        await edit_or_reply(event, "- هذا نص غير صحيح")
        return
        text = text.strip()
        lan = lan.strip()

    HuReevent = await edit_or_reply(event, "⌔∮ جـار التسجيل انتـظر قليلا")


    if not os.path.isdir("./temp/"):

        os.makedirs("./temp/")

    required_file_name = "./temp/" + "voice.ogg"

    try:

        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
             required_file_name,
             "-map",
             "0:a",
             "-codec:a",
             "libopus",
             "-b:a",
             "100k",
             "-vbr",
             "on",
             required_file_name + ".opus"
        ]
        
        try:

            t_response = subprocess.check_output(

                command_to_execute, stderr=subprocess.STDOUT

            )

        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:

            await HuReevent.edit(str(exc))

        else:

            os.remove(required_file_name)

            required_file_name = required_file_name + ".opus"

        end = datetime.now()

        ms = (end - start).seconds

        await event.client.send_file(

            event.chat_id,

            required_file_name,

            reply_to=event.message.reply_to_msg_id,

            allow_cache=False,

            voice_note=True,

        )

        os.remove(required_file_name)

        await edit_delete(

            HuReevent,

            "تحويل النص {} الى مقطع صوتي في {} ثواني ".format(text[0:20], ms),

        )

    except Exception as e:

        await edit_or_reply(HuReevent, f"خطأ:\n{e}")
