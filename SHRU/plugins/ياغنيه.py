import asyncio
from telethon import events
from SHRU import Qrh9
from ..core.managers import edit_or_reply

ausa = {}
rioishere = {}

@Qrh9.ar_cmd(
    pattern="نشر (https?://[^\s]+)(?: (\d+))?",
    command=("نشر", "utils"),
    info={
        "header": "نشر تلقائي لرسالة كل فترة زمنية معينة.",
        "usage": "{tr}نشر <رابط المجموعة> <عدد الثواني> بالرد على رسالة.",
    }
)
async def astaer(event):
    reply = await event.get_reply_message()
    if not reply:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على رسالة ليتم نشرها.")
    
    speedrunminecraft = event.pattern_match.group(1)
    speedrunminecraft = speedrunminecraft.strip()
    
    interval = event.pattern_match.group(2)
    interval = int(interval) if interval else 60 

    if speedrunminecraft in rioishere:
        return await edit_or_reply(event, f"⌔∮ النشر قيد التنفيذ بالفعل لهذه المجموعة: {speedrunminecraft}")

    rioishere[speedrunminecraft] = reply.message

    async def posts():
        while speedrunminecraft in rioishere:
            try:
                await Qrh9.send_message(speedrunminecraft, rioishere[speedrunminecraft])
                await asyncio.sleep(interval)  
            except Exception as e:
                await edit_or_reply(event, f"⌔∮ حدث خطأ أثناء النشر: {str(e)}")
                break
    
    task = asyncio.create_task(posts())
    ausa[speedrunminecraft] = task

    await edit_or_reply(event, f"⌔∮ تم بدء النشر التلقائي لهذه المجموعة: {speedrunminecraft} كل {interval} ثانية.")


@Qrh9.ar_cmd(
    pattern="نشر_انهاء (https?://[^\s]+)",
    command=("ايقاف_نشر", "utils"),
    info={
        "header": "إيقاف النشر التلقائي.",
        "usage": "{tr}ايقاف_نشر <رابط المجموعة>",
    }
)
async def unpot(event):
    speedrunminecraft = event.pattern_match.group(1)
    speedrunminecraft = speedrunminecraft.strip()

    if speedrunminecraft in rioishere:
        del rioishere[speedrunminecraft]
        ausa[speedrunminecraft].cancel()
        del ausa[speedrunminecraft]
        await edit_or_reply(event, f"⌔∮ تم إيقاف النشر لهذه المجموعة: {speedrunminecraft}")
    else:
        await edit_or_reply(event, f"⌔∮ لا يوجد نشر قيد التنفيذ لهذه المجموعة: {speedrunminecraft}")


@Qrh9.ar_cmd(
    pattern="قائمة_النشر$",
    command=("قائمة_النشر", "utils"),
    info={
        "header": "عرض قائمة المجموعات التي يتم النشر لها حاليًا",
        "usage": "{tr}قائمة_النشر",
    }
)
async def lis(event):
    if rioishere:
        active_groups = "\n".join(rioishere.keys())
        await edit_or_reply(event, f"⌔∮ قائمة المجموعات التي يتم النشر لها حاليًا:\n{active_groups}")
    else:
        await edit_or_reply(event, "⌔∮ لا يوجد نشر قيد التنفيذ حاليًا")
