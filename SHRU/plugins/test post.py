from telethon import *
from telethon.tl import functions, types
from telethon.errors import RPCError
from SedUb import Qrh9
from ..core.managers import edit_or_reply
from ..sql_helper.autopost_sql import add_post, is_post, remove_post

@Qrh9.on(admin_cmd(pattern="(تفعيل_النشر)"))
async def auto_publish_in_super_groups(event):
    if not event.reply_to_msg_id:
        return await edit_or_reply(event, "❌ يجب أن ترد على رسالة معينة لتفعيل النشر.")

    previous_message = await event.get_reply_message()

    try:
        result = await event.client(functions.messages.GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=types.InputPeerEmpty(),
            limit=100,
            hash=0
        ))
    except RPCError as e:
        return await edit_or_reply(event, f"❌ فشل في الحصول على المجموعات: {e}")

    found_groups = [chat for chat in result.chats if chat.megagroup and ("سوبر" in chat.title or "super" in chat.title.lower())]

    if not found_groups:
        return await edit_or_reply(event, "❌ لا توجد مجموعات تحتوي على 'سوبر' أو 'super' في الاسم.")

    for group in found_groups:
        if not is_post(group.id, event.chat_id):
            add_post(str(group.id), event.chat_id)
            try:
                await event.client.send_message(group.id, previous_message)
            except RPCError as e:
                print(f"فشل في إرسال الرسالة إلى {group.title}: {e}")

    await edit_or_reply(event, f"✅ تم تفعيل النشر التلقائي في {len(found_groups)} مجموعة تحتوي على 'سوبر' أو 'super' في الاسم.")

@Qrh9.on(admin_cmd(pattern="(ايقاف_النشر)"))
async def stop_auto_publish(event):
    if not event.reply_to_msg_id:
        return await edit_or_reply(event, "❌ يجب أن ترد على رسالة معينة لإيقاف النشر.")

    result = await event.client(functions.messages.GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=types.InputPeerEmpty(),
        limit=100,
        hash=0
    ))

    found_groups = [chat for chat in result.chats if chat.megagroup and ("سوبر" in chat.title or "super" in chat.title.lower())]

    if not found_groups:
        return await edit_or_reply(event, "❌ لا توجد مجموعات تحتوي على 'سوبر' أو 'super' في الاسم.")

    for group in found_groups:
        if is_post(group.id, event.chat_id):
            remove_post(str(group.id), event.chat_id)

    await edit_or_reply(event, f"✅ تم إيقاف النشر التلقائي في {len(found_groups)} مجموعة تحتوي على 'سوبر' أو 'super' في الاسم.")
#خريط ترا