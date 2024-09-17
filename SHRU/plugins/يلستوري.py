import random
from telethon import events
from SHRU import Qrh9
from ..core.managers import edit_or_reply
from datetime import datetime, timedelta
afk = {}
user_join_times = {}
fshr_active = {}
w18 = [
    "⌔∮ عير بكسمك"
]

@Qrh9.on(events.NewMessage(pattern=r".فشر(?: |$)(.*)"))
async def fsh(event):
    reply = await event.get_reply_message()
    if not reply:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على رسالة الشخص")
    
    user_id = reply.sender_id
    words = event.pattern_match.group(1) or random.choice(w18)
    
    fshr_active[user_id] = words
    await edit_or_reply(event, f"⌔∮ تم تفعيل الفشار على الشخص، كل ما يرسل رسالة راح يجيه الرد: {words}")

@Qrh9.on(events.NewMessage(pattern=r".خلص"))
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



@Qrh9.on(events.ChatAction())
async def track_join(event):
    if event.user_joined or event.user_added:
        user_join_times[event.user_id] = datetime.now()

@Qrh9.on(events.NewMessage(pattern=r"\.تواجدي$"))
async def check_time(event):
    user_id = event.sender_id
    if user_id in user_join_times:
        join_time = user_join_times[user_id]
        now = datetime.now()
        time_diff = now - join_time
        days, seconds = time_diff.days, time_diff.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        response = f"⌔∮ صارلك متواجد هنا لمدة: {days} يوم، {hours} ساعة، و {minutes} دقيقة"
    else:
        response = "⌔∮ ما اكدر اعرف شكد صارلك داخل، يمكن دخلت قبل لا نبدي نتبع التواجد"

    await edit_or_reply(event, response)


@Qrh9.on(events.NewMessage(pattern=r".غياب (\d+)([smhd])(?: |$)(.*)"))
async def set_afk(event):
    duration_value = int(event.pattern_match.group(1))
    duration_type = event.pattern_match.group(2)
    reason = event.pattern_match.group(3) or "غير معروف"

    if duration_type == 's':
        duration = timedelta(seconds=duration_value)
    elif duration_type == 'm':
        duration = timedelta(minutes=duration_value)
    elif duration_type == 'h':
        duration = timedelta(hours=duration_value)
    elif duration_type == 'd':
        duration = timedelta(days=duration_value)

    afk_until = datetime.now() + duration

    afk[event.sender_id] = {
        "until": afk_until,
        "reason": reason
    }

    await edit_or_reply(event, f"⌔∮ تم تفعيل الغياب لمدة {duration_value}{duration_type} السبب: {reason}")

@Qrh9.on(events.NewMessage(pattern=r".رجعت"))
async def remove_afk(event):
    if event.sender_id in afk:
        del afk[event.sender_id]
        await edit_or_reply(event, "⌔∮ تم الالغاء منور")
    else:
        await edit_or_reply(event, "⌔∮ هله بيك")

@Qrh9.on(events.NewMessage())
async def auto_reply_afk(event):
    if event.sender_id in afk:
        afk_info = afk[event.sender_id]
        if datetime.now() < afk_info['until']:
            remaining_time = afk_info['until'] - datetime.now()
            await event.reply(f"⌔∮ المستخدم غايب لفتره السبب: {afk_info['reason']} باقي: {remaining_time}")
        else:
            del afk[event.sender_id]
            await event.reply("⌔∮ المستخدم رجع تكدر تراسله هسه")
