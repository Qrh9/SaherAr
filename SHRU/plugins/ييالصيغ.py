import asyncio
import logging
import os
import time
from datetime import datetime
from telethon import events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerChannel
from telethon.errors import ChannelPrivateError
from telethon.utils import get_peer_id
from SHRU import Qrh9
from telethon import types
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type, progress, thumb_from_audio
from ..helpers.functions import (
    convert_toimage,
    convert_tosticker,
    vid_to_gif,
)
from ..helpers.utils import _cattools, _catutils, _format, parse_pre, reply_id

plugin_category = "misc"

if not os.path.isdir("./temp"):
    os.makedirs("./temp")


LOGS = logging.getLogger(__name__)
PATH = os.path.join("./temp", "temp_vid.mp4")

thumb_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
cancel_process = False

#Copyright  By  @SXYO3  © 2021
#WRITE BY  @ll1ilt  
#Edited By Reda 



@Qrh9.ar_cmd(
    pattern=r"حفظ_المحتوى (.+)",
    command=("حفظ_المحتوى", plugin_category),
    info={
        "header": "حفظ الصور والفيديوهات والملفات إذا وجد في الرسالة.",
        "description": "يقوم بحفظ الصور والفيديوهات والملفات والنص إذا وجد في الرسالة.",
        "usage": "{tr}حفظ الصور <رابط الرسالة>",
    },
)
async def save_media(event):
    message_link = event.pattern_match.group(1)

    if not message_link:
        return await event.edit("يرجى تحديد رابط الرسالة!")

    save_dir = "media"
    os.makedirs(save_dir, exist_ok=True)

    try:
        message_link_parts = str(message_link).split("/")
        
        if message_link_parts:
            if message_link_parts[-2] == "c":
                channel_username_or_id = int(message_link_parts[-3])
                message_id = int(message_link_parts[-1])
            else:
                channel_username_or_id = message_link_parts[-2]
                message_id = int(message_link_parts[-1])
        else:
            return await event.edit("تحقق من الرابط، لأنه غير صحيح")
    except Exception as e:
        return await event.edit(f"حدث خطأ قم بتوجيه الرسالة لمطوري @rd0r0\n{e}")
    
    try:
        if int(channel_username_or_id):
            channel_username_or_id = int("-100" + str(channel_username_or_id))
        
        entity = await Qrh9.get_entity(channel_username_or_id)      
        message = await Qrh9.get_messages(entity, ids=message_id)
        if not message:
            return await event.edit("الرابط غلط او الرسالة غير موجوده")
    except ChannelPrivateError:
        await event.edit("يجب أن تنضم للقناة أولاً لتستطيع الحفظ منها")
    #except Exception as e:
       # return await event.edit(f"An error occurred while retrieving the message. Error: {str(e)}")

    try:
        message = await Qrh9.get_messages(channel_username_or_id, ids=message_id)
        if not message:
            return await event.edit("رابط الرسالة غير صالح!")

        if message.media:
            file_ext = ""
            if message.photo:
                file_ext = ".jpg"
            elif message.video:
                file_ext = ".mp4"
            elif message.document:
                if hasattr(message.document, "file_name"):
                    file_ext = os.path.splitext(message.document.file_name)[1]

            if not file_ext:
                return await event.edit(f"الرسالة لا تحتوي على ميديا!\n{message.message}")

            file_path = os.path.join(save_dir, f"media_{message.id}{file_ext}")
            await Qrh9.download_media(message, file=file_path)

            await Qrh9.send_file('me', file=file_path, caption=message.text)

            os.remove(file_path)
            await event.edit(f"تم حفظ الميديا بنجاح!\n\nرابط الرسالة: {message_link}")
        else:
            await event.edit("الرسالة لا تحتوي على ميديا!")
    except Exception as e:
        await event.edit(f"حدث خطأ أثناء حفظ الرسالة. الخطأ: {str(e)}")

        
@Qrh9.ar_cmd(
    pattern="تحويل صورة$",
    command=("تحويل صورة", plugin_category),
    info={
        "header": "Reply this command to a sticker to get image.",
        "description": "This also converts every media to image. that is if video then extracts image from that video.if audio then extracts thumb.",
        "usage": "{tr}stoi",
    },
)
async def _(event):
    "Sticker to image Conversion."
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "᯽︙ يجـب عليـك الرد عـلى الملصق لتحويـله الـى صورة ⚠️"
        )
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "᯽︙ غـير قـادر على تحويل الملصق إلى صورة من هـذا الـرد ⚠️"
        )
    meme_file = convert_toimage(output[1])
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()

@Qrh9.ar_cmd(
    pattern="الغاء سيف$",
    command=("الغاء سيف", plugin_category),
    info={
        "header": "إلغاء عملية حفظ الميديا.",
        "description": "يقوم بإلغاء العملية الجارية لحفظ الميديا من القنوات.",
        "usage": "{tr}إلغاء حفظ الميديا",
    },
)
async def Hussein(event):
    "إلغاء عملية حفظ الميديا."
    global cancel_process
    cancel_process = True
    await event.edit("تم إلغاء عملية حفظ الميديا.")

Qrh9.on(events.NewMessage(incoming=True))
async def check_cancel(event):
    global cancel_process
    if isinstance(event.message, MessageService) and event.message.action and isinstance(event.message.action, MessageActionChannelMigrateFrom):
        cancel_process = True

@Qrh9.ar_cmd(
    pattern="سيف(?: |$)(.*) (\d+)",
    command=("سيف", plugin_category),
    info={
        "header": "حفظ الميديا من القنوات ذات تقييد المحتوى.",
        "description": "يقوم بحفظ الميديا (الصور والفيديوهات والملفات) من القنوات ذات تقييد المحتوى.",
        "usage": "{tr}حفظ الميديا اسم_القناة الحد",
    },
)
async def Hussein(event):
    "حفظ الميديا من القنوات ذات تقييد المحتوى."
    global cancel_process
    
    channel_username = event.pattern_match.group(1)
    limit = int(event.pattern_match.group(2))
    
    if not channel_username:
        return await event.edit("يجب تحديد اسم القناة!")
    
    save_dir = "media"
    os.makedirs(save_dir, exist_ok=True)
    
    try:
        channel_entity = await Qrh9.get_entity(channel_username)
        messages = await Qrh9.get_messages(channel_entity, limit=limit)
    except Exception as e:
        return await event.edit(f"حدث خطأ أثناء جلب الرسائل من القناة. الخطأ: {str(e)}")

    for message in messages:
        try:
            if message.media:
                file_ext = ""
                if message.photo:
                    file_ext = ".jpg"
                elif message.video:
                    file_ext = ".mp4"
                elif message.document:
                    if hasattr(message.document, "file_name"):
                        file_ext = os.path.splitext(message.document.file_name)[1]
                    else:
                        # Handle documents without file_name attribute
                        file_ext = ""
                
                if not file_ext:
                    continue
                
                file_path = os.path.join(save_dir, f"media_{message.id}{file_ext}")
                await message.download_media(file=file_path)
                await Qrh9.send_file("me", file=file_path)
                os.remove(file_path)
            
            if cancel_process:
                await event.edit("تم إلغاء عملية حفظ الميديا.")
                cancel_process = False
                return
        except Exception as e:
            print(f"حدث خطأ أثناء حفظ الرسالة {message.id}. الخطأ: {str(e)}")
            continue

    await event.edit(f"تم حفظ الميديا من القناة {channel_username} بنجاح.")

@Qrh9.ar_cmd(
    pattern="تحويل ملصق$",
    command=("تحويل ملصق", plugin_category),
    info={
        "header": "Reply this command to image to get sticker.",
        "description": "This also converts every media to sticker. that is if video then extracts image from that video. if audio then extracts thumb.",
        "usage": "{tr}itos",
    },
)
async def _(event):
    "Image to Sticker Conversion."
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await edit_delete(
            event, "᯽︙ يجـب عليـك الرد عـلى الصـورة لتحويـلها الـى مـلصق ⚠️"
        )
    output = await _cattools.media_to_pic(event, reply)
    if output[1] is None:
        return await edit_delete(
            output[0], "᯽︙ غـير قـادر على استـخراج الـملصق من هـذا الـرد ⚠️"
        )
    meme_file = convert_tosticker(output[1])
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()

@Qrh9.ar_cmd(
    pattern="تحويل (mp3|voice)$",
    command=("تحويل", plugin_category),
    info={
        "header": "Converts the required media file to voice or mp3 file.",
        "usage": [
            "{tr}تحويل بصمة",
            "{tr}تحويل بصمة",
        ],
    },
)
async def _(event):
    "Converts the required media file to voice or mp3 file."
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "**᯽︙ يـجب الـرد على اي مـلف اولا ⚠️**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "**᯽︙ يـجب الـرد على اي مـلف اولا ⚠️**")
        return
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "᯽︙ يتـم التـحويل انتـظر قليـلا ⏱")
    try:
        start = datetime.now()
        c_time = time.time()
        downloaded_file_name = await event.client.download_media(
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "trying to download")
            ),
        )
    except Exception as e:
        await event.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit(
            "᯽︙ التحـميل الى `{}` في {} من الثواني ⏱".format(downloaded_file_name, ms)
        )
        new_required_file_name = ""
        new_required_file_caption = ""
        command_to_run = []
        voice_note = False
        supports_streaming = False
        if input_str == "voice":
            new_required_file_caption = "voice_" + str(round(time.time())) + ".opus"
            new_required_file_name = (
                Config.TMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-map",
                "0:a",
                "-codec:a",
                "libopus",
                "-b:a",
                "100k",
                "-vbr",
                "on",
                new_required_file_name,
            ]
            voice_note = True
            supports_streaming = True
        elif input_str == "mp3":
            new_required_file_caption = "mp3_" + str(round(time.time())) + ".mp3"
            new_required_file_name = (
                Config.TMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-vn",
                new_required_file_name,
            ]
            voice_note = False
            supports_streaming = True
        else:
            await event.edit("᯽︙ غـير مدعوم ❕")
            os.remove(downloaded_file_name)
            return
        process = await asyncio.create_subprocess_exec(
            *command_to_run,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        os.remove(downloaded_file_name)
        if os.path.exists(new_required_file_name):
            force_document = False
            await event.client.send_file(
                entity=event.chat_id,
                file=new_required_file_name,
                allow_cache=False,
                silent=True,
                force_document=force_document,
                voice_note=voice_note,
                supports_streaming=supports_streaming,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "trying to upload")
                ),
            )
            os.remove(new_required_file_name)
            await event.delete()
            
#Copyright  By  @SXYO3  © 2021
#WRITE BY  @ll1ilt

@Qrh9.ar_cmd(
    pattern="تحويل متحركة ?([0-9.]+)?$",
    command=("تحويل متحركة", plugin_category),
    info={
        "header": "Reply this command to a video to convert it to gif.",
        "description": "By default speed will be 1x",
        "usage": "{tr}vtog <speed>",
    },
)
async def _(event):
    "Reply this command to a video to convert it to gif."
    reply = await event.get_reply_message()
    mediatype = media_type(event)
    if mediatype and mediatype != "video":
        return await edit_delete(event, "᯽︙ يجـب عليك الـرد على فيديو اولا لتحـويله ⚠️")
    args = event.pattern_match.group(1)
    if not args:
        args = 2.0
    else:
        try:
            args = float(args)
        except ValueError:
            args = 2.0
    catevent = await edit_or_reply(event, "**᯽︙ يتـم التحويل الى متـحركه انتـظر ⏱**")
    inputfile = await reply.download_media()
    outputfile = os.path.join(Config.TEMP_DIR, "vidtogif.gif")
    result = await vid_to_gif(inputfile, outputfile, speed=args)
    if result is None:
        return await edit_delete(event, "**᯽︙ عـذرا لا يمكـنني تحويل هذا الى متـحركة ⚠️**")
    jasme = await event.client.send_file(event.chat_id, result, reply_to=reply)
    await _catutils.unsavegif(event, jasme)
    await catevent.delete()
    for i in [inputfile, outputfile]:
        if os.path.exists(i):
            os.remove(i)
