import asyncio
from telethon import events
from SHRU import Qrh9
from ..core.managers import edit_or_reply

ausa = {}
rioishere = {}

@Qrh9.ar_cmd(
    pattern="نشر (https?://[^\s]+)",
    command=("نشر", "utils"),
    info={
        "header": "نشر تلقائي لرسالة كل دقيقة",
        "usage": "{tr}نشر <رابط المجموعة> بالرد على رسالة",
    }
)
async def astaer(event):
    reply = await event.get_reply_message()
    if not reply:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على رسالة ليتم نشرها.")
    
    sqe = event.pattern_match.group(1)
    sqe = sqe.strip()

    if sqe in rioishere:
        return await edit_or_reply(event, f"⌔∮ النشر قيد التنفيذ بالفعل لهذه المجموعة: {sqe}")

    rioishere[sqe] = reply.message

    async def posts():
        while sqe in rioishere:
            try:
                await Qrh9.send_message(sqe, rioishere[sqe])
                await asyncio.sleep(60)  # الانتظار لمدة دقيقة
            except Exception as e:
                await edit_or_reply(event, f"⌔∮ حدث خطأ أثناء النشر: {str(e)}")
                break
    
    task = asyncio.create_task(posts())
    ausa[sqe] = task

    await edit_or_reply(event, f"⌔∮ تم بدء النشر التلقائي لهذه المجموعة: {sqe}")


@Qrh9.ar_cmd(
    pattern="ايقاف_نشر (https?://[^\s]+)",
    command=("ايقاف_نشر", "utils"),
    info={
        "header": "إيقاف النشر التلقائي.",
        "usage": "{tr}ايقاف_نشر <رابط المجموعة>",
    }
)
async def unpot(event):
    sqe = event.pattern_match.group(1)
    sqe = sqe.strip()

    if sqe in rioishere:
        del rioishere[sqe]
        ausa[sqe].cancel()
        del ausa[sqe]
        await edit_or_reply(event, f"⌔∮ تم إيقاف النشر لهذه المجموعة: {sqe}")
    else:
        await edit_or_reply(event, f"⌔∮ لا يوجد نشر قيد التنفيذ لهذه المجموعة: {sqe}")


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
        await edit_or_reply(event, "⌔∮ لا يوجد نشر قيد التنفيذ حاليا")
