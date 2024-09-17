from telethon import events, functions, types
from telethon.tl.functions.users import GetFullUserRequest
from SHRU import Qrh9
import asyncio

onichans = {}

@Qrh9.on(events.NewMessage(pattern=r".مراقبة_حساب(?: |$)(.*)"))
async def s12(event):
    username = event.pattern_match.group(1)
    if not username:
        return await event.reply("⌔∮ يرجى إدخال اسم المستخدم.")
    
    user = await Qrh9(GetFullUserRequest(username))
    user_id = user.user.id
    onichans[user_id] = {
        "photo": user.user.photo,
        "bio": user.about,
        "status": user.user.status
    }

    await event.reply(f"⌔∮ بدأ مراقبة حساب {username}.")
    while user_id in onichans:
        await asyncio.sleep(60)
        new_user = await Qrh9(GetFullUserRequest(username))

        if new_user.user.photo != onichans[user_id]["photo"]:
            onichans[user_id]["photo"] = new_user.user.photo
            await event.respond(f"⌔∮ {username} قام بتغيير صورته الشخصية!")

        if new_user.about != onichans[user_id]["bio"]:
            onichans[user_id]["bio"] = new_user.about
            await event.respond(f"⌔∮ {username} قام بتحديث البايو!\nالبايو الجديد: {new_user.about}")

        if new_user.user.status != onichans[user_id]["status"]:
            onichans[user_id]["status"] = new_user.user.status
            if isinstance(new_user.user.status, types.UserStatusOnline):
                await event.respond(f"⌔∮ {username} متصل الآن!")
            elif isinstance(new_user.user.status, types.UserStatusOffline):
                await event.respond(f"⌔∮ {username} أصبح غير متصل!")

@Qrh9.on(events.NewMessage(pattern=r".إيقاف_مراقبة(?: |$)(.*)"))
async def stop_s12(event):
    username = event.pattern_match.group(1)
    if not username:
        return await event.reply("⌔∮ يرجى إدخال اسم المستخدم.")
    
    user = await Qrh9(GetFullUserRequest(username))
    user_id = user.user.id

    if user_id in onichans:
        del onichans[user_id]
        await event.reply(f"⌔∮ تم إيقاف مراقبة حساب {username}.")
    else:
        await event.reply(f"⌔∮ لا يتم مراقبة حساب {username} حالياً.")
