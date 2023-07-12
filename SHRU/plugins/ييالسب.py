from SHRU import l313l
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events

from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events
from ..helpers import reply_id, time_formatter
from ..core.managers import edit_or_reply
from ..core.managers import edit_delete
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

Mn3_sb = [
    "عير", "كواد", "تنيج", "كسمك", "فرخ", "خنجه", "استنياج", "سرسري",
    "عريض", "خنيث", "بلاع", "عيوره", "طيزك", "المنيوج", "المنيوك", "تناحه",
    "الديوث", "قريخ", "كحاب", "كحبه" , " كس "
]


@l313l.on(events.NewMessage)
async def Hussein(event):
    if gvarstatus("delete_enabled") and any(word in event.raw_text for word in Mn3_sb):
        await event.delete()

@l313l.ar_cmd(pattern=r"السب تفعيل$")
async def sbt36el(event):
    if gvarstatus("delete_enabled") is not None and gvarstatus("delete_enabled") == "true":
        return await edit_delete(event, "**امر منع السب  مُفعل بالفعل **")
    else:
        addgvar("delete_enabled", True)
        await event.edit("᯽︙ تم منع السب بنجاح ✓")

@l313l.ar_cmd(pattern=r"السب تعطيل$")
async def sbtf3el(event):
    if gvarstatus("delete_enabled") is not None and gvarstatus("delete_enabled") == "true":
        delgvar("delete_enabled")
        await event.edit("**᯽︙ تم تعطيل امر منع السب  بنجاح.**")
    else:
        return await edit_delete(event, "**امر منع السب مُعطل بالفعل🧸♥**")