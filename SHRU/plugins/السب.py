from SHRU import l313l
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events
from ..core.managers import edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
Mn3_sb = [
    "عير", "كس ", "كواد", "تنيج", "كسمك", " فرخ", "خنجه", "استنياج", "سرسري",
    " عريض ", "خنيث", "بلاع", "عيوره", "طيزك", "المنيوج", "المنيوك", "تناحه",
    "الديوث", "قريخ", "كحاب", "كحبه"
]

addgvar("delete_enabled", False)

@l313l.on(events.NewMessage)
async def Hussein(event):
    if gvarstatus("delete_enabled") and gvarstatus("enable_speech_ban") and any(word in event.raw_text for word in Mn3_sb):
        await event.delete()

@l313l.ar_cmd(pattern=r"السب تفعيل$")
async def sbt36el(event):
    if gvarstatus("delete_enabled"):
        await event.edit("᯽︙ الأمر مفعل بالفعل")
    else:
        addgvar("delete_enabled", True)
        await event.edit("᯽︙ تم منع السب بنجاح ✓")

@l313l.ar_cmd(pattern=r"السب تعطيل$")
async def sbtf3el(event):
    if not gvarstatus("delete_enabled"):
        await event.edit("᯽︙ الأمر معطل بالفعل")
    else:
        delgvar("delete_enabled", False)
        await event.edit("᯽︙ تم السماح بالسب هنا ✓")
