import random
import re
import time
import asyncio
import os
from datetime import datetime
from platform import python_version
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from SHRU import Qrh9
from random import choice
from Qrh9.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from SHRU import StartTime, Qrh9, JEPVERSION
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention
 
plugin_category = "utils"
async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object
#كتـابة وعـديل:  @ll1iltت
file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)

@Qrh9.ar_cmd(pattern="فحص(?:\s|$)([\s\S]*)")

async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "** ᯽︙ يتـم التـأكـد انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "⿻┊‌‎"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "[**父 Vip member🎖️父**](t.me/SXYO3)" if user.id in Config.Vip_members else "父[𝘼𝙇𝙨𝙖𝙝𝙚𝙧 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 ✓](t.me/Sxyo3)父"
    Qrue_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC or "https://telegra.ph/file/4d3a48331f232ad0246f3.mp4"
    Qrh9_caption = gvarstatus("ALIVE_TEMPLATE") or Temp_Vip if user.id in Config.Vip_members else temp
    caption = Qrh9_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jepver=JEPVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        Tare5=installation_time,
    )
    if Qrue_IMG:
        SHRU = [x for x in Qrue_IMG.split()]
        PIC = random.choice(SHRU)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )

Temp_Vip = """{ALIVE_TEXT}
**‎{EMOJI}‌‎ الأسم  𖠄 {mention}** ٫
**‌‎{EMOJI}‌‎ اصدار البايثون 𖠄 `{pyver}`** ٫
**‌‎{EMOJI}‌‎ الساحر 𖠄 `{telever}`** ٫
**‌‎{EMOJI}‌‎ وقت التشغيل 𖠄 `{uptime}`** ٫
‌‎**{EMOJI}‌‎‌‎ البنك 𖠄 `{ping}`** ٫
‌‎**{EMOJI}‌‎‌‎ التاريخ 𖠄 `{Tare5}`** ٫
** Vip Member **"""

temp = """{ALIVE_TEXT}
**‎{EMOJI}‌‎𝙽𝙰𝙼𝙴 𖠄 {mention}** ٫
**‌‎{EMOJI}‌‎𝙿𝚈𝚃𝙷𝙾𝙽 𖠄 `{pyver}`** ٫
**‌‎{EMOJI}‌‎ALSAHER 𖠄 `{telever}`** ٫
**‌‎{EMOJI}‌‎𝚄𝙿𝚃𝙸𝙼𝙴 𖠄 `{uptime}`** ٫
‌‎**{EMOJI}‌‎‌‎𝙿𝙸𝙽𝙶 𖠄 `{ping}`** ٫
‌‎**{EMOJI}‌‎‌‎𝚂𝙴𝚃𝚄𝙿 𝙳𝙰𝚃𝙴 𖠄 `{Tare5}`** ٫
**𖠄 ALSAHER 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𖠄**"""
