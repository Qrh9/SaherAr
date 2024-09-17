import random
from telethon import events
from SHRU import Qrh9
from ..core.managers import edit_or_reply

fshr_active = {}
default_words = [
    "⌔∮ عير بكسمك"
]

@Qrh9.on(events.NewMessage(pattern=r".فشر(?: |$)(.*)"))
async def fsh(event):
    reply = await event.get_reply_message()
    if not reply:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على رسالة الشخص")
    
    user_id = reply.sender_id
    words = event.pattern_match.group(1) or random.choice(default_words)
    
    fshr_active[user_id] = words
    await edit_or_reply(event, f"⌔∮ تم تفعيل الفشار على الشخص، كل ما يرسل رسالة راح يجيه الرد: {words}")

@Qrh9.on(events.NewMessage(pattern=r".ايقاف"))
async def fshar(event):
    reply = await event.get_reply_message()
    if not reply:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على رسالة")
    
    user_id = reply.sender_id
    if user_id in fshr_active:
        del fshr_active[user_id]
        await edit_or_reply(event, "⌔∮ تم ايقاف الفشار عن الشخص")
    else:
        await edit_or_reply(event, "⌔∮ لا يوجد فشار مشغل لهذا ")

@Qrh9.on(events.NewMessage())
async def fashr(event):
    if event.sender_id in fshr_active:
        response = fshr_active.get(event.sender_id)
        await event.reply(response)
