import random
from telethon import events
import random, re

from SHRU.utils import admin_cmd

import asyncio
from SHRU import Qrh9
from Qrh9.razan._islam import *
from ..core.managers import edit_or_reply

plugin_category = "extra" 

#by ~ @SX9OO
@Qrh9.ar_cmd(
    pattern="اذكار الصباح",
    command=("اذكار الصباح", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           roze = random.choice(razan)
           return await event.edit(f"{roze}")
#by ~ @SX9OO
@Qrh9.ar_cmd(
    pattern="اذكار المساء$",
    command=("اذكار المساء", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           ror = random.choice(roz)
           return await event.edit(f"{ror}")
            
#by ~ @RR 9R7
@Qrh9.ar_cmd(
    pattern="احاديث$",
    command=("احاديث", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           me = random.choice(roza)
           return await event.edit(f"{me}")

@Qrh9.ar_cmd(
    pattern="اذكار الاستيقاظ$",
    command=("اذكار الاستيقاظ", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           az = random.choice(rozan)
           return await event.edit(f"{az}")
                     
@Qrh9.ar_cmd(
    pattern="اذكار النوم$",
    command=("اذكار النوم", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           rr = random.choice(rozmuh)
           return await event.edit(f"{rr}")
           
@Qrh9.ar_cmd(
    pattern="اذكار الصلاة$",
    command=("اذكار الصلاة", plugin_category),)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
           rm = random.choice(rzane)
           return await event.edit(f"{rm}")

@Qrh9.ar_cmd(
    pattern="اوامر الاذكار$",
    command=("اوامر الاذكار", plugin_category),)
async def _(event):
    await event.edit(
        "قائمة أوامر الأذكار:\n"
        "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
        "اختر أحدى هذه القوائم:\n\n"
        "- ( `.اذكار الصباح` )\n"
        "- ( `.اذكار المساء` )\n"
        "- ( `.اذكار النوم` )\n"
        "- ( `.اذكار الصلاة` )\n"
        "- ( `.اذكار الاستيقاظ` )\n"
        "- ( `.احاديث` )\n"
        "- ( `.اذكار` )\n"
        "- ( `.اذكار عشر` )\n"
        "- ( `.حديث` )\n"
        "- ( `.كم باقي` )\n"
        "- ( `.آية` )\n\n"
        "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
        "⌔︙CH: @SXYO3"
    )         
shortcuts = {}

@Qrh9.on(events.NewMessage(pattern=r"^.اختصر (.+) (.+)"))
async def add_shortcut(event):
    msg = event.pattern_match.group(1)
    shortcut = event.pattern_match.group(2)
    shortcuts[shortcut] = msg
    await event.edit(f"تم اضافة اختصار: `{shortcut}`")

@Qrh9.on(events.NewMessage(pattern=r"^\.(.+)"))
async def expand_shortcut(event):
    shortcut = event.pattern_match.group(1)
    if shortcut in shortcuts:
        msg = shortcuts[shortcut]
        await event.edit(msg)

@Qrh9.on(events.NewMessage(pattern=r"^.قائمه الاختصار|قائمة الاختصار"))
async def show_shortcuts(event):
    if not shortcuts:
        await event.edit("ليس هناك اختصارات مضافه")
        return
    reply = "**الاختصارات:**\n"
    for shortcut, msg in shortcuts.items():
        reply += f"`{shortcut}` = `{msg}`\n"
    await event.edit(reply)
@Qrh9.on(events.NewMessage(pattern=r"^\.امسح (.+)$"))
async def delete_shortcut(event):
    shortcut = event.pattern_match.group(1).lower()
    
    if shortcut in shortcuts:
        del shortcuts[shortcut]
        await event.edit(f"الاختصار `{shortcut}` تم حذفه بنجاح")
    else:
        await event.edit(f"الاختصار `{shortcut}` غير موجود")