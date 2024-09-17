from telethon import events
from telethon.tl.functions.messages import SendReactionRequest
from SHRU import Qrh9
import random 
iz3aj_active = {}
emoje = ["😂","🔥"]

@Qrh9.on(events.NewMessage(pattern=r".ازعاج (.*)"))
async def start_iz3aj(event):
    emoji = event.pattern_match.group(1).strip()
    reply = await event.get_reply_message()
    if not reply:
        return await event.respond("⌔∮ يرجى الرد على رسالة الشخص.")
    
    user_id = reply.sender_id
    iz3aj_active[user_id] = emoji if emoji else random.choice(emoje)
    await event.respond(f"⌔∮ تم تفعيل الإزعاج بهذا الإيموجي {emoji} للشخص.")

@Qrh9.on(events.NewMessage(pattern=r".حذف_ازعاج"))
async def stop_iz3aj(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.respond("⌔∮ يرجى الرد على رسالة الشخص.")
    
    user_id = reply.sender_id
    if user_id in iz3aj_active:
        del iz3aj_active[user_id]
        await event.respond("⌔∮ تم إلغاء الإزعاج للشخص.")
    else:
        await event.respond("⌔∮ لا يوجد إزعاج مفعّل لهذا الشخص.")

@Qrh9.on(events.NewMessage())
async def iz3a(event):
    if event.sender_id in iz3aj_active:
        emoji = iz3aj_active.get(event.sender_id)
        if not emoji or not emoji.strip():
            emoji = random.choice(emoje)
        
        try:
            await Qrh9(SendReactionRequest(event.chat_id, event.id, [emoji]))
        except Exception as e:
            await event.respond(f"خطأ: {str(e)}")
