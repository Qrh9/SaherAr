import asyncio
import random
from telethon import events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
from SHRU import Qrh9
from ..core.managers import edit_or_reply

ausa = {}
rioishere = {}

DE = ["https://t.me/saherhelp"]  

@Qrh9.ar_cmd(
    pattern="نشر (https?://[^\s]+)(?: (\d+))?(?: (طبيعي|امن))?",
    command=("نشر", "utils"),
    info={
        "header": "نشر تلقائي سادلايفو",
        "usage": "{tr}نشر <رابط المجموعة> <عدد الثواني> <طبيعي/امن> بالرد على رسالة",
    }
)
async def astaer(event):
    reply = await event.get_reply_message()
    if not reply:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على رسالة ليتم نشرها.")
    
    speedrunminecraft = event.pattern_match.group(1).strip()

    if speedrunminecraft in DE:
        return await edit_or_reply(event, "⌔∮ لا يمكن النشر في هذه المجموعة.")

    interval = int(event.pattern_match.group(2)) if event.pattern_match.group(2) else 60
    mode = event.pattern_match.group(3) or "طبيعي"  

    if speedrunminecraft in rioishere:
        return await edit_or_reply(event, f"⌔∮ النشر قيد التنفيذ بالفعل لهذه المجموعة: {speedrunminecraft}")

    rioishere[speedrunminecraft] = reply

    async def posts():
        while speedrunminecraft in rioishere:
            try:
                if reply.sticker:
                    await Qrh9.send_file(speedrunminecraft, reply.media)
                elif reply.reactions and reply.reactions.recent_reactions:
                    for reaction in reply.reactions.recent_reactions:
                        await Qrh9(SendReactionRequest(
                            peer=speedrunminecraft,
                            msg_id=reply.id,
                            reaction=[ReactionEmoji(emoticon=reaction.emoticon)]
                        ))
                else:
                    if mode == "امن":
                        modified_message = wsasdas(reply.message)
                        await Qrh9.send_message(speedrunminecraft, modified_message)
                    else:
                        await Qrh9.send_message(speedrunminecraft, rioishere[speedrunminecraft].message)
                await asyncio.sleep(interval)
            except Exception as e:
                await edit_or_reply(event, f"⌔∮ حدث خطأ أثناء النشر: {str(e)}")
                break

    task = asyncio.create_task(posts())
    ausa[speedrunminecraft] = task

    await edit_or_reply(event, f"⌔∮ تم بدء النشر التلقائي لهذه المجموعة: {speedrunminecraft} كل {interval} ثانية، الوضع: {mode}")

@Qrh9.ar_cmd(
    pattern="نشر_انهاء (https?://[^\s]+)",
    command=("نشر_انهاء", "utils"),
    info={
        "header": "إيقاف النشر التلقائي.",
        "usage": "{tr}نشر_انهاء <رابط المجموعة>",
    }
)
async def unpot(event):
    speedrunminecraft = event.pattern_match.group(1).strip()

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
        await edit_or_reply(event, "⌔∮ لا يوجد نشر قيد التنفيذ حاليًا.")

#امك شلونها
def wsasdas(message):
    mystepsisistoooohot = ["\u200B", "\u200C", "\u200D", "\u2060"]  
    index = random.randint(0, len(message))
    return message[:index] + random.choice(mystepsisistoooohot) + message[index:]
